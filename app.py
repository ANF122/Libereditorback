from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)  # Autorise toutes les origines

@app.route('/', methods=['GET'])
def index():
    return "Backend is running"

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.json.get('code', '')
    try:
        result = subprocess.run(['python3', '-c', code], capture_output=True, text=True)
        return jsonify({'stdout': result.stdout, 'stderr': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
