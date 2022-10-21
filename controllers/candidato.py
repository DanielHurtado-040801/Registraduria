from models.candidato import Candidato

class CandidatoControl():
    
    def __init__(self):
        print("Creando ControlCandidato")    
        
    def get(self):
        candidato = {
            "id": 1,
            "name": "0",
            "lema": "Petrosky mi presidente..."
        }    
        return candidato
    
    def create(self, datosCandidato):
        print("Se ha creado crrectamente el partido")
        candidato = Candidato(datosCandidato)
        return candidato.__dict__
    
    def update(self, id, datosCandidato):
        print('candidato con el id: ' + id + ' actualizado correctamente')
        candidato = Candidato(datosCandidato)
        return candidato.__dict__
    
    def find(self, id):
        print('candidato con el id: ' + id + 'encontrado')
        candidato = {
            "id": 1,
            "name": "0",
            "lema": "Petrosky mi presidente..."
        }  
        return candidato    
        
    def delete(self, id):
        print("candidato " + id + " eliminado")
        candidato = {
            "id": 1,
            "name": "0",
            "lema": "Petrosky mi presidente..."
        }   
        return candidato  