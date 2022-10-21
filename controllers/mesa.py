from models.mesa import Mesa

class MesaControl():
    
    def __init__(self):
        print("Creando ControlMesa")    
        
    def get(self):
        mesa = {
            "Numero_mesa": 1,
            "cantidad_cedulas_inscritas": "0",
        }    
        return mesa
    
    def create(self, datosMesa):
        print("Se ha creado crrectamente el mesa")
        mesa = Mesa(datosMesa)
        return mesa.__dict__
    
    def update(self, id, datosMesa):
        print('mesa con el id: ' + id + ' actualizado correctamente')
        mesa = Mesa(datosMesa)
        return mesa.__dict__
    
    def find(self, id):
        print('mesa con el id: ' + id + 'encontrado')
        mesa = {
            "Numero_mesa": 1,
            "cantidad_cedulas_inscritas": "0",
        }    
        return mesa    
        
    def delete(self, id):
        print("mesa " + id + " eliminado")
        mesa = {
            "Numero_mesa": 1,
            "cantidad_cedulas_inscritas": "0",
        }    
        return mesa  