from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)

cors = CORS(app)

from app import routes
