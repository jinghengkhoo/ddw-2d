from flask import render_template
from app.forms import WheatDataEntryForm
from app.regression import wheat_pred
from app import application

@application.route('/')
@application.route('/wheat', methods=['GET','POST'])
def wheat():
    """
    Route for handling wheat input data

    Methods:
    - GET: Renders the 'wheat.html' template with an empty form.
    - POST: Handles form submission, makes a prediction, and renders the template with the result.
    """
    form = WheatDataEntryForm()
    result = ""
    print("wheat loaded")
    if form.validate_on_submit():
        result = str(wheat_pred(form)) + "(1000 Bushels)"
    return render_template('wheat.html', form=form, result=result)
