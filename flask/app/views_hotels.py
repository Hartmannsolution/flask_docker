from app import app

import os
import json
import sys
from flask import jsonify, render_template

with open('hotels_small.json','r') as jsonfile:
    diction = json.load(jsonfile)
    # print(diction)

@app.route("/")
def index():
    return render_template('./index_hotels.html')

@app.route("/hotel/all")
def tests():
    return jsonify(diction)

@app.route("/hotel/<id>")
def test(id):
    for hotel in diction:
        if str(hotel['id']) == str(id):
            return jsonify(hotel) 
    return jsonify({"code":400,"error":"no recipe exist with id: "+id}),400

@app.route('/<path:path>')
def catch_all(path):
    resp = {"code":400,"error":path+" is not a valid resource on this server"}
    return jsonify(resp), 400 # second value in returned tuple is the status code
