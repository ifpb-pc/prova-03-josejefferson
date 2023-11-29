# Programação Estruturada: Prova 03

## Instruções

### Execução manual

Para executar o seu programa: Altere o código no arquivo main com a sua solução e execute no terminal o comando a seguir:

```sh
python main.py
```

### Teste com pytest

Para testar o seu programa com pytest: Altere o código no arquivo main com a sua solução e execute no terminal o comando a seguir:

```sh
pytest
```

## Questão 01

A partir do dicionário de nomes e idades de cidades a seguir, crie uma função que retorne uma lista de cidades maiores que 100 anos.

### Exemplo:

Entrada:

```py
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
```

Saída:

resultado_esperado = ['João Pessoa', 'Campina Grande', 'Patos', 'Sousa', 'Cajazeiras', 'Guarabira', 'Areia']


## Questão 02

Crie um programa que leia duas listas (lista1 e lista2), retorne uma tupla contendo: 

- A soma de todos os números das duas listas maiores que 0,

- Uma lista  em ordem crescente dos elementos da lista1 e lista2 maiores que 0.

### Exemplos

Entrada:

- lista1 = [3, -5, 12, 0, -8, 7]
- lista2 = [-2, 10, -1, 6, -4, 9]

Saída:

- resultado_esperado - 47, [3, 6, 7, 9, 10, 12]

Entrada:

- lista1 = [2, 4, 6, 8, 10]

- lista2 = [-1, -3, -5, -7, -9]

Saída

- resultado_esperado = 30, [2, 4, 6, 8, 10]

## Questão 03:

Você deverá ler valores numéricos até o usuário digitar 0. Crie uma função ler_valores() para retornar os valores deverão ser passados para uma função processa_lista(lista) que irá retornar 2 listas, uma lista para valores pares e uma lista para ímpares.

### Exemplos

- Entrada: [2, 4, 6, 8, 10, 12, 14, 0]

- Saída Esperada:

  - Lista de Pares: [12, 14, 6, 8, 10]
  - Lista de Ímpares: []

- Entrada: [1, 3, 5, 7, 9, 11, 0]
- Saída Esperada:

  - Lista de Pares: []
  - Lista de Ímpares: [11, 9, 7, 5, 3]

- Entrada: [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11, 0]
- Saída Esperada:
  - Lista de Pares: [12, 4, 6, 8, 10]
  - Lista de Ímpares: [11, 3, 5, 7, 9]

## Questão 04

Joaquina é uma fotógrafa muito peculiar. Ela só aceita tirar fotos de pessoas se as pessoas estiverem em grupos de exatamente 03 pessoas. Tudo isso porque Joaquina tem uma mania esquisita de ordenação. Para ela, a pessoa mais baixa deve ficar sempre do lado direito, a segunda mais baixa do lado esquerdo, no meio, fica a terceira pessoa.

Você deverá ler valores numéricos referente à altura em uma função ler_03_alturas() que deve retornar a lista de alturas. Em seguida, os valores deverão ser passados para uma função organizar_alturas(lista) que irá organizar a lista de altuas conforme a proposta de Joaquina. Ao final, crie uma função para formatar as alturas da lista de Joaquina, onde cada valor fique com duas casas decimais após a vírgula e retorne esta lista formatada.

### Exemplos

- Entrada

  A entrada consiste de 03 números reais maiores que zero correspondendo às alturas de 03 pessoas. Cada número é dado em uma linha diferente. A entrada pode não estar ordenada.
  [30, 20, 10]

- Saída

  Consiste de 03 números reais, separados por um final de linha. Os números devem ser formatados com 02 casas decimais.

  [20.00, 30.00, 10.00]
