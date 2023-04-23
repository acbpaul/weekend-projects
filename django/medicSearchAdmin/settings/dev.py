from .settings import * 

DEBUG = True 

#Crie a secret key para seu ambiente de desenvolvimento 
SECRET_KEY = 're78uia#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h' 

DATABASES = { 
    'default':{ 
        'ENGINE':'django.db.backends.postgresql_psycopg2', 
        'NAME':'django', 
        'USER':'acbpaul', 
        'PASSWORD':'senhadomedicsearchadmin', 
        'HOST':'medicSearchAdmin', 
        'PORT':'5432', 
    } 
}