from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, validators
from wtforms.validators import DataRequired


class LineEntryForm(FlaskForm):
    line = StringField('Line')

class StartForm(FlaskForm):
    script = SelectField('Ceremony', choices=[('pre', 'Pre-Ordeal')])
    role = SelectField('Role', choices = [('Kichkinet', 'Kichkinet')]) #, ('Meteu', 'Meteu'), ('Nutiket', 'Nutiket'), ('Allowat Sakima', 'Allowat Sakima')])
    admonition = PasswordField('Admonition', validators=[
        validators.Regexp('ahoalton', message='You have administered the admonition incorrectly.')
    ])