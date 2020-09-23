from . import main
from flask import render_template,url_for,flash,redirect
from .forms import RegistrationForm,LoginForm


@main.route('/')
def home():
    title= 'Home - Pitch APP '
    return render_template('index.html',title=title)


@main.route('/about')
def about():
    title= 'About - Pitch APP '
    return render_template('about.html',title=title)

@main.route('/pickup_lines')
def pickup_lines():
    title= 'pickup_lines '
    return render_template('pickup_lines.html',title=title)

@main.route('/interview_pitch')
def interview_pitch():
    title= 'interview_pitch '
    return render_template('interview_pitch.html',title=title)

@main.route('/products_pitch')
def products_pitch():
    title= 'products_pitch '
    return render_template('products_pitch.html',title=title)

@main.route('/promotion_pitch')
def promotion_pitch():
    title= 'promotion_pitch '
    return render_template('promotion_pitch.html',title=title)

@main.route('/register',methods= ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('.home'))
    return render_template('register.html',title='Register',form=form)

@main.route('/login',methods= ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'dualmyk@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('.home'))
        else:
            flash('Login Unsuccessful.Please check username and password', 'danger')
    return render_template('login.html',title='Login',form=form)