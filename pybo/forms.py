from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입니다.')])
    content = TextField('내용', validators=[DataRequired('내용은 필수입니다.')])

class AnswerForm(FlaskForm):
    content = TextField('내용', validators=[DataRequired('내용은 필수입니다.')])

class UserCreateForm(FlaskForm):
    user_id = StringField('사용자ID', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', [DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    user_id = StringField('사용자 ID', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

