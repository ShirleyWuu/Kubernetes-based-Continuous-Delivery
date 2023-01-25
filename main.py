import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
import html

app = Flask(__name__)



@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Hello World! CD"


@app.route("/echo/<name>")
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


@app.route("/population/<region>/<year>")
def index(region, year):
    if region == "usa" and year == "2012":
        return render_template('map-usa.html')
    elif region == "hk" and year == "2011":
        return render_template('map-HK.html')
    # return render_template('map-usa.html')
    # return render_template('map-usa.html', title="page", jsonfile=json.dumps(data))

@app.route("/hk")
def indexHK():    
    return render_template('map-HK.html')

@app.route('/population/usa/usa_data')
def usa_data():
    # read file
    with open('./templates/USA.json', 'r') as myfile:
        data = myfile.read()
    return jsonify(data)

@app.route('/population/hk/hk_data')
def hk_data():
    # read file
    with open('./templates/HK.json', 'r') as myfile:
        data = myfile.read()
    return jsonify(data)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)