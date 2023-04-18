import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from requisito import Requisito
from stakeholder import Stakeholder
from algoritmo import algoritmo_greedy

class TestAlgoritmoGreedy(unittest.TestCase):

    STAKEHOLDER_1 = "Stakeholder 1"
    REQUISITO_1 = "Requisito 1"
    REQUISITO_2 = "Requisito 2"

    def test_solucion_exclusiones(self):
        stakeholder1 = Stakeholder(self.STAKEHOLDER_1)
        requisito1 = Requisito(self.REQUISITO_1)
        requisito2 = Requisito(self.REQUISITO_2)
        requisito3 = Requisito("Requisito 3")

        requisito1.agregar_stakeholder(stakeholder1)
        requisito2.agregar_stakeholder(stakeholder1)
        requisito3.agregar_stakeholder(stakeholder1)

        requisito1.agregar_exclusion(requisito2)

        limite_coste = 20
        solucion = algoritmo_greedy([requisito1, requisito2, requisito3], limite_coste)

        # Comprueba si la solución contiene los requisitos esperados
        self.assertIn(requisito1, solucion)
        self.assertNotIn(requisito2, solucion)
        self.assertIn(requisito3, solucion)

        # Comprueba si el coste acumulado es menor o igual al límite de coste
        coste_acumulado = sum([r.calcular_coste() for r in solucion])
        self.assertLessEqual(coste_acumulado, limite_coste)

    def test_solucion_implicaciones(self):
        stakeholder1 = Stakeholder(self.STAKEHOLDER_1)
        requisito1 = Requisito(self.REQUISITO_1)
        requisito2 = Requisito(self.REQUISITO_2)
        requisito3 = Requisito("Requisito 3")
        requisito4 = Requisito("Requisito 4")

        requisito1.agregar_stakeholder(stakeholder1)
        requisito2.agregar_stakeholder(stakeholder1)
        requisito3.agregar_stakeholder(stakeholder1)
        requisito4.agregar_stakeholder(stakeholder1)

        requisito1.agregar_implicacion(requisito2)
        requisito3.agregar_implicacion(requisito4)

        limite_coste = 40
        solucion = algoritmo_greedy([requisito1, requisito2, requisito3, requisito4], limite_coste)

        self.assertNotIn(requisito1, solucion)
        self.assertIn(requisito2, solucion)
        self.assertNotIn(requisito3, solucion)
        self.assertIn(requisito4, solucion)

    def test_solucion_combinaciones(self):
        
        stakeholder1 = Stakeholder(self.STAKEHOLDER_1)
        stakeholder2 = Stakeholder("Stakeholder 2")
        stakeholder3 = Stakeholder("Stakeholder 3")
        stakeholder4 = Stakeholder("Stakeholder 4")
        stakeholder5 = Stakeholder("Stakeholder 5")

        requisito1 = Requisito(self.REQUISITO_1)
        requisito2 = Requisito(self.REQUISITO_2)
        requisito3 = Requisito("Requisito 3")
        requisito4 = Requisito("Requisito 4")
        requisito5 = Requisito("Requisito 5")

        requisito1.agregar_stakeholder(stakeholder1)
        requisito2.agregar_stakeholder(stakeholder2)
        requisito3.agregar_stakeholder(stakeholder3)
        requisito1.agregar_stakeholder(stakeholder4)
        requisito4.agregar_stakeholder(stakeholder5)
        requisito5.agregar_stakeholder(stakeholder5)
        requisito5.agregar_stakeholder(stakeholder4)
        requisito2.agregar_stakeholder(stakeholder2)
        requisito4.agregar_stakeholder(stakeholder3)
        requisito4.agregar_stakeholder(stakeholder1)

        requisito1.agregar_exclusion(requisito2)
        requisito3.agregar_combinacion(requisito5)
        requisito4.agregar_implicacion(requisito2)

        limite_coste = 40
        solucion = algoritmo_greedy([requisito1, requisito2, requisito3, requisito4], limite_coste)

        self.assertIn(requisito1, solucion)
        self.assertIn(requisito3, solucion)
        self.assertIn(requisito5, solucion)

    def test_solucion_sin_espacio(self):
        stakeholder1 = Stakeholder(self.STAKEHOLDER_1)
        requisito1 = Requisito(self.REQUISITO_1)
        requisito2 = Requisito(self.REQUISITO_2)
        requisito3 = Requisito("Requisito 3")

        requisito1.agregar_stakeholder(stakeholder1)
        requisito2.agregar_stakeholder(stakeholder1)
        requisito3.agregar_stakeholder(stakeholder1)

        limite_coste = 5
        solucion = algoritmo_greedy([requisito1, requisito2, requisito3], limite_coste)

        self.assertEqual(len(solucion), 0)

if __name__ == '__main__':
    unittest.main()