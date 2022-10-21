from models.voto import Voto

class VotoControl():
    
    def __init__(self):
        print("Creando ControlVoto")    
        
    def get(self):
        voto = {
            "id": 1,
            "cedula_user": "123456789",
            "id candidato": "1",
            "Numero mesa": "1",
        }    
        return voto
    
    def create(self, datosVoto):
        print("Se ha creado crrectamente el voto")
        voto = Voto(datosVoto)
        return voto.__dict__
    
    def update(self, id, datosVoto):
        print('voto con el id: ' + id + ' actualizado correctamente')
        voto = Voto(datosVoto)
        return voto.__dict__
    
    def find(self, id):
        print('voto con el id: ' + id + 'encontrado')
        voto = {
            "id": 1,
            "cedula_user": "123456789",
            "id candidato": "1",
            "Numero mesa": "1",
        }    
        return voto    
        
    def delete(self, id):
        print("voto " + id + " eliminado")
        voto = {
            "id": 1,
            "cedula_user": "123456789",
            "id candidato": "1",
            "Numero mesa": "1",
        }    
        return voto  