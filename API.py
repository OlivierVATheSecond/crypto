from flask import Flask
from Crypto import encrypt
import json


app = Flask(__name__, static_url_path='')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route("/refresh")
def refresh():
    alpha, cypher = encrypt()
    decrypt_map = dict()
    encrypt_map = dict()
    for i in range(len(alpha)):
        encrypt_map[alpha[i]] = cypher[i]
        decrypt_map[cypher[i]] = alpha[i]
    result = dict(cypher=cypher, alpha=alpha, encrypt=encrypt_map, decrypt=decrypt_map)

    with open('current-cypher.json', 'w') as f:
        f.write(json.dumps(result))
    return json.dumps(result)


@app.route("/alphabet")
def get_cypher():
    with open('current-cypher.json', 'r') as f:
        result = f.read()

    return result
