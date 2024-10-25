import math

def bissetriz_interna(a, b, c):
    razao = b / a
    return razao

def bissetriz_externa(a, b, c):
    try:
        divisao = (a + b) / c
    except ZeroDivisionError:
        return "Divisão por zero não é possível. Verifique os lados do triângulo."
    return divisao

def main():
    print("Cálculo das propriedades da Bissetriz Interna e Externa de um Triângulo")
    
    a = float(input("Digite o valor do lado A: "))
    b = float(input("Digite o valor do lado B: "))
    c = float(input("Digite o valor do lado C (lado oposto à bissetriz): "))

    razao_interna = bissetriz_interna(a, b, c)
    print(f"A razão das partes formadas pela bissetriz interna é: {razao_interna}")
    
    divisao_externa = bissetriz_externa(a, b, c)
    print(f"A divisão do lado oposto pela bissetriz externa é: {divisao_externa}")

if __name__ == "__main__":
    main()
