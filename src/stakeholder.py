class Stakeholder:

    IMPORTANCIA_BASE = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.recomendaciones = 0

    def agregar_recomendacion(self, stakeholder):
        self.recomendaciones += 1

    def calcular_importancia(self):
        return self.IMPORTANCIA_BASE + self.recomendaciones
