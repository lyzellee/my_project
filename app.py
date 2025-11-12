from flask import Flask, render_template
from dotenv import load_dotenv
from config import Config
from models.db import db
from models.user_model import User
from flask_migrate import Migrate

import os


load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('registerpage.html')

if __name__ == '__main__':
    app.run(debug=True)