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

function main(): void {
  console.log("Cálculo das propriedades da Bissetriz Interna e Externa de um Triângulo");

  // Entrada dos lados do triângulo
  const a: number = parseFloat(prompt("Digite o valor do lado A: ") || "0");
  const b: number = parseFloat(prompt("Digite o valor do lado B: ") || "0");
  const c: number = parseFloat(prompt("Digite o valor do lado C (lado oposto à bissetriz): ") || "0");

  // Parte A - Bissetriz Interna
  const razaoInterna = bissetrizInterna(a, b, c);
  console.log(`A razão das partes formadas pela bissetriz interna é: ${razaoInterna}`);

  // Parte B - Bissetriz Externa
  const divisaoExterna = bissetrizExterna(a, b, c);
  console.log(`A divisão do lado oposto pela bissetriz externa é: ${divisaoExterna}`);
}

main();
