from flask_wtf import (
    FlaskForm
)

from wtforms.fields import (
    StringField,
    SelectField,
    FileField,
    TextAreaField
)

from wtforms.validators import (
    Length,
    DataRequired
)

class AddAnime(FlaskForm):
    title = StringField('Назва', validators=[Length(max=50), DataRequired()])
    description = TextAreaField('Опис', validators=[Length(max=500)])
    rating = SelectField('Рейтинг', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10')])

    image = FileField('Обкладинка')
    url = StringField('Посилання на аніме', validators=[DataRequired()])
