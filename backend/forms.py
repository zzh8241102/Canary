from ast import In
import string
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

class UserBasicInfoForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20, message='the length of the user name should be between 3 and 20')])
    email = wtforms.StringField(validators=[email(message='the email format is not correct')])
    # should be 11 digits
    phoneNumber = wtforms.StringField(validators=[length(min=11, max=11, message='the length of the phone number should be 11 digits')])
    location = wtforms.StringField(validators=[length(min=3, max=20, message='the length of the location should be between 3 and 20')])

class ChangePasswordForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20, message='the length of the user name should be between 3 and 20')])
    oldPassword = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])
    newPassword = wtforms.StringField(validators=[length(min=6, max=20, message='the length of the password should be between 6 and 20')])

class PostCommentForm(wtforms.Form):
    # article id should be a interger, db id
    article_id = wtforms.IntegerField(validators=[InputRequired(message='the article id should be a interger')])
    # comment should be a string
    content = wtforms.StringField(validators=[length(min=1, max=5000, message='the length of the comment should be between 1 and 5000')])
    commentor = wtforms.StringField(validators=[length(min=3, max=20, message='the length of the user name should be between 3 and 20')])

class PostArticleForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=1, max=300, message='the length of the title should be between 1 and 100')])
    content = wtforms.StringField(validators=[length(min=1, max=20000, message='the length of the content should be between 1 and 20000')])
    tags = wtforms.StringField(validators=[])
    author = wtforms.StringField(validators=[length(min=3, max=20, message='the length of the user name should be between 3 and 20')])
    # a list of tags

class AddNewTagForm(wtforms.Form):
    tag_name = wtforms.StringField(validators=[length(min=2, max=30, message='the length of the tag name should be between 2 and 30')])
    tag_description = wtforms.StringField(validators=[])