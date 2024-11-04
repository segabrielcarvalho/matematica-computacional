def analisar_idades():
    try:
        idade_m1 = int(input("\n	Informe a idade do primeiro homem: "))
        idade_m2 = int(input("\n	Informe a idade do segundo homem: "))
        idade_f1 = int(input("\n	Informe a idade da primeira mulher: "))
        idade_f2 = int(input("\n	Informe a idade da segunda mulher: "))
        
        if any(idade <= 0 for idade in [idade_m1, idade_m2, idade_f1, idade_f2]):
            print("\n	Erro: Todas as idades devem ser maiores que zero.")
            return

        mais_velho = max(idade_m1, idade_m2)
        mais_novo = min(idade_m1, idade_m2)
        mais_velha = max(idade_f1, idade_f2)
        mais_nova = min(idade_f1, idade_f2)

        resultado_soma = mais_velho + mais_nova
        resultado_produto = mais_novo * mais_velha

        print(f"\n	Resultado da soma do homem mais velho com a mulher mais nova: {resultado_soma}")
        print(f"\n	Resultado do produto do homem mais novo com a mulher mais velha: {resultado_produto}")

    except ValueError:
        print("\n	Erro: Por favor, insira valores numéricos inteiros válidos.")

analisar_idades()
