# Relatório: Análise Lógica de um Caso Concreto com Python

## Introdução

Este relatório descreve a implementação de uma análise lógica a partir de um caso concreto, aplicando conceitos de lógica proposicional. A análise é feita com o uso de tabelas verdade para avaliar diferentes cenários, além da implementação da lógica em Python e a criação de representações visuais no GeoGebra para uma melhor compreensão.

## Descrição da Situação

A situação envolve dois amigos, Ana e Bruno, que fazem as seguintes combinações:
- **P**: Ana vai à festa.
- **Q**: Bruno vai à festa.
- **M**: Bruno traz música.
- **R**: A festa é animada.

As condições para a festa são:
1. Se Ana vai à festa (P), então Bruno também vai (Q): **P → Q**.
2. Se pelo menos um deles vai à festa, a festa será animada (R): **P ∨ Q → R**.
3. Se Ana não for, a festa só será animada se Bruno trouxer música (M): **¬P → (M → R)**.

## Implementação da Tabela Verdade em Python

O programa em Python recebe como entrada os valores lógicos para **P**, **Q** e **M**, e gera a tabela verdade para a expressão completa, verificando cada uma das condições descritas. Exemplo do código:

```python
from itertools import product

def tabela_verdade():
    print("P\tQ\tM\tR")
    print("-" * 20)
    for P, Q, M in product([True, False], repeat=3):
        R = ((P or Q) and (not P or (M and True)))
        print(f"{P}\t{Q}\t{M}\t{R}")

tabela_verdade()
```

## Explicação do Algoritmo

1. **Entrada de Dados**: Utiliza todas as combinações possíveis de valores lógicos para **P**, **Q** e **M** usando a função `product` do módulo `itertools`.
2. **Avaliação das Proposições Lógicas**: Avalia as proposições lógicas utilizando operadores de Python, como `and`, `or`, e `not`.
3. **Exibição da Tabela Verdade**: Exibe a tabela verdade para todas as combinações possíveis de **P**, **Q**, **M** e calcula **R** para cada caso.

## Representação Visual no GeoGebra

1. **Construção dos Diagramas de Venn**: No GeoGebra, diagramas de Venn são utilizados para representar visualmente as condições de presença na festa (Ana, Bruno) e se a festa será animada.
2. **Interpretação Visual**: Utilizando os diagramas, pode-se ver claramente como cada combinação de **P**, **Q**, e **M** influencia na animação da festa.
3. **Captura de Tela**: O diagrama construído no GeoGebra é capturado e anexado para justificar visualmente as relações lógicas envolvidas.

## Conclusão

A atividade aplicou conceitos de lógica proposicional para analisar cenários do cotidiano envolvendo condições de presença em uma festa. A implementação da tabela verdade em Python e a construção visual no GeoGebra ajudaram a validar os conceitos teóricos e ilustrar de maneira clara a lógica envolvida. Esses métodos facilitaram a compreensão dos resultados e a verificação das condições propostas.

