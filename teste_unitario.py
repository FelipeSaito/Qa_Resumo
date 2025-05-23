# Testes unitários são utilizados para verificar se pequenas partes do código, chamadas de unidades, funcionam como esperado. Esse tipo de teste ajuda a identificar erros rapidamente,
# garantindo que funções ou métodos produzam os resultados corretos. O framework unittest do Python facilita a criação desses testes, automatizando as verificações e exibindo os
# resultados.

import unittest

# Função que será testada
def multiplicar(a, b):
    return a * b

# Classe de teste
class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(4, 5), 20)

    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-2, -3), 6)

    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(10, 0), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
