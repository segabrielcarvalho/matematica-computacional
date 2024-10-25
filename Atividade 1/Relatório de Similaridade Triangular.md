# Relatório: Implementação de Semelhança de Triângulos em Python

## Introdução

Este relatório descreve a implementação de um programa em Python que verifica a semelhança entre dois triângulos com base nos critérios: **LAL (Lado-Ângulo-Lado)**, **AA (Ângulo-Ângulo)** e **LLL (Lado-Lado-Lado)**. O objetivo é aplicar conceitos de geometria e programação para determinar se dois triângulos são semelhantes.

## Critérios de Semelhança

- **LAL**: Dois lados proporcionales e ângulo entre eles congruente.
- **AA**: Dois ângulos congruentes.
- **LLL**: Todos os três lados proporcionais.

## Implementação do Código em Python

O programa recebe os valores dos lados e ângulos de dois triângulos e verifica a semelhança com base nos critérios mencionados. Exemplo do código:

```python
# Função para verificar semelhança pelo critério LAL
def eh_semeLAL(lados1, lados2, angulo1, angulo2):
    proporcao_lados = (lados1[0] / lados2[0]) == (lados1[1] / lados2[1])
    angulos_congruentes = angulo1 == angulo2
    return proporcao_lados and angulos_congruentes

# Função para verificar semelhança pelo critério AA
def eh_semeAA(angulos1, angulos2):
    return angulos1[0] == angulos2[0] and angulos1[1] == angulos2[1]

# Função para verificar semelhança pelo critério LLL
def eh_semeLLL(lados1, lados2):
    return (lados1[0] / lados2[0] == lados1[1] / lados2[1] == lados1[2] / lados2[2])

# Função principal para verificar semelhança
def verifica_semelhanca():
    tipo = input("Informe o tipo de critério de semelhança (LAL, AA, LLL): ").strip().upper()

    if tipo == "LAL":
        lados1 = list(map(float, input("Informe os dois lados do primeiro triângulo: ").split()))
        lados2 = list(map(float, input("Informe os dois lados do segundo triângulo: ").split()))
        angulo1 = float(input("Informe o ângulo do primeiro triângulo: "))
        angulo2 = float(input("Informe o ângulo do segundo triângulo: "))
        if eh_semeLAL(lados1, lados2, angulo1, angulo2):
            print("Os triângulos são semelhantes pelo critério LAL.")
        else:
            print("Os triângulos não são semelhantes pelo critério LAL.")

    elif tipo == "AA":
        angulos1 = list(map(float, input("Informe dois ângulos do primeiro triângulo: ").split()))
        angulos2 = list(map(float, input("Informe dois ângulos do segundo triângulo: ").split()))
        if eh_semeAA(angulos1, angulos2):
            print("Os triângulos são semelhantes pelo critério AA.")
        else:
            print("Os triângulos não são semelhantes pelo critério AA.")

    elif tipo == "LLL":
        lados1 = list(map(float, input("Informe os três lados do primeiro triângulo: ").split()))
        lados2 = list(map(float, input("Informe os três lados do segundo triângulo: ").split()))
        if eh_semeLLL(lados1, lados2):
            print("Os triângulos são semelhantes pelo critério LLL.")
        else:
            print("Os triângulos não são semelhantes pelo critério LLL.")

    else:
        print("Critério inválido. Por favor, informe LAL, AA ou LLL.")

# Chamada da função principal
verifica_semelhanca()
```

## Explicação do Algoritmo

1. **Entrada de Dados**: Solicita ao usuário os valores dos lados e ângulos dos triângulos.
2. **Verificação dos Critérios**: Verifica os critérios LAL, AA ou LLL usando funções específicas.
3. **Resultado**: Informa se os triângulos são semelhantes com base no critério escolhido.

## Representação no GeoGebra

1. **Construção dos Triângulos**: Criar segmentos e pontos no GeoGebra.
2. **Medidas dos Ângulos e Lados**: Medir ângulos e lados para justificar a semelhança.
3. **Captura de Tela**: Capturar a construção para justificar visualmente a semelhança.

## Conclusão

Este exercício aplicou conceitos de geometria e programação para verificar a semelhança de triângulos. A implementação dos critérios de semelhança e a representação visual no GeoGebra ajudaram a validar a lógica dos algoritmos e visualizar os conceitos teóricos.
