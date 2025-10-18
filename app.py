from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os

load_dotenv()  # load .env file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username == os.getenv('ADMIN_USER') and password == os.getenv('ADMIN_PASS'):
        return jsonify({"status": "success", "message": "Login successful"})
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
