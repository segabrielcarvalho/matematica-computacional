function tabelaVerdade(): void {
  console.log("P\tQ\tM\tR");
  console.log("-".repeat(20));

  const valores = [true, false];

  for (const P of valores) {
    for (const Q of valores) {
      for (const M of valores) {
        // Avaliando as condições lógicas
        const cond1 = !P || Q; // P → Q
        const cond2 = P || Q;  // P ∨ Q
        const cond3 = !P || (M && true); // ¬P → (M → R)
        const R = cond1 && cond2 && cond3;

        // Exibindo a tabela verdade
        console.log(`${P}\t${Q}\t${M}\t${R}`);
      }
    }
  }
}

tabelaVerdade();
