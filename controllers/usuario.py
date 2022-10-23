from models.usuario import Usuario
from repositorios.repositorioUsuario import RepositorioUsuario

class UsuarioControl():
    
    def __init__(self):
        print("Creando ControlUsuario")    
        self.repositorio_usuario = RepositorioUsuario()
                
    def get(self):
        usuarios = self.repositorio_usuario.findAll()
        return usuarios
    
    def create(self, datosUsuario):
        usuario = Usuario(datosUsuario)
        datos_salida = self.repositorio_usuario.save(usuario)
        return datos_salida
    
    def update(self, id, datosUsuario):
        buscar_usuario = self.repositorio_usuario.findById(id)
        usuario = Usuario(buscar_usuario)
        usuario.username = datosUsuario["username"]
        usuario.cedula = datosUsuario["cedula"]
        self.repositorio_usuario.save(usuario)
        return usuario.__dict__
    
    def find(self, id):
        buscar_usuario = self.repositorio_usuario.findById(id)
        usuario = Usuario(buscar_usuario)
        return usuario.__dict__
        
    def delete(self, id):
        print('Usuario ' + id + ' elinimado')
        usuario = self.repositorio_usuario.delete(id)
        return usuario    