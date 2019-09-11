from flask import Flask, render_template, request
from random import sample, choice
import requests 
import json

app = Flask(__name__)


@app.route('/')
def index():

    search_bar = request.args.get('search_bar')
    if request.args.get('random') == "random" or request.args.get('search_bar') == "":
        f=open("static/random.txt", "r")
        word_list = f.readlines()
        f.close
        word_list = word_list[0].split(' ')
        search_bar = choice(word_list)
    params = {
        "q": search_bar,
        "key": "B76YW88VZ3MZ"
    }

    response = requests.get("https://api.tenor.com/v1/search", params=params).json()
    gifs = response["results"][0:10]

    """Return homepage."""
    return render_template("index.html", response=response, gifs=gifs, search_bar= search_bar)

if __name__ == '__main__':
    app.run(debug=True)


