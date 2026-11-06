import unittest
from calculos.emisiones import calcular_emisiones_carbono
class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo_exitoso(self):
        """Verifico valor numerico con un valor valido."""
        #Aca pruebo con 100 kWh * 0.4 de factor debería dar 40.0
        resultado = calcular_emisiones_carbono(100, 0.4)
        self.assertEqual(resultado, 40.0)
    def test_consumo_negativo_genera_error(self):
        """Compruebo que se lance un ValueError si el consumo es negativo."""
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50, 0.4)
if __name__ == '__main__':
    unittest.main()