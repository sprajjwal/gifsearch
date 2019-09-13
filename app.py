from flask import Flask, render_template, request
from random import sample, choice
import requests 
import json

# flask instantiation
app = Flask(__name__)

# route to the homepage
@app.route('/')
def index():
    search_bar = request.args.get('search_bar') #query for search
    if request.args.get('trending') == 'trending':  # trending gifs
        print("in trending")
        response = requests.get("https://api.tenor.com/v1/trending").json()
        search_bar = "Trending"
    else:
        status = True
        while status:  # loop to get random gifs so we don't get a page without gifs
            # grabbing a word from random.txt from spaceman
            if request.args.get('random') == "random" or request.args.get('search_bar') == "" or request.args.get('search_bar') == None:
                f=open("static/random.txt", "r")
                word_list = f.readlines()
                f.close
                word_list = word_list[0].split(' ')
                search_bar = choice(word_list)
            params = {  # parameters for API request
                "q": search_bar,
                "key": "B76YW88VZ3MZ"
            }
            response = requests.get("https://api.tenor.com/v1/search", params=params).json() # API request
            gifs = response["results"][0:10]   # Processing API for individual gifs
            if gifs or request.args.get('search_bar'):
                status = False

    gifs = response["results"][0:10]
    """Return homepage."""
    return render_template("index.html", response=response, gifs=gifs, search_bar= search_bar)

if __name__ == '__main__':
    app.run(debug=True)


