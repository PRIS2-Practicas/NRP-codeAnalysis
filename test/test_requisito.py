import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from requisito import Requisito
from stakeholder import Stakeholder
from algoritmo import algoritmo_greedy

class TestRequisito(unittest.TestCase):

    STAKEHOLDER_1 = "Stakeholder 1"

    def setUp(self):
        self.requisito1 = Requisito("Requisito 1")
        self.requisito2 = Requisito("Requisito 2")
        self.stakeholder1 = Stakeholder("Stakeholder 1")
        self.stakeholder2 = Stakeholder("Stakeholder 2")

    def test_agregar_exclusion(self):
        self.requisito1.agregar_exclusion(self.requisito2)
        self.assertIn(self.requisito2, self.requisito1.exclusiones)
        self.assertIn(self.requisito1, self.requisito2.exclusiones)
    
    def test_agregar_exclusion_duplicada(self):
        self.requisito1.agregar_exclusion(self.requisito2)
        self.requisito1.agregar_exclusion(self.requisito2)

        # Verificamos que la exclusión se agregó solo una vez
        self.assertEqual(self.requisito1.exclusiones.count(self.requisito2), 1)
        self.assertEqual(self.requisito2.exclusiones.count(self.requisito1), 1)

    def test_agregar_implicacion(self):
        self.requisito1.agregar_implicacion(self.requisito2)
        self.assertIn(self.requisito2, self.requisito1.implicaciones)

    def test_agregar_combinacion(self):
        self.requisito1.agregar_combinacion(self.requisito2)
        self.assertIn(self.requisito2, self.requisito1.combinaciones)
        self.assertIn(self.requisito1, self.requisito2.combinaciones)

    def test_agregar_combinacion_duplicada(self):
        self.requisito1.agregar_combinacion(self.requisito2)
        self.requisito1.agregar_combinacion(self.requisito2)  # Agregamos la misma combinación otra vez

        # Verificamos que la combinación se agregó solo una vez
        self.assertEqual(self.requisito1.combinaciones.count(self.requisito2), 1)
        self.assertEqual(self.requisito2.combinaciones.count(self.requisito1), 1)

    def test_agregar_stakeholder(self):
        self.requisito1.agregar_stakeholder(self.stakeholder1)
        self.assertIn(self.stakeholder1, self.requisito1.stakeholders)

    def test_calcular_satisfaccion(self):
        self.requisito1.agregar_stakeholder(self.stakeholder1)
        self.requisito1.agregar_stakeholder(self.stakeholder2)
        self.stakeholder1.calcular_importancia = lambda: 2
        self.stakeholder2.calcular_importancia = lambda: 3
        self.assertEqual(self.requisito1.calcular_satisfaccion(), 5)

    def test_calcular_coste(self):
        self.assertEqual(self.requisito1.calcular_coste(), 10)

    def test_es_factible(self):
        self.requisito1.agregar_exclusion(self.requisito2)
        self.assertFalse(self.requisito1.es_factible([self.requisito2]))
        self.assertFalse(self.requisito2.es_factible([self.requisito1]))
        self.requisito1.agregar_implicacion(self.requisito2)
        self.assertFalse(self.requisito1.es_factible([self.requisito2]))
        self.requisito1.agregar_combinacion(self.requisito2)
        self.assertFalse(self.requisito1.es_factible([self.requisito2, self.requisito1]))
        self.assertTrue(self.requisito1.es_factible([]))
    
    def test_requisito_implicado(self):
        stakeholder1 = Stakeholder(self.STAKEHOLDER_1)
        requisito1 = Requisito("Requisito 1")
        requisito2 = Requisito("Requisito 2")

        requisito1.agregar_stakeholder(stakeholder1)
        requisito2.agregar_stakeholder(stakeholder1)

        requisito1.agregar_implicacion(requisito2)

        solucion = algoritmo_greedy([requisito1, requisito2], 20)

        self.assertNotIn(requisito1, solucion)
        self.assertIn(requisito2, solucion)

    def test_requisito_implica(self):
        stakeholder1 = Stakeholder(self.STAKEHOLDER_1)
        requisito1 = Requisito("Requisito 1")
        requisito2 = Requisito("Requisito 2")

        requisito1.agregar_stakeholder(stakeholder1)
        requisito2.agregar_stakeholder(stakeholder1)

        requisito2.agregar_implicacion(requisito1)

        solucion = algoritmo_greedy([requisito1, requisito2], 20)

        self.assertIn(requisito1, solucion)
        self.assertNotIn(requisito2, solucion)

if __name__ == '__main__':
    unittest.main()