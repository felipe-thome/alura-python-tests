from codigo.bytebank import Funcionario
from pytest import mark
import pytest


class TestClass:
    # def test_retorno_str(self):
    #     # Given
    #     nome, data_nasc, salario = 'Teste', '12/04/2000', 1000
    #     esperado = 'Funcionario(Teste, 12/04/2000, 1000)'
    #
    #     # When
    #     funcionario_teste = Funcionario(nome, data_nasc, salario)
    #     resultado = funcionario_teste.__str__()
    #
    #     # Then
    #     assert resultado == esperado

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given
        entrada = '13/03/2000'
        esperado = 23

        # When
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        # Then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        # Given
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        # When
        lucas = Funcionario(entrada, '11/11/200', 1111)
        resultado = lucas.sobrenome()

        # Then
        assert resultado == esperado

    def test_quando_decrecimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        # When
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        # Then
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given
        entrada = 1000
        esperado = 100

        # When
        funcionario_teste = Funcionario('Teste', '11/11/200', entrada)
        resultado = funcionario_teste.calcular_bonus()

        # Then
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_mais_de_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # Given
            entrada = 1000000

            # When
            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            # Then
            assert resultado

