from flask import Flask, render_template, url_for, flash, redirect, request
from website import app, db
from website.models import User
from website.forms import Login, Register, Edit
import os
from flask_login import login_user, current_user, logout_user, login_required
import bcrypt

@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('home'))
    form = Register()
    if form.validate_on_submit():
        hashed = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        user = User(username=form.username.data, password=hashed, linkedin=form.linkedin.data, github=form.github.data, email=form.email.data, name=form.name.data, tagline=form.tagline.data, image=form.image.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Created account for {form.username.data}. You may now log in.', 'success')
        return redirect(url_for('login'))

    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
            login_user(user, remember=form.rememberMe.data)
            flash('Logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Error Logging In', 'danger')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/site/<username>', methods=['GET'])
def site(username):
    user = User.query.filter_by(username=username).first()
    return render_template('user.html', user=user)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = Edit()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.name = form.name.data
        current_user.tagline = form.tagline.data
        current_user.image = form.image.data
        current_user.linkedin = form.linkedin.data
        current_user.github = form.github.data
        current_user.email = form.email.data
        db.session.commit()
        flash('You have successfully updated your info!', 'success')
        return redirect(url_for("home"))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.name.data = current_user.name
        form.tagline.data = current_user.tagline
        form.image.data = current_user.image
        form.linkedin.data = current_user.linkedin
        form.github.data = current_user.github
        form.email.data = current_user.email
        return render_template("account.html", form=form)
    return 'big error'
