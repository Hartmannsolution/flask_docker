from app import app

import os
import json
from flask import jsonify 

with open('recipes.json','r') as jsonfile:
        diction = json.load(jsonfile)

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"

@app.route("/recipes")
def recipes():
    return jsonify(diction['recipes'])

@app.route("/recipe/<id>")
def recipe(id):
    return jsonify(diction['recipes'][id])