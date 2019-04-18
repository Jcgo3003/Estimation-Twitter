from flask import Flask, redirect, render_template, request, url_for

import sys
import os
import helpers  #manda llamar helpers no se para que
from analyzer import Analyzer   #analazer por supuesto

app = Flask(__name__)   ###ASI LLAMA LA aplicacion

@app.route("/") ##asi le llama a esta funcion
def index():
    return render_template("index.html")##render_template - funcion llamar a una pagina web INDEX

@app.route("/search")   ##aqui la funcion se llama buscar
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    positive, negative, neutral = 0.0, 0.0, 0.0

    # If there is no tweets
    if tweets == None:
        return redirect(url_for("index"))

    #Initalize analyzer
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # feeding analyser
    analyzer = Analyzer(positives, negatives)

    # Couting tweets
    n = len(tweets)
    score = 0

    if n < 100:
        for i in range(0, n):
            score = analyzer.analyze(tweets[i])
            if score > 0.0:
                positive += 1.0
            elif score < 0.0:
                negative += 1.0
            else:
                neutral += 1.0

    elif n > 100:
        for i in range(0, 100):
            score = analyzer.analyze(tweets[i])
            if score > 0.0:
                positive += 1.0
            elif score < 0.0:
                negative += 1.0
            else:
                neutral += 1.0


    # generate chart
    chart = helpers.chart(positive, negative, neutral) #### llama a helpers.chart

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name) #regresa llama "redr_template" y lo llena con (search chart y screen_name)