import os

import pandas as pd

from flask import Blueprint
from flask import request, redirect, url_for, render_template, send_file, current_app



country_api = Blueprint('country_api', __name__)

@country_api.route('/country/<country_name>', methods=['GET', 'POST'])
def country_tab(country_name):
	print('country_api tab-----------------')

	if request.method == 'POST':
		if 'return_main_tab' in request.form:
			return redirect(url_for('main_tab'))

	df = pd.read_csv('static/data/text.csv')
	text = ' '.join(list(df['keyword']))
	text = text.replace('_', '')

	return render_template('country_search.html', country=country_name, text=text)

