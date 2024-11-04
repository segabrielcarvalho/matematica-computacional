def calcular_pagamento_total():
    vendedor_nome = input("\n	Informe o nome do funcionário: ")
    vendedor_codigo = input("\n	Informe o código do funcionário: ")
    
    try:
        base_salario = float(input("\n	Informe o salário base (em R$): "))
        valor_por_veiculo = float(input("\n	Informe a comissão por veículo vendido (em R$): "))
        qtd_veiculos_vendidos = int(input("\n	Informe a quantidade de veículos vendidos: "))
        vendas_totais_valor = float(input("\n	Informe o valor total das vendas (em R$): "))
    except ValueError:
        print("\n	Erro: Por favor, insira valores numéricos válidos.")
        return

    pagamento_total = base_salario

    if qtd_veiculos_vendidos > 0:
        pagamento_total += valor_por_veiculo * qtd_veiculos_vendidos
        pagamento_total += 0.05 * vendas_totais_valor

        if qtd_veiculos_vendidos > 10:
            pagamento_total += 0.10 * vendas_totais_valor
    else:
        print("\n	Nenhum veículo foi vendido, pagamento será apenas o salário base.")

    print("\n	--- Informações do Funcionário ---")
    print(f"\n	Nome: {vendedor_nome}")
    print(f"\n	Código: {vendedor_codigo}")
    print(f"\n	Pagamento Total: R$ {pagamento_total:.2f}")

calcular_pagamento_total()