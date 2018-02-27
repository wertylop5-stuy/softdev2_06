import mongod
import pymongo
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')                                                                 
def home():
    return render_template('yay.html')

@app.route('/results', methods=["POST"])
def results():
    search = request.form['query']
    typeq = request.form['type']

    col = mongod.init()
    res = ["hi", "bye"]

    print search
    print typeq
    
    if(typeq == "party"):
        print 1
        res = mongod.find_party(search, col)
    if(typeq == "person"):
        print 2
        splitted = search.split(" ")
        print splitted
        last = splitted[1]
        first = splitted[0]
        res = mongod.find_person(last, first, col)
    if(typeq == "twitter"):
        print 3
        res = mongod.find_twitter(search, col)
    if(typeq == "state"):
        print 4
        res = mongod.find_state(search, col)
    print 0
    return render_template('results.html', docs=res)


if __name__ == '__main__':
    app.debug = True
    app.run()
