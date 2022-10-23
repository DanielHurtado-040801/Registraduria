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


usuarioControl = UsuarioControl()
votosControl = VotoControl()
mesaControl = MesaControl()
juradoControl = JuradoControl()
candidatoControl = CandidatoControl()
partidoControl = PartidoControl()

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

"""RUTAS DE ADMIN --> USUARIOS"""

"""LISTAR USUARIOS (GET)"""
@app.route("/usuarios/",methods=['GET'])
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


"""RUTAS DE ADMIN --> VOTOS"""

"""LISTAR VOTOS (GET)"""
@app.route("/admin/votos/",methods=['GET'])
def getVotos():
    json=votosControl.get()
    return jsonify(json)

"""CREAR UN VOTO - (POST)"""
@app.route("/admin/votar",methods=['POST'])
def createVoto():
    dataEntrada = request.get_json()
    dataSalida=votosControl.create(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN VOTO - (DELETE)"""
@app.route("/admin/votos/delete/<string:id>",methods=['DELETE'])
def deleteVoto(id):
    json=votosControl.delete(id)
    return jsonify(json)

"""ACTUALIZAR UN VOTO - (PUT)"""
@app.route("/admin/votos/update/<string:id>", methods=['PUT'])
def actualizarVoto(id):
    data = request.get_json()
    json = votosControl.update(id, data)
    return jsonify(json)

"""BUSCAR VOTO - (GET)"""
@app.route("/admin/votos/find/<string:id>", methods=['GET'])
def buscarVoto(id):
    json = votosControl.find(id)
    return jsonify(json)

"""RUTAS DE ADMIN --> CANDIDATOS"""

"""LISTAR CANDIDATOS (GET)"""
@app.route("/admin/candidatos/",methods=['GET'])
def getCandidatos():
    json=candidatoControl.get()
    return jsonify(json)

"""CREAR UN CANDIDATO - (POST)"""
@app.route("/admin/candidatos",methods=['POST'])
def createCandidato():
    dataEntrada = request.get_json()
    dataSalida=candidatoControl.create(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN CANDIDATO - (DELETE)"""
@app.route("/admin/candidatos/delete/<string:id>",methods=['DELETE'])
def deleteCandidato(id):
    json=candidatoControl.delete(id)
    return jsonify(json)

"""ACTUALIZAR UN CANDIDATO - (PUT)"""
@app.route("/admin/candidatos/update/<string:id>", methods=['PUT'])
def actualizarCandidato(id):
    data = request.get_json()
    json = candidatoControl.update(id, data)
    return jsonify(json)

"""BUSCAR CANDIDADTO - (GET)"""
@app.route("/admin/candidatos/find/<string:id>", methods=['GET'])
def buscarCandidato(id):
    json = candidatoControl.find(id)
    return jsonify(json)

"""ASIGNAR PARTIDO A UN CANDIDATO - (PUT)"""
@app.route("/admin/candidato/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartido(id, id_partido):
    json = candidatoControl.asignarPartido(id, id_partido)
    return jsonify(json)


"""RUTAS DE ADMIN --> MESAS VOTACION"""

"""LISTAR MESAS (GET)"""
@app.route("/admin/mesas/",methods=['GET'])
def getMesas():
    json=mesaControl.get()
    return jsonify(json)

"""CREAR UN MESA - (POST)"""
@app.route("/admin/mesas",methods=['POST'])
def createMesa():
    dataEntrada = request.get_json()
    dataSalida=mesaControl.create(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN MESA - (DELETE)"""
@app.route("/admin/mesas/delete/<string:id>",methods=['DELETE'])
def deleteMesa(id):
    json=mesaControl.delete(id)
    return jsonify(json)

"""ACTUALIZAR UN MESA - (PUT)"""
@app.route("/admin/mesas/update/<string:id>", methods=['PUT'])
def actualizarMesa(id):
    data = request.get_json()
    json = mesaControl.update(id, data)
    return jsonify(json)

"""BUSCAR MESA - (GET)"""
@app.route("/admin/mesas/find/<string:id>", methods=['GET'])
def bsucarMesa(id):
    json = mesaControl.find(id)
    return jsonify(json)


"""RUTAS DE ADMIN --> JURADOS"""

"""LISTAR JURADOS (GET)"""
@app.route("/admin/jurados/",methods=['GET'])
def getJurados():
    json=juradoControl.get()
    return jsonify(json)

"""CREAR UN JURADO - (POST)"""
@app.route("/admin/jurado",methods=['POST'])
def createJurado():
    dataEntrada = request.get_json()
    dataSalida=juradoControl.create(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN JURADO - (DELETE)"""
@app.route("/admin/jurados/delete/<string:id>",methods=['DELETE'])
def deleteJurado(id):
    json=juradoControl.delete(id)
    return jsonify(json)

"""ACTUALIZAR UN JURADO - (PUT)"""
@app.route("/admin/jurados/update/<string:id>", methods=['PUT'])
def actualizarJurado(id):
    data = request.get_json()
    json = juradoControl.update(id, data)
    return jsonify(json)

"""BUSCAR JURADO - (GET)"""
@app.route("/admin/jurados/find/<string:id>", methods=['GET'])
def buscarJurado(id):
    json = juradoControl.find(id)
    return jsonify(json)


"""RUTAS DE ADMIN --> PARTIDOS"""

"""LISTAR PARTIDOS (GET)"""
@app.route("/admin/partidos/",methods=['GET'])
def getPartidos():
    json=partidoControl.get()
    return jsonify(json)

"""CREAR UN PARTIDO - (POST)"""
@app.route("/admin/partidos",methods=['POST'])
def createPartido():
    dataEntrada = request.get_json()
    dataSalida=partidoControl.create(dataEntrada)
    return jsonify(dataSalida)

"""ELIMINAAR UN PARTIDO - (DELETE)"""
@app.route("/admin/partidos/delete/<string:id>",methods=['DELETE'])
def deletePartido(id):
    json=partidoControl.delete(id)
    return jsonify(json)

"""ACTUALIZAR UN PARTIDO - (PUT)"""
@app.route("/admin/partidos/update/<string:id>", methods=['PUT'])
def actualizarPartido(id):
    data = request.get_json()
    json = partidoControl.update(id, data)
    return jsonify(json)

"""BUSCAR PARTIDO - (GET)"""
@app.route("/admin/partidos/find/<string:id>", methods=['GET'])
def buscarPartido(id):
    json = partidoControl.find(id)
    return jsonify(json)



if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])