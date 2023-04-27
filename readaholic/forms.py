from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FileField, TextAreaField, URLField, SelectField, FloatField
from wtforms.validators import Email, Length, EqualTo, DataRequired, URL, NumberRange, Optional

class AdminRegisterationForms(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')] )

    submit = SubmitField("Register")

class AdminLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6)])
    submit = SubmitField("Login")

class AddBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    isbn = StringField("ISBN",validators=[DataRequired()])
    genre = SelectField("Genre",validators=[DataRequired(),], choices = [('ed','Educational'), ('ck','Cooking'), ('fc','Fiction')])
    shoplink = URLField("Shop Link",validators=[DataRequired(), URL()])
    rating = FloatField("Rating", validators=[DataRequired(), NumberRange(min=0, max=10)])
    cover_image = FileField("Upload Cover Image")
    summary = TextAreaField("Tiny Summary",render_kw={"placeholder":"few words ..."}, validators=[DataRequired()])
    save =SubmitField("Save")

class AddComment(FlaskForm):
    name= StringField("Name", validators=[DataRequired()], render_kw={"placeholder":"Anonymous"})
    email = StringField("Email", validators=[DataRequired(), Email()])
    summary = TextAreaField("Comment", validators=[DataRequired()])
    comment =SubmitField("Comment")

