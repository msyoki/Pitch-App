import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://msyoki:psql20*@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


    

class ProdConfig(Config):
    '''
    Production configuration child class 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Arg:
        config: The parent configuration class with General connfiguration settings
    '''

    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}