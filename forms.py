from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
# Define Form Class for Questionnaire
class MyForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    student_number = StringField('Student Number', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    course_grades = StringField('Grades Obtained in Courses', validators=[InputRequired()])
    satisfaction = SelectField('Overall Satisfaction with Academic Experience', choices=[
        ('', 'Select Satisfaction Level'),
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('unsatisfied', 'Unsatisfied'),
        ('very-unsatisfied', 'Very Unsatisfied')
    ], validators=[InputRequired()])
    improvements = TextAreaField('Suggestions for Improvement')