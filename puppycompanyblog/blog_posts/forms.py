from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    title = StringField('Title',render_kw={"placeholder":"Your Title Here"}, validators=[DataRequired()])
    text = TextAreaField('Text',render_kw={"placeholder":"Your Blog Comes Here !"}, validators=[DataRequired()])
    submit = SubmitField('BlogPost')
