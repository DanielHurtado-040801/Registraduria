from models.jurado import Jurado
from repositorios.repositorioJurado import RepositorioJurado

class JuradoControl():
    
    def __init__(self):
        print("Creando ControlJurado")    
        self.repo_jurado = RepositorioJurado()
        
    def get(self):
        jurados = self.repo_jurado.findAll()
        return jurados
    
    def create(self, datosJurado):
        print("Se ha creado crrectamente el jurado")
        jurado = Jurado(datosJurado)
        return jurado.__dict__
    
    def update(self, id, datosJurado):
        print('Jurado con el id: ' + id + ' actualizado correctamente')
        jurado = Jurado(datosJurado)
        return jurado.__dict__
    
    def find(self, id):
        print('jurado con el id: ' + id + 'encontrado')
        jurado = {
            "id": 1,
            "cedula user": "123456789",
            "mesa": "1",
        }
        return jurado    
        
    def delete(self, id):
        print("jurado " + id + " eliminado")
        jurado = {
            "id": 1,
            "cedula_user": "1000589224",
            "numero mesa": "1",
        }
        return jurado  