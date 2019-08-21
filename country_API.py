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

@country_api.route('/country/<country_name>/<sentiment_type>', methods=['GET', 'POST'])
def filter_by_sentiment(country_name, sentiment_type):
	'''
	PARAM sentiment_type
		0 - neu
		1 - pos
		2 - neg
	'''
	df = pd.read_csv('data/text.csv')
	use_cols = ['title', 'url', 'pos', 'neg', 'compound', 'country', 'socialimage', 'keyword']

	if country_name and len(country_name) > 0:
		df = df[df['country'] == country_name]
	if sentiment_type == 0:
		df = df[(df['pos'] > 0.104787) & df['pos'] > df['neg']].sort_values(by='pos', ascending=False)
	elif sentiment_type == 1:
		df = df[(df['neg'] > 0.093440) & df['pos'] < df['neg']].sort_values(by='neg', ascending=False)
	elif sentiment_type == 2:
		df = df[(df['pos'] < 0.104787) & (df['neg'] < 0.093440)].sort_values(by='neu', ascending=False)

	data = df[use_cols].to_dict('records')
	text = ' '.join(data['keyword'].tolist())
	return render_template('country_search.html', country=country_name, text=text)
