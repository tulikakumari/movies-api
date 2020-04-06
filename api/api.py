import flask
import requests
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/t2', methods=['GET'])
def tulika():
    return "<h1>Tuliks API</h1><p>My first api. <b> Hello</b></p>"


@app.route('/movies', methods=['GET'])
def movies():

    name = request.args.get('name')
    url = "http://www.omdbapi.com/?t=" + name+ "&apikey=2f03aad5"

    response = requests.request("GET", url)

    return response.text.encode('utf8')

app.run()