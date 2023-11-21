from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class WheatDataEntryForm(FlaskForm):
	"""
	Handles the input fields required for the wheat regression model
	"""
	
	year = IntegerField('Year', validators=[DataRequired()])
	# state = SelectField('State', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')], validators=[DataRequired()])
	area = IntegerField('Area', validators=[DataRequired()])
	tavg = FloatField('Average Temperature (Jun - October)', validators=[DataRequired()])
	cdd = IntegerField('Cooling Degree Days (Jun - October)', validators=[DataRequired()])
	hdd = IntegerField('Heating Degree Days (Jun - October)', validators=[DataRequired()])
	tmax = FloatField('Maximum Temperature (Jun - October)', validators=[DataRequired()])
	tmin = FloatField('Minimum Temperature (Jun - October)', validators=[DataRequired()])
	pzi = FloatField('Palmer Z-Index (Jun - October)', validators=[DataRequired()])
	pp = FloatField('Precipitation (Jun - October)', validators=[DataRequired()])
	lat = FloatField('latitude', validators=[DataRequired()])
	lon = FloatField('longitude', validators=[DataRequired()])
	run = SubmitField('Run')