class Requisito:
    COSTE = 10

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.stakeholders = []
        self.exclusiones = []
        self.implicaciones = []
        self.combinaciones = []
    
    def agregar_exclusion(self, requisito):
        if requisito not in self.exclusiones:
            self.exclusiones.append(requisito)
        if self not in requisito.exclusiones:
            requisito.exclusiones.append(self)

    def agregar_implicacion(self, requisito):
        self.implicaciones.append(requisito)

    def agregar_combinacion(self, requisito):
        if requisito not in self.combinaciones:
            self.combinaciones.append(requisito)
        if self not in requisito.combinaciones:
            requisito.combinaciones.append(self)

    def agregar_stakeholder(self, stakeholder):
        self.stakeholders.append(stakeholder)

    def calcular_satisfaccion(self):
        return sum([stakeholder.calcular_importancia() for stakeholder in self.stakeholders])

    def calcular_coste(self):
        return self.COSTE
    
    def es_factible(self, solucion_parcial):
        for requisito in solucion_parcial:
            if requisito in self.exclusiones or self in requisito.exclusiones:
                return False
            if self in requisito.implicaciones:
                return False
            if self in requisito.combinaciones and requisito not in self.combinaciones:
                return False
        return True
