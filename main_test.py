# Testes parametrizados corrigidos
import pytest
import builtins
from main import q1,q2,q3,q4

@pytest.mark.parametrize("idades, esperado", [
    ({"João Pessoa": 432, "Campina Grande": 325, "Santa Rita": 68, "Patos": 289}, ["João Pessoa", "Campina Grande", "Patos"]),
    ({"Bayeux": 54, "Sousa": 178, "Cajazeiras": 201, "Cabedelo": 45}, ["Sousa", "Cajazeiras"]),
    ({"Guarabira": 122, "Areia": 177}, ["Guarabira", "Areia"]),
    ({"CidadeA": 80, "CidadeB": 110, "CidadeC": 90}, ["CidadeB"]),
    ({"CidadeX": 150, "CidadeY": 80, "CidadeZ": 200}, ["CidadeX", "CidadeZ"]),
])

def test_q1(idades, esperado):
    resultado = q1(idades)
    assert resultado == esperado

@pytest.mark.parametrize("lista1, lista2, soma_esperada, resultado_esperado", [
    ([3, -5, 12, 0, -8, 7], [-2, 10, -1, 6, -4, 9], 47, [3, 6, 7, 9, 10, 12]),
    ([2, 4, 6, 8, 10], [-1, -3, -5, -7, -9], 30, [2, 4, 6, 8, 10]),
    ([-1, -2, -3], [-4, -5, -6], 0, []),
])
def test_q2(lista1, lista2, soma_esperada, resultado_esperado):
    soma, resultado = q2(lista1, lista2)
    assert soma == soma_esperada
    assert resultado == resultado_esperado



