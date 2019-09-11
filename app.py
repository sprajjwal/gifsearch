from flask import Flask, render_template, request
from random import sample
import requests 
import json

app = Flask(__name__)



@app.route('/')
def index():

    search_bar = request.args.get('search_bar')
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


