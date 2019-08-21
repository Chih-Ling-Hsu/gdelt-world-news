#!/usr/bin/env python3

import os
from os import popen

from flask import Flask, request, redirect, url_for, render_template

from country_API import country_api


app = Flask(__name__, static_url_path="/static", static_folder="static")

app.register_blueprint(country_api)
# app.register_blueprint(information_api)
# app.register_blueprint(search_by_text_api)
# app.register_blueprint(preview_img_LV_api)
# app.register_blueprint(search_by_img_api)
# app.register_blueprint(tsne_api)
# app.register_blueprint(plot_3D_api)
# app.register_blueprint(classification_api)


@app.route("/", methods=["GET", "POST"])
def main_tab():
	
	return render_template("main.html")

if __name__ == "__main__":
	# load_CBIR()
	print("-----------------------------------------------")
	print("Start What is going on WEB-APP...")
	app.run(port=8000, host="0.0.0.0", threaded=True, debug=True)
