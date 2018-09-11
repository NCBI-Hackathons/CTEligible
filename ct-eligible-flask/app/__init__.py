import os

from flask import Flask
from flask_pymongo import PyMongo


mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/ct-eligible')

app = Flask(__name__)
app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)
