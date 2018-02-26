import mongod
import pymongo
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')                                                                 
def home():
    return render_template('yay.html')

@app.route('/results')
def results(search, typeq):
    col = mongod.init()
    res
    if(typeq == "party"):
        res = mongod.find_party(search, col)
    if(typeq == "person"):
        splitted = search.split(" ")
        last = splitted[1]
        first = splitted[0]
        res = mongod.find_person(last, first, col)
    if(typeq == "twitter"):
        res = mongod.find_twitter(search, col)
    if(typeq == "state"):
        res = mongod.find_state(search, col)
    return render_template('results.html', res)

if __name__ == '__main__':
    app.debug = True
    app.run()
