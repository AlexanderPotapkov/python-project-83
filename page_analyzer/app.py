import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return 'index'
