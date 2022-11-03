from models.jurado import Jurado
from models.mesa import Mesa
from models.usuario import Usuario
from repositorios.repositorioJurado import RepositorioJurado
from repositorios.repositorioMesa import RepositorioMesa
from repositorios.repositorioUsuario import RepositorioUsuario

class JuradoControl():
    
    def __init__(self):
        print("Creando ControlJurado")  
        self.repo_jurado = RepositorioJurado()  
        self.repo_mesa = RepositorioMesa()
        self.repo_usuario = RepositorioUsuario()
        
    def get(self):
        jurados = self.repo_jurado.findAll()
        return jurados
    
    def create(self):
        jurado = Jurado(datosJurado)
        datos_salida = self.repo_jurado.save(jurado)
        return datos_salida
    
    def update(self, id, datosJurado):
        buscar_jurado = self.repo_jurado.findById(id)
        jurado = Jurado(buscar_jurado)
        jurado.cedula_user = datosJurado["cedula_user"]
        jurado.numero_mesa = datosJurado["numero_mesa"]
        self.repo_jurado.save(jurado)
        return jurado.__dict__
    
    def find(self, id):
        jurado = self.repo_jurado.findById(id) 
        return jurado.__dict__    
        
    def delete(self, id):
        print("Jurado " + id + " eliminado")
        jurado = self.repo_jurado.delete(id)
        return jurado  
    
    def asignar_mesa_cedula(self, id_user, id_mesa,id_jurado):
        jurado_actual = Jurado(self.repo_jurado.findById(id_jurado))
        mesa_actual = Mesa(self.repo_mesa.findById(id_mesa))
        usuario_actual = Usuario(self.repo_usuario.findById(id_user))
        jurado_actual.mesa = mesa_actual
        jurado_actual.usuario = usuario_actual
        return self.repo_jurado.save(jurado_actual)  