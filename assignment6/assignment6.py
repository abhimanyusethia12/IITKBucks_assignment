from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
my_map = {}
peers = []
#peers = ["http://127.0.0.1:8788/add", "http://127.0.0.1:8789/add"]

@app.route('/')
def home():
    return "Hello! Abhimanyu here :p"

@app.route('/add',methods=["POST"])
def add_and_broadcast():
    req_dict = request.get_json()
    key = req_dict['key']
    value = req_dict['value']
    if key in my_map:
        print("IGNORED- key is already in the map")
        return "Ignored"
    #setting key:value in map
    my_map[key] = value
    print('set %d:%s'%(key,value))
    
    #sending POST requests to all peers
    for url in peers:
        requests.post(url, json={key: value})
        print("sent POST request to URL- %s"%url)
    
    return jsonify(req_dict)

@app.route('/list')
def list_map():
    print("returning my map")
    print(my_map)
    return jsonify(my_map)

app.run(port=8787, debug=True)