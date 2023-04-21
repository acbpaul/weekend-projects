# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:12:38 2023

@author: adr_p
"""

from functools import lru_cache
from os import PathLike

from pyspark import SparkContext
from pyspark.sql import SparkSession, DataFrame, Window
from pyspark.sql.functions import lit, lag, pow, when, lead




@lru_cache(maxsize=1)
def get_spark():
    sc = SparkContext(master="local[1]", appName="Speeding detector")
    spark = SparkSession(sc)
    return spark


def load_tracking(tracking_path: PathLike) -> DataFrame:
    return get_spark().read.json(str(tracking_path))


# TODO: Task #1
def detect_speeding_events(logs: DataFrame) -> DataFrame:
    
    # In pyspark
    w = Window.partitionBy(['customer_id','driver_id','vehicle_id']).orderBy('timespan')
    logs = logs.withColumn('lag_x', lag('location_x',1).over(w))
    logs = logs.withColumn('lag_y', lag('location_y',1).over(w))
    logs = logs.withColumn('lag_t', lag('timespan',1).over(w))
    
    logs = logs.withColumn('delta_x', logs['location_x'] - logs['lag_x'])
    logs = logs.withColumn('delta_y', logs['location_y'] - logs['lag_y'])
    logs = logs.withColumn('delta_t', logs['timespan'] - logs['lag_t'])
    
    logs = logs.withColumn('distance', pow(pow(logs['delta_x'],2) + pow(logs['delta_y'],2),1/2))
    logs = logs.withColumn('velocity', logs['distance']/logs['delta_t']*3600)
    logs = logs.withColumn('is_speeding', when(logs.velocity > logs.speed_limit, True).otherwise(False))
    
    logs = logs.drop('lag_x','lag_y', 'lag_t', 'delta_x', 'delta_y', 'delta_t', 'distance', 'velocity')
    
    # In pandas
    # for i in range(1,len(logs)):
    #     logs.loc[i,"delta_x"] = logs.loc[i,"location_x"] - logs.loc[i-1,"location_x"]
    #     logs.loc[i,"delta_y"] = logs.loc[i,"location_y"] - logs.loc[i-1,"location_y"]
    #     logs.loc[i,"delta_t"] = logs.loc[i,"timespan"]   - logs.loc[i-1,"timespan"]
    #     logs.loc[i,"travel_distance"] = sqrt(logs.loc[i,"delta_x"]*logs.loc[i,"delta_x"] + logs.loc[i,"delta_y"]*logs.loc[i,"delta_y"])
    #     logs.loc[i,"calculated_velocity"] = logs.loc[i,"travel_distance"] / logs.loc[i,"delta_t"] * 3600      
    #     logs.loc[i,"is_speeding"] = logs.loc[i,"calculated_velocity"] > logs.loc[i,"speed_limit"]
        
    return logs


# TODO: Task #2
def predict_speeding_event(logs_with_speeding: DataFrame, 
                           prediction_horizon: int) -> DataFrame:
    
    w = Window.partitionBy(['customer_id','driver_id','vehicle_id']).orderBy('timespan')
    
    logs_with_speeding = logs_with_speeding.withColumn('actually_speeding', lit(False))
    
    for i in range(1,prediction_horizon+1):
        logs_with_speeding = logs_with_speeding.withColumn('lag_'+str(i), lead('is_speeding',i).over(w))
        logs_with_speeding = logs_with_speeding.withColumn('actually_speeding', 
                                                           when((logs_with_speeding.will_be_speeding == logs_with_speeding['lag_'+str(i)]) & 
                                                                (logs_with_speeding.will_be_speeding== True), True).otherwise(False))
        logs_with_speeding = logs_with_speeding.drop('lag_'+str(i))
        
    
    return logs_with_speeding












