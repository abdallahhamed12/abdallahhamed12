from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello everybody'

@app.route('/hello')
def show_headers():
    headers = request.headers
    response = "HTTP Headers received:\n\n"
    
    for key, value in headers.items():
        response += f"{key}: {value}\n"
    
    response += f"\nClient IP: {request.remote_addr}"
    response += f"\nMethod: {request.method}"
    
    return f"<pre>{response}</pre>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Server running on port {port}")
    print(f"Visit http://localhost:{port}/hello to see headers")
    app.run(host='0.0.0.0', port=port)
