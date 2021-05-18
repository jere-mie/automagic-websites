from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from website.models import User

class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=60)])    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    linkedin = StringField('LinkedIn Profile', validators=[Length(min=0, max=60)])    
    github = StringField('GitHub Profile', validators=[Length(min=0, max=60)])    
    email = StringField('Email', validators=[Length(min=0, max=60)])    

    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username has already been used')

class Edit(FlaskForm):
    linkedin = StringField('LinkedIn Profile', validators=[Length(min=5, max=60)])    
    github = StringField('GitHub Profile', validators=[Length(min=5, max=60)])    
    email = StringField('Email', validators=[Length(min=5, max=60)])    
    submit = SubmitField('Edit')
    
class Login(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')  