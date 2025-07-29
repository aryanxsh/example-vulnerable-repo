#!/usr/bin/env python3
"""
Example vulnerable Flask application for testing SBOM scanner
This app intentionally uses vulnerable packages to demonstrate security scanning
"""

from flask import Flask, render_template_string, request, jsonify
import requests
import yaml
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Home page with vulnerable template"""
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vulnerable Test App</title>
    </head>
    <body>
        <h1>Vulnerable Test Application</h1>
        <p>This is a test application with known vulnerable dependencies.</p>
        <p>Use this repository to test your SBOM vulnerability scanner!</p>
        <ul>
            <li>Flask 0.12.3 - XSS vulnerability</li>
            <li>requests 2.19.1 - SSRF vulnerability</li>
            <li>PyYAML 5.1 - Code execution vulnerability</li>
            <li>Werkzeug 0.14.1 - Path traversal</li>
            <li>And more...</li>
        </ul>
    </body>
    </html>
    '''
    return render_template_string(template)

@app.route('/api/test')
def test_api():
    """Test endpoint that uses vulnerable packages"""
    try:
        # Using vulnerable requests library
        response = requests.get('https://httpbin.org/get')
        
        # Using vulnerable PyYAML
        yaml_data = yaml.load("""
        test:
          - item1
          - item2
        """, Loader=yaml.Loader)
        
        return jsonify({
            'status': 'success',
            'http_response': response.json(),
            'yaml_data': yaml_data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    """Vulnerable file upload endpoint"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Using vulnerable Werkzeug secure_filename
    filename = secure_filename(file.filename)
    
    # Save file (vulnerable to path traversal in older versions)
    file.save(os.path.join('uploads', filename))
    
    return jsonify({'message': f'File {filename} uploaded successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 