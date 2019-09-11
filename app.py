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
    gifs = sample(response["results"], 10)

    """Return homepage."""
    # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("index.html", response=response, gifs=gifs, search_bar= search_bar)

if __name__ == '__main__':
    app.run(debug=True)


