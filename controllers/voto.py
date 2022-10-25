from models.voto import Voto
from models.mesa import Mesa
from models.usuario import Usuario
from models.candidato import Candidato
from repositorios.repositorioCandidato import RepositorioCandidato
from repositorios.repositorioMesa import RepositorioMesa
from repositorios.repositorioUsuario import RepositorioUsuario
from repositorios.repositorioVoto import RepositorioVoto

class VotoControl():
    
    def __init__(self):
        print("Creando ControlVoto")  
        self.repo_voto = RepositorioVoto()  
        self.repo_mesa = RepositorioMesa()
        self.repo_usuario = RepositorioUsuario()
        self.repo_candidato = RepositorioCandidato()
        
    def get(self):
        votos = self.repo_voto.findAll()
        return votos
    
    def create(self, datosvoto):
        voto = Voto(datosvoto)
        datos_salida = self.repo_voto.save(voto)
        return datos_salida
    
    def update(self, id, datosvoto):
        buscar_voto = self.repo_voto.findById(id)
        voto = Voto(buscar_voto)
        voto.cedula_user = datosvoto["cedula_user"]
        voto.numero_mesa = datosvoto["numero_mesa"]
        voto.id_candidato = datosvoto["id_candidato"]
        self.repo_voto.save(voto)
        return voto.__dict__
    
    def find(self, id):
        voto = self.repo_voto.findById(id) 
        return voto.__dict__    
        
    def delete(self, id):
        print("voto " + id + " eliminado")
        voto = self.repo_voto.delete(id)
        return voto  
    
    def votar(self, id_voto,id_user, id_mesa, id_candidato):
        voto_actual = Voto(self.repo_voto.findById(id_voto))
        mesa_actual = Mesa(self.repo_mesa.findById(id_mesa))
        usuario_actual = Usuario(self.repo_usuario.findById(id_user))
        candidato_actual = Candidato(self.repo_candidato.findById(id_candidato))
        voto_actual.mesa = mesa_actual
        voto_actual.usuario = usuario_actual
        voto_actual.candidato = candidato_actual
        return self.repo_voto.save(voto_actual)  