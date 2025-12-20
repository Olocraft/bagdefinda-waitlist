from flask import Flask, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/marketplace.html')
@app.route('/marketplace')
def marketplace():
    return send_from_directory(BASE_DIR, 'marketplace.html')

@app.route('/<path:filename>')
def serve_static(filename):
    # Allow serving static files with specific extensions
    allowed_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.css', '.js', '.ico', '.html'}
    _, ext = os.path.splitext(filename)

    if ext.lower() in allowed_extensions:
        return send_from_directory(BASE_DIR, filename)
    return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
