from models.partido import Partido
from repositorios.repositorioPartido import RepositorioPartido

class PartidoControl():
    
    def __init__(self):
        print("Creando ControlPartido")    
        self.repo_partido = RepositorioPartido()
        
    def get(self):
        partido = self.repo_partido.findAll()
        return partido
    
    def create(self, datosPartido):
        partido = Partido(datosPartido)
        datos_salida = self.repo_partido.save(partido)
        return datos_salida
    
    def update(self, id, datosPartido):
        buscar_partido = self.repo_partido.findById(id)
        partido = Partido(buscar_partido)
        partido.name = datosPartido["name"]
        partido.lema = datosPartido["lema"]
        self.repo_partido.save(partido)
        return partido.__dict__
    
    def find(self, id):
        buscar_partido = self.repo_partido.findById(id)
        partido = Partido(buscar_partido)
        return partido.__dict__
        
    def delete(self, id):
        print("partido " + id + " eliminado")
        partido = self.repo_partido.delete(id)
        return partido