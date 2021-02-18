from flask import Flask, render_template, url_for, flash, redirect, request
from website import app, db
from website.models import User
from flask_login import login_user, current_user, logout_user, login_required
# import bcrypt

@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

