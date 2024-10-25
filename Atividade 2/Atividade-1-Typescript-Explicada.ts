// Função para verificar se dois triângulos são semelhantes pelo critério LAL
function ehSemeLAL(
  lados1: number[],
  lados2: number[],
  angulo1: number,
  angulo2: number
): boolean {
  if (lados1.length < 2 || lados2.length < 2) {
    return false;
  }
  const proporcaoLados = lados1[0] / lados2[0] === lados1[1] / lados2[1];
  const angulosCongruentes = angulo1 === angulo2;
  return proporcaoLados && angulosCongruentes;
}

// Função para verificar se dois triângulos são semelhantes pelo critério AA
function ehSemeAA(angulos1: number[], angulos2: number[]): boolean {
  if (angulos1.length < 2 || angulos2.length < 2) {
    return false;
  }
  return angulos1[0] === angulos2[0] && angulos1[1] === angulos2[1];
}

// Função para verificar se dois triângulos são semelhantes pelo critério LLL
function ehSemeLLL(lados1: number[], lados2: number[]): boolean {
  if (lados1.length < 3 || lados2.length < 3) {
    return false;
  }
  return (
    lados1[0] / lados2[0] === lados1[1] / lados2[1] &&
    lados1[1] / lados2[1] === lados1[2] / lados2[2]
  );
}

// Função principal para verificar semelhança
function verificaSemelhanca(): void {
  const lados1 =
    prompt("Informe os lados do primeiro triângulo (separados por espaço):")
      ?.split(" ")
      .map(Number)
      .filter((n) => !isNaN(n)) || [];
  const lados2 =
    prompt("Informe os lados do segundo triângulo (separados por espaço):")
      ?.split(" ")
      .map(Number)
      .filter((n) => !isNaN(n)) || [];
  const angulos1 =
    prompt("Informe os ângulos do primeiro triângulo (separados por espaço):")
      ?.split(" ")
      .map(Number)
      .filter((n) => !isNaN(n)) || [];
  const angulos2 =
    prompt("Informe os ângulos do segundo triângulo (separados por espaço):")
      ?.split(" ")
      .map(Number)
      .filter((n) => !isNaN(n)) || [];

  let algumCriterioValido = false;

  if (
    lados1.length >= 2 &&
    lados2.length >= 2 &&
    angulos1.length >= 1 &&
    angulos2.length >= 1
  ) {
    if (
      ehSemeLAL(
        lados1.slice(0, 2),
        lados2.slice(0, 2),
        angulos1[0],
        angulos2[0]
      )
    ) {
      console.log("Os triângulos são semelhantes pelo critério LAL.");
      algumCriterioValido = true;
    } else {
      console.log("Os triângulos não são semelhantes pelo critério LAL.");
    }
  }

  if (angulos1.length >= 2 && angulos2.length >= 2) {
    if (ehSemeAA(angulos1, angulos2)) {
      console.log("Os triângulos são semelhantes pelo critério AA.");
      algumCriterioValido = true;
    } else {
      console.log("Os triângulos não são semelhantes pelo critério AA.");
    }
  }

  if (lados1.length >= 3 && lados2.length >= 3) {
    if (ehSemeLLL(lados1, lados2)) {
      console.log("Os triângulos são semelhantes pelo critério LLL.");
      algumCriterioValido = true;
    } else {
      console.log("Os triângulos não são semelhantes pelo critério LLL.");
    }
  }

  if (!algumCriterioValido) {
    console.log("Nenhum critério de semelhança foi atendido.");
  }
}

verificaSemelhanca();
