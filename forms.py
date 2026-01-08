from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class DlzbyForm(FlaskForm):
    dlznik = StringField(
        'Meno dlžníka:', 
        validators=[DataRequired()]
    )

    prijemca = StringField(
        'Meno príjemcu:',
        validators=[DataRequired()]
    )

    suma = StringField(
        'Suma v €:',
        validators=[DataRequired()]
    )

    poznamka = TextAreaField(
        'Poznámka:',
    )

    submit = SubmitField('Uložiť')