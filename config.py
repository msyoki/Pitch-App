import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://msyoki:psql20*@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

class ProdConfig(Config):
    '''
    Production configuration child class 
    '''
    SQLALCHEMY_DATABASE_URI ='postgres://oyvdgupxolvxse:7f640312fec6b1693fccc9aa3a46307e7c4cee0c6f2756d6cfd2a00a8396cbbe@ec2-107-22-7-9.compute-1.amazonaws.com:5432/dfsofooub6js6n'

    

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG=True

class DevConfig(Config):
    '''
    Development configuration child class
    
    Arg:
        config: The parent configuration class with General connfiguration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://msyoki:psql20*@localhost/pitch'

    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}