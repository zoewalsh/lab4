import os
import sys

from flask import Flask, session, render_template, request, flash, redirect, abort, jsonify, current_app as app
from flask_session import Session
from datetime import datetime
import requests
import geojson
import json


app = Flask(__name__)

# fix windows terminal issue on my computer
if sys.platform.lower() == "win64":
    os.system('color')

# default route, no data is passed to index
@app.route("/", methods=['POST', 'GET'])
def index():
    url_services = request.url_root + 'static/Community_Services.geojson'
    url_schools = request.url_root + 'static/Schools.geojson'
    return render_template("index.html", url_services=url_services, url_schools=url_schools)
