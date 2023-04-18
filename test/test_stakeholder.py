import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from stakeholder import Stakeholder

class TestStakeholder(unittest.TestCase):

    def setUp(self):
        self.stakeholder1 = Stakeholder("Stakeholder 1")
        self.stakeholder2 = Stakeholder("Stakeholder 2")

    def test_agregar_recomendacion(self):
        self.stakeholder1.agregar_recomendacion(self.stakeholder2)
        self.assertEqual(self.stakeholder1.recomendaciones, 1)

    def test_calcular_importancia(self):
        self.stakeholder1.agregar_recomendacion(self.stakeholder2)
        self.stakeholder2.agregar_recomendacion(self.stakeholder1)
        self.assertEqual(self.stakeholder1.calcular_importancia(), 1)
        self.assertEqual(self.stakeholder2.calcular_importancia(), 1)

if __name__ == '__main__':
    unittest.main()
