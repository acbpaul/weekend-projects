#%%
# Import inicial
import pandas as pd
import numpy as np

df = pd.read_csv('sample.csv')



#%%
# Funções de criação de colunas de atributos
def draw_asc_order(df):
    # Ordena as dezenas sorteadas em ordem crescente
    m = 6
    df['SEQ'] = None
    l = list(df.columns)
    l.pop(0)
    for n in range(m):
        df['{}A_ORD'.format(n+1)] = 0

    for i in range(len(df)):
        a = list(df[l].iloc[i])
        a.sort()
        df.at[i,'SEQ'] = a
        for n in range(m):
            df['{}A_ORD'.format(n+1)].iloc[i] = a[n]
        

    return df

# Valor médio acumulado
def order_avg_value(df):
    #TODO
    return df


df['Total'] = df[l].sum(axis=1)
#%% 
# df['Count1_0'] = 0
# df['Count1_1'] = 0
# df['Count1_2'] = 0
# df['Count1_3'] = 0
# df['Count1_4'] = 0
# df['Count1_5'] = 0

# df['Count2_0'] = 0
# df['Count2_1'] = 0
# df['Count2_2'] = 0
# df['Count2_3'] = 0
# df['Count2_4'] = 0
# df['Count2_5'] = 0
# df['Count2_6'] = 0
# df['Count2_7'] = 0
# df['Count2_8'] = 0
# df['Count2_9'] = 0


for col in l:
    df[col+'_t'] = df[col].apply(str)
    df[col+'_t'] = df[col+'_t'].apply(lambda x: '0'+ x if len(x) == 1 else x)
    df['Count1_0'] = df[col].apply(lambda x: x + 1 if int(np.floor(x / 10)) == 0 else x)

# %%
df1 = draw_asc_order(df)

# %%
