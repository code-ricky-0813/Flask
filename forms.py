from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class MessageForm(FlaskForm):
    name = StringField('名字', validators=[DataRequired(), Length(max=20)])
    content = TextAreaField('留言', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('送出')