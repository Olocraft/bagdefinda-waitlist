from flask import Flask, request, jsonify, send_from_directory
import database
import os

app = Flask(__name__)

# Initialize DB on startup
database.init_db()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/marketplace.html')
@app.route('/marketplace')
def marketplace():
    return send_from_directory('.', 'marketplace.html')

@app.route('/<path:filename>')
def serve_static(filename):
    if filename in ['1-removebg-preview.png', 'index.html', 'marketplace.html']:
        return send_from_directory('.', filename)
    return "File not found", 404

@app.route('/api/waitlist', methods=['POST'])
def add_waitlist():
    data = request.json
    email = data.get('email')
    source = data.get('source', 'unknown')
    website = data.get('website', 'unknown')

    if not email:
        return jsonify({'success': False, 'message': 'Email is required'}), 400

    result = database.add_email(email, source, website)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
