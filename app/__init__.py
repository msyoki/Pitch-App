from flask import Flask
from .config import DevConfig

app = Flask(__name__)


posts = [
    {
        'title':'Blog post 1',
        'author':'Erick Musyoki',
        'date_post':'22 Sep 2020',
        'content':'Fist post content'
    },
    {
        'title':'Blog post 2',
        'author': 'Mike Mutua',
        'date_post':'23 Sep 2020',
        'content':'Second post content'
    }
]

# Setting up configuration
app.config.from_object(DevConfig)

from app import views
