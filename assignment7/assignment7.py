from flask import Flask, request, jsonify
from threading import Thread
import hashlib
import requests

app = Flask(__name__)

@app.route('/')
def home():
    print("server home accessed")
    return "Hello! This is Abhimanyu"

@app.route('/start',methods=["POST"])
def start_mining():
    data = (request.get_json())['data']
    global nonce
    nonce = -1
    
    def mine(data, nonce):
        target_string = '0000000f00000000000000000000000000000000000000000000000000000000'
        print("started mining with target string: %s \n and data: %s"%(target_string,data))
        target_int = int(target_string,16)
        maxnonce = 2 ** 32
        for i in range(maxnonce):
            print("trying for i: %d\n"%i)
            edited_string = data + str(i)
            hash_bytes = hashlib.sha256(edited_string.encode())
            hash_hexadecimal = hash_bytes.hexdigest()
            if(int(hash_hexadecimal,16)<target_int):
                break
            i += 1
        nonce = i
        print("completed mining with nonce value: %d"%nonce)

    thread1 = Thread(target=mine,args=[data,nonce,])
    print("/start: POST request received")
    thread1.start()
    return "mining",200

@app.route('/result')
def send_result():
    print("/result: GET request received")
    if nonce == -1:
        print("result: searching \n nonce: -1")
        return jsonify({"result":"searching","nonce":nonce})
    else:
        print("result: found \n nonce: %d" %nonce)
        return jsonify({"result":"found","nonce":nonce})

app.config['JSON_SORT_KEYS'] = False
if __name__ == '__main__':
    app.run(debug=True, port = 8787)
    