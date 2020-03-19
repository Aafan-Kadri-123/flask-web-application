from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, number_range


class FileForm(FlaskForm):
    filename = StringField('filename',
                           validators=[Length(min=2, max=20)], default="file1.txt")
    startline = StringField('Start Line Number',  
                                    default=-1)
    endline = StringField('End Line Number', default=-1)
    submit = SubmitField('Submit')


# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')