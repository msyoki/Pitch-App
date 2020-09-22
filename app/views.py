from app import app,posts
from flask import render_template

@app.route('/')
def hello_world():
    title= 'Home - Pitch APP '
    return render_template('index.html',posts=posts ,title=title)


@app.route('/about')
def about():
    title= 'About - Pitch APP '
    return render_template('about.html',title=title)

