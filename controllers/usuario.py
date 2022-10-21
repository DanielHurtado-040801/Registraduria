from models.usuario import Usuario

class UsuarioControl():
    
    def __init__(self):
        print("Creando ControlUsuario")    
        
    def get(self):
        usuario = {
            "id": 1,
            "username": "DanielH",
            "email": "daniel@gmail.com",
            "password": "123", 
            "cedula": "123456789",
            "is_Admin": True,
        }    
        return usuario
    
    def create(self, datosUsuario):
        print("Se ha creado crrectamente el usuario")
        usuario = Usuario(datosUsuario)
        return usuario.__dict__
    
    def update(self, id, datosUsuario):
        print('Usuario con el id: ' + id + ' actualizado correctamente')
        usuario = Usuario(datosUsuario)
        return usuario.__dict__
    
    def find(self, id):
        print('usuario con el id: ' + id + 'encontrado')
        usuario = {
            "id": 1,
            "username": "danielh",
            "email": "Daniel@gmail.com",
            "password": "123", 
            "cedula": "123456789",
            "is_Admin": True,
        }
        return usuario    
        
    def delete(self, id):
        print("Usuario " + id + " eliminado")
        usuario = {
            "id": 1,
            "cedula": "1000589224",
            "nombre": "Daniel",
            "apellido": "Hurtado"
        }
        return usuario    