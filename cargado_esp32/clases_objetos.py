class Libro:
    def __init__ (self):
        self.iD = 0 # Nro. Tag Libro
        self.estado = True # Disponible= True/ En prestamo= False
        self.persona = 'Indefinido' #instanciaciones de objetos

    def reset(self):
        self.iD = 0
        self.estado = False

class Persona:
    def __init__ (self):
        self.id_persona = 0 #ID persona 
        self.libro_prestamo = '0x00000000' #Id del tag de libro, si tiene algun libro en prestamo

    def reset(self):
        self.id_persona = 0
        self.libro_prestamo = '0x00000000'