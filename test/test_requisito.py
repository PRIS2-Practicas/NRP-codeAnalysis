import unittest
from requisito import Requisito
from stakeholder import Stakeholder

class TestRequisito(unittest.TestCase):

    def setUp(self):
        self.requisito1 = Requisito("Requisito 1")
        self.requisito2 = Requisito("Requisito 2")
        self.stakeholder1 = Stakeholder("Stakeholder 1")
        self.stakeholder2 = Stakeholder("Stakeholder 2")

    def test_agregar_exclusion(self):
        self.requisito1.agregar_exclusion(self.requisito2)
        self.assertIn(self.requisito2, self.requisito1.exclusiones)
        self.assertIn(self.requisito1, self.requisito2.exclusiones)

    def test_agregar_implicacion(self):
        self.requisito1.agregar_implicacion(self.requisito2)
        self.assertIn(self.requisito2, self.requisito1.implicaciones)

    def test_agregar_combinacion(self):
        self.requisito1.agregar_combinacion(self.requisito2)
        self.assertIn(self.requisito2, self.requisito1.combinaciones)
        self.assertIn(self.requisito1, self.requisito2.combinaciones)

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

if __name__ == '__main__':
    unittest.main()