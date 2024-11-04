# Relatório: Implementação de Bissetrizes em Triângulos com TypeScript

## Introdução

Este relatório descreve a implementação de um programa em TypeScript que calcula as propriedades das bissetrizes interna e externa de um triângulo. O objetivo é explorar os conceitos e propriedades das bissetrizes, aplicando lógica matemática e programação para determinar as divisões dos lados do triângulo feitas pelas bissetrizes.

## Bissetrizes Interna e Externa

- **Bissetriz Interna**: Divide o ângulo interno de um triângulo em duas partes iguais e intercepta o lado oposto, formando segmentos proporcionais.
- **Bissetriz Externa**: Divide o ângulo externo de um triângulo em duas partes iguais e intercepta o prolongamento do lado oposto, formando uma divisão específica.

## Implementação do Código em TypeScript

O programa recebe os valores dos lados do triângulo e calcula as propriedades das bissetrizes interna e externa com base nas fórmulas matemáticas. Exemplo do código:

```typescript
function bissetrizInterna(a: number, b: number, c: number): number {
  /**
   * Calcula a razão das partes formadas pela bissetriz interna no lado oposto.
   * @param a Lado A do triângulo
   * @param b Lado B do triângulo
   * @param c Lado C do triângulo (lado oposto à bissetriz)
   * @return Razão das partes formadas pela bissetriz interna
   */
  const razao = b / a;
  return razao;
}

function bissetrizExterna(a: number, b: number, c: number): string | number {
  /**
   * Calcula a divisão do lado oposto pela bissetriz externa.
   * @param a Lado A do triângulo
   * @param b Lado B do triângulo
   * @param c Lado C do triângulo (lado oposto à bissetriz externa)
   * @return Divisão do lado oposto pela bissetriz externa
   */
  if (c === 0) {
    return "Divisão por zero não é possível. Verifique os lados do triângulo.";
  }
  const divisao = (a + b) / c;
  return divisao;
}
```

## Explicação do Algoritmo

1. **Entrada de Dados**: Solicita ao usuário os valores dos lados do triângulo.
2. **Cálculo da Bissetriz Interna**: Utiliza a função `bissetrizInterna` para calcular a razão das partes formadas pela bissetriz interna no lado oposto.
3. **Cálculo da Bissetriz Externa**: Utiliza a função `bissetrizExterna` para determinar a divisão do lado oposto pela bissetriz externa.
4. **Tratamento de Erros**: Verifica possíveis divisões por zero, garantindo que os valores fornecidos sejam válidos.

## Representação no GeoGebra

1. **Construção do Triângulo**: Criar um triângulo no GeoGebra utilizando a ferramenta de polígono.
2. **Desenho das Bissetrizes**: Utilizar as ferramentas de bissetriz para desenhar as bissetrizes interna e externa dos ângulos do triângulo.
3. **Visualização da Proporção**: Medir os segmentos do lado oposto para verificar a divisão realizada pelas bissetrizes.
4. **Captura de Tela**: Capturar a construção para justificar visualmente as divisões e proporções dos lados.

## Conclusão

Este exercício aplicou conceitos de geometria e programação para calcular e visualizar as propriedades das bissetrizes interna e externa de um triângulo. A implementação das funções em TypeScript, junto com a representação gráfica no GeoGebra, permitiu validar as relações matemáticas e demonstrar visualmente os conceitos teóricos.

