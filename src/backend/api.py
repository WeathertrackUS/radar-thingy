from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "API is running"})

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the API for radar thingy. Use /api/health to check the status."})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)