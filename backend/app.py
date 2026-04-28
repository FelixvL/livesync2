from flask import Flask, jsonify,request
from flask_cors import CORS

import auto_uit_db

app = Flask(__name__)
CORS(app)

@app.route("/get_alle_autos")
def get_alle_autos_ep():
    return jsonify(auto_uit_db.get_all_autos())

@app.route("/maak_auto", methods=["POST"])
def maak_auto_ep():
    auto_uit_db.maak_auto()
    return jsonify({"message": "Auto succesvol gemaakt!"}), 201