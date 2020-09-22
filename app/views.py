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

@app.route('/pickup_lines')
def pickup_lines():
    title= 'pickup_lines '
    return render_template('pickup_lines.html',title=title)

@app.route('/interview_pitch')
def interview_pitch():
    title= 'interview_pitch '
    return render_template('interview_pitch.html',title=title)

@app.route('/products_pitch')
def products_pitch():
    title= 'products_pitch '
    return render_template('products_pitch.html',title=title)

@app.route('/promotion_pitch')
def promotion_pitch():
    title= 'promotion_pitch '
    return render_template('promotion_pitch.html',title=title)