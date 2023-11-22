from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class WheatDataEntryForm(FlaskForm):
	"""
	Handles the input fields required for the wheat regression model
	"""
	area = IntegerField('Area', validators=[DataRequired()])
	lon = FloatField('longitude', validators=[DataRequired()])
	lat = FloatField('latitude', validators=[DataRequired()])
	hdd = IntegerField('Heating Degree Days (Jun - October)', validators=[DataRequired()])
	tavg = FloatField('Average Temperature (Jun - October)', validators=[DataRequired()])
	tdiff = FloatField('Temperature Difference (Max - Min) (Jun - October)', validators=[DataRequired()])
	run = SubmitField('Run')