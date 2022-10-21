from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from controllers.partido import PartidoControl
from controllers.candidato import CandidatoControl
from controllers.jurado import JuradoControl
from controllers.mesa import MesaControl
from controllers.usuario import UsuarioControl
from controllers.voto import VotoControl

app=Flask(__name__)
cors = CORS(app)


"""RUTAS DE API (PATHS)"""

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

"""RUTAS DE ADMIN"""

"""LISTAR USUARIOS (GET)"""
usuarioControl = UsuarioControl()
@app.route("/admin/usuarios/",methods=['GET'])
def getUsuarios():
    json=usuarioControl.get()
    return jsonify(json)

"""CREAR UN USUARIO - (POST)"""
@app.route("/usuarios",methods=['POST'])
def createUsuarios():
    dataEntrada = request.get_json()
    dataSalida=usuarioControl.create(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN USUARIOS - (DELETE)"""
@app.route("/admin/usuarios/delete/<string:id>",methods=['DELETE'])
def deleteUsuario(id):
    json=usuarioControl.delete(id)
    return jsonify(json)

"""ACTUALIZAR UN USUARIO - (PUT)"""
@app.route("/admin/usuarios/update/<string:id>", methods=['PUT'])
def actualizarUsuario(id):
    data = request.get_json()
    json = usuarioControl.update(id, data)
    return jsonify(json)

"""BUSCAR USUARIO - (GET)"""
@app.route("/admin/usuarios/find/<string:id>", methods=['GET'])
def buscarUsuario(id):
    json = usuarioControl.find(id)
    return jsonify(json)


if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])