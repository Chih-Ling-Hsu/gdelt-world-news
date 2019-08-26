from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

'''
PARAM str
    headline
RETURN json object
    {'neg': 0.219, 'neu': 0.616, 'pos': 0.164, 'compound': -0.2023}
'''
def get_sentiment_scores(headline):
    score = analyser.polarity_scores(headline)
    return score

if __name__ == '__main__':
    headlines = ['Will Jamie Foxx and Katie Holmes Get Back Together? - Showbiz Cheat Sheet', "Antonio Brown actually shows up for Raiders' practice and it appears his crazy helmet saga could be over - CBS Sports", 'Larry King Files for Divorce from Wife Shawn After 22 Year Marriage - TMZ', 'Task Force Updates Breast Cancer Recommendations - WebMD', '‘Matrix 4’ Officially a Go With Keanu Reeves, Carrie-Anne Moss and Lana Wachowski (EXCLUSIVE) - Variety', 'Fortnite’s latest tournament proved nobody is right about the mechs - Polygon', 'Disney-Sony Standoff Ends Marvel Studios & Kevin Feige’s Involvement In ‘Spider-Man’ - Deadline', "NASA confirms mission to Jupiter's moon Europa - Engadget", 'Bank watchdogs approve rule to loosen ban on risky Wall Street trades | TheHill - The Hill', "Italy's prime minister resigns as government nears collapse - New York Post ", 'Lightning-compatible YubiKey 5Ci could secure your iPhone logins - Engadget', "Why Anthony Scaramucci's rebellion bothers Donald Trump so much - CNN", 'CDC: 11 Hoosiers with History of Vaping have Lung Illnesses - WBIW.com', "'We Should Be Retreating Already From the Coastline,' Scientist Suggests After Finding Warm Waters Below Greenland - EcoWatch", "Catherine Rampell: Move over, Illuminati. The conspiracy against Trump's economy is massive. - Salt Lake Tribune", "Stocks making the biggest moves midday: Home Depot, MSG, Kohl's, Beyond Meat & more - CNBC", "A Guide To What's Happening In Hong Kong - NPR", "'Complete garbage': White House spokesman goes after media for refusing 'to call out anti-Semitism' - Washington Examiner", 'Police shoot man who took bus passengers hostage in Brazil - CBS News', 'Microsoft: the Next Version of Edge Is Ready for Daily Use, Launches Beta Builds - Thurrott.com']
    for h in headlines:
        print(h, get_sentiment_scores(h))
