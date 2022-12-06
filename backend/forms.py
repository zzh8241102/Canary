import wtforms
from wtforms.validators import length, email, EqualTo, InputRequired

class Register_form(wtforms.Form):
    user_name = wtforms.StringField(validators=[length(min=4, max=20, message='the length of the user name should be between 4 and 20')])
    user_password = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])


class Login_form(wtforms.Form):
    user_name = wtforms.StringField(validators=[length(min=4, max=20, message='the length of the user name should be between 4 and 20')])
    user_password = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])

class Change_password_form(wtforms.Form):
    old_password = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])
    new_password = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])
    confirm_password = wtforms.StringField(validators=[EqualTo('new_password', message='the two passwords are not the same')])