#!/usr/bin/env python 

from flask import Flask, json, render_template, request
import os

#create instance of flask app
app = Flask(__name__) # for our namespace

#decorator
@app.route("/") # calling a function called "route"
def echo_hello():
    return "Hello World!"

@app.route("/gdp")
def gdp():
    json_url = os.path.join(app.static_folder, "", "us_gdp.json")
    data_json = json.load(open(json_url))

    # pass in the json_data into the data part of the html template we made
    return render_template('index.html', data=data_json)

@app.route("/gdp/<year>")
def gdp_year(year):
    json_url = os.path.join(app.static_folder, "", "us_gdp.json")
    data_json = json.load(open(json_url))

    data = data_json[1]
    year = request.view_args['year']

    output_data = [x for x in data if x['date']==year]
    return render_template('index.html', data=output_data)

# if this is the main file that we're calling...then we want to do stuff
if __name__ == "_main_":
    app.run(debug=True)