from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField("Email", validators=[Required(),
                                             Length(1, 64),
                                             Email()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")

class RegistrationForm(Form):
    email = StringField("Email", validators=[Required(),
                                             Length(1, 64),
                                             Email()])
    user_name = StringField("User name", validators=[Required(),
                                             Length(1, 64),
                                             Regexp("^[A-Za-z][A-Za-z0-9_.]*$",
                                                    0,
                                                    "User names must have ,\
                                                    only letters, numbers, \
                                                    dots or underscores")])

    password = PasswordField("Password",
                             validators=[Required(), EqualTo("password2",
                                         message="Passwords must match")])
    password2 = PasswordField("Confirm Password", validators=[Required()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered")

    def validate_user_name(self, field):
        if User.query.filter_by(user_name=field.data).first():
            raise ValidationError("User name already registered")



