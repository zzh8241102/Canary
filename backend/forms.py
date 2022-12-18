from ast import In
import wtforms
from wtforms.validators import length, email, EqualTo, InputRequired
# ////////////////////////////////////////////////////////////////////////

class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
    email = wtforms.StringField(validators=[email(message='the email format is not correct')])

# ////////////////////////////////////////////////////////////////////////

class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20, message='the length of the user name should be between 3 and 20')])
    password = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])
    
# ////////////////////////////////////////////////////////////////////////
class ChangePasswordForm(wtforms.Form):
    old_password = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])
    new_password = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])
    confirm_password = wtforms.StringField(validators=[EqualTo('new_password', message='the two passwords are not the same')])

class UserBasicInfoForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=4, max=20, message='the length of the user name should be between 4 and 20')])
    email = wtforms.StringField(validators=[email(message='the email format is not correct')])
    phoneNumber = wtforms.StringField(validators=[length(min=2, max=11, message='the length of the phone number should be 11')])
    location = wtforms.StringField(validators=[length(min=4, max=20, message='the length of the location should be between 4 and 20')])

# class NewTagForm(wtforms.Form):
#     tag_name = wtforms.StringField(validators=[length(min=4, max=20, message='the length of the tag name should be between 4 and 20')])
#     tag_description = wtforms.StringField(validators=[length(min=4, max=20, message='the length of the tag description should be between 4 and 20')])