from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.json.get('code')
    try:
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
        return jsonify({'stdout': result.stdout, 'stderr': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
