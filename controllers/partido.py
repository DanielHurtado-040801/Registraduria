from models.partido import Partido

class PartidoControl():
    
    def __init__(self):
        print("Creando ControlPartido")    
        
    def get(self):
        partido = {
            "id": 1,
            "name": "0",
            "lema": "Petrosky mi presidente..."
        }    
        return partido
    
    def create(self, datosPartido):
        print("Se ha creado crrectamente el partido")
        partido = Partido(datosPartido)
        return partido.__dict__
    
    def update(self, id, datosPartido):
        print('partido con el id: ' + id + ' actualizado correctamente')
        partido = Partido(datosPartido)
        return partido.__dict__
    
    def find(self, id):
        print('partido con el id: ' + id + 'encontrado')
        partido = {
            "id": 1,
            "name": "0",
            "lema": "Petrosky mi presidente..."
        }  
        return partido    
        
    def delete(self, id):
        print("partido " + id + " eliminado")
        partido = {
            "id": 1,
            "name": "0",
            "lema": "Petrosky mi presidente..."
        }   
        return partido  