from flask import Flask, jsonify,request
from dataclasses import dataclass
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@dataclass
class Fiets:
    merk:str

@app.route("/")
def hello_world():
    return "<h1>Hello, Weer wat FGWW!</h1>"

@app.route("/tweede")
def hello_world_tweede():
    return "<p>Hello, felix</p>"

@app.route("/derde/<naam>")
def hello_world_derde(naam):
    return f"hoi: {naam}"

@app.route("/vierde/<>")
def vierde():
    fiets1 = Fiets("Gazelle")
    fiets2 = Fiets("batavus2")
    return jsonify(fiets1)   

@app.route("/vijfde", methods=["GET","POST"])
def vijfde():
    if request.method == "GET":
        return "no"
    return "yes"

@app.route("/zesde", methods=["POST"])
def zesde():
    print(request.json)
    print(request.json.get("naam"))
    print(request.json.get("naam").upper())
    return "yes"+request.json.get("naam")