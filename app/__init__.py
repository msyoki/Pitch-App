from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = '3a58c9a4a8d5d9e456de6650505514d5'

posts = [
    {
        'title':'Pitch post 1',
        'author':'Erick Musyoki',
        'date_post':'22 Sep 2020',
        'content':'Fist post content'
    },
    {
        'title':'Pitch post 2',
        'author': 'Mike Mutua',
        'date_post':'23 Sep 2020',
        'content':'Second post content'
    }
]



# Initializing flask extensions
db.init_app(app)


# Setting up configuration
app.config.from_object(DevConfig)

from app import views
