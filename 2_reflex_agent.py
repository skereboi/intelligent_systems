"""
Agente Reflectivo Simple - Sistemas Inteligentes Inv 2024
"""
# Reglas
ACCIONES = {
    'moneda': 'pedir-codigo',
    'a1': 'servir-bebida1',
    'a2': 'servir-bebida2',
    'a3': 'servir-bebida3'
    }

class AgenteReactivoSimple:
    """Agente racional de tipo Reactivo"""   
    # Constructor
    def __init__(self, reglas):
        self.reglas = reglas
        self.percepciones = ""

    def actuar(self, percepcion, accion_basica=''):
        """Actua segun una percepcion, devuelve una accion"""
        if not percepcion:
            return accion_basica
        if percepcion in self.reglas.keys():
            return self.reglas[percepcion]
        return accion_basica

expendedora = AgenteReactivoSimple(ACCIONES)
percepcion = input("Indicar Percepcion: ")

while percepcion:
    accion = expendedora.actuar(percepcion, 'reiniciarse')
    print(accion)
    percepcion = input("Indicar Percepcion: ")

# Agente 

