# Fika News
Fika News is a plateform created to show the user a global view of the news around the World.

<p align="center">
<img src="images/plateform_overview.png">
</p>

It uses data from [GDELT](https://www.gdeltproject.org) and key words from trending topics to create an interactive way to visualise the news.

  - News by country
  - Sentiment analysis
  - Word Cloud


## Introduction

For a lightweight introduction to the rationale of the project, please take a
look at the presentation in `presentation/index.html` it was made with
[reveal.js](https://github.com/hakimel/reveal.js) and can be viewed in any
browser.

## Usage
You just need to set up the virtual environment either with conda or virtualenv
and pip

```sh
$ conda create -n fika-news
$ conda activate fika-news
$ conda install -c anaconda pandas
$ conda install -c anaconda flask
```

download the data files at the data folder and then run
```sh
$ python runPlateform.py
```

## New Features are coming!

  - Knowledge graph
  - History telling

## Contacts
Please contact  _[matheusfranca.t19@gmail.com](matheusfranca.t19@gmail.com)_  or open an issue for any questions or suggestions.

Thanks! (●'◡'●)
