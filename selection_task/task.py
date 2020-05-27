from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/hash',methods=["POST"])
def finds_hash():
    req_dict = request.get_json()
    source = req_dict['data']
    hash_bytes = hashlib.sha256(source.encode())
    hash_hex = hash_bytes.hexdigest()
    return jsonify(hash = hash_hex)

app.run(port=8787, debug=True)
