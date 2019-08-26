#!/usr/bin/env python3

import os
import pandas as pd

from flask import Flask, request, redirect, url_for, render_template

from country_API import country_api


app = Flask(__name__, static_url_path="/static", static_folder="static")

app.register_blueprint(country_api)

@app.route("/", methods=["GET", "POST"])
def main_tab():
	
	df = pd.read_csv('static/data/text.csv')
	text = ' '.join(list(df['keyword']))
	text = text.replace('_', '')

	return render_template("main.html", text=text)

if __name__ == "__main__":
	# load_CBIR()
	print("-----------------------------------------------")
	print("Start What is going on WEB-APP...")
	app.run(port=8000, host="0.0.0.0", threaded=True, debug=True)
