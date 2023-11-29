#################################
##          QUESTÃO 1          ##
#################################

"""
A partir do dicionário de nomes e idades de cidades a seguir, crie uma função que retorne
uma lista de cidades maiores que 100 anos.
"""

def q1(cidades):
    cidades_mais_100_anos = []

    for nome, idade in cidades.items():
        if idade > 100:
            cidades_mais_100_anos.append(nome)

    return cidades_mais_100_anos





#################################
##          QUESTÃO 2          ##
#################################

"""
Crie um programa que leia duas listas (lista1 e lista2), retorne uma tupla contendo:
- A soma de todos os números das duas listas maiores que 0,
- Uma lista em ordem crescente dos elementos da lista1 e lista2 maiores que 0.
"""

def q2(lista1, lista2):
    numeros_maiores_que_0 = []

    for numero in lista1 + lista2:
        if numero > 0:
            numeros_maiores_que_0.append(numero)

    soma = sum(numeros_maiores_que_0)
    numeros_ordenados = sorted(numeros_maiores_que_0)
    return soma, numeros_ordenados





#################################
##          QUESTÃO 3          ##
#################################

"""
Você deverá ler valores numéricos até o usuário digitar 0. Crie uma função ler_valores() para
retornar os valores deverão ser passados para uma função processa_lista(lista) que irá retornar
2 listas, uma lista para valores pares e uma lista para ímpares.
"""

def ler_valores(valores = None):
    if valores:
        return valores[:-1]

    valores = []

    while True:
        valor = int(input("Digite um valor, ou 0 para finalizar: "))
        if valor == 0:
            break
        else:
            valores.append(valor)

    return valores

def processa_lista(valores):
    valores_pares = []
    valores_impares = []

    for valor in valores:
        if valor % 2 == 0:
            valores_pares.append(valor)
        else:
            valores_impares.append(valor)

    return valores_pares, valores_impares


def q3(valores = None):
    valores = ler_valores(valores)
    valores_pares, valores_impares = processa_lista(valores)
    return valores_pares, valores_impares





#################################
##          QUESTÃO 4          ##
#################################

"""
Joaquina é uma fotógrafa muito peculiar. Ela só aceita tirar fotos de pessoas se as pessoas 
estiverem em grupos de exatamente 03 pessoas. Tudo isso porque Joaquina tem uma mania esquisita 
de ordenação. Para ela, a pessoa mais baixa deve ficar sempre do lado direito, a segunda mais 
baixa do lado esquerdo, no meio, fica a terceira pessoa.

Você deverá ler valores numéricos referente à altura em uma função ler_03_alturas() que deve retornar
a lista de alturas. Em seguida, os valores deverão ser passados para uma função organizar_alturas(lista)
que irá organizar a lista de altuas conforme a proposta de Joaquina. Ao final, crie uma função para
formatar as alturas da lista de Joaquina, onde cada valor fique com duas casas decimais após a vírgula
e retorne esta lista formatada.
"""

def ler_03_alturas(alturas = None):
    if alturas:
        return alturas

    alturas = []

    for _ in range(3):
        valor = int(input("Digite um valor, ou 0 para finalizar: "))
        alturas.append(valor)

    return alturas

def organizar_alturas(lista):
    lista_ordenada = sorted(lista)

    pessoa_baixa = lista_ordenada[0]
    pessoa_media = lista_ordenada[1]
    pessoa_alta = lista_ordenada[2]

    return pessoa_media, pessoa_alta, pessoa_baixa

def formatar_alturas(altura):
    return f'{altura:.2f}'

def q4(alturas = None):
    alturas = ler_03_alturas(alturas)
    alturas_org = organizar_alturas(alturas)
    alturas_fmt = list(map(formatar_alturas, alturas_org))
    return alturas_fmt





# Teste as questões que você desenvolveu manualmente:
def main():
    # =============== Questão 1 ===============
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    resultado_esperado = ['João Pessoa', 'Campina Grande', 'Patos', 'Sousa', 'Cajazeiras', 'Guarabira', 'Areia']
    print("q1:", resultado)
    assert resultado == resultado_esperado

    # =============== Questão 2 ===============
    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    resultado_esperado = (47, [3, 6, 7, 9, 10, 12])
    print("q2:", resultado)
    assert resultado == resultado_esperado

    # =============== Questão 3 ===============
    numeros = [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11, 0]
    resultado = q3(numeros)
    resultado_esperado = ([2, 4, 6, 8, 10, 12], [1, 3, 5, 7, 9, 11])
    print("q3:", resultado)
    assert resultado == resultado_esperado

    # =============== Questão 4 ===============
    alturas = [30, 20, 10]
    resultado = q4(alturas)
    resultado_esperado = ["20.00", "30.00", "10.00"]
    print("q4:", resultado)
    assert resultado == resultado_esperado

if __name__ == "__main__":
    main()
