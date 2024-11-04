def eh_semeLAL(lados1, lados2, angulo1, angulo2):
    if len(lados1) < 2 or len(lados2) < 2:
        return False
    proporcao_lados = (lados1[0] / lados2[0]) == (lados1[1] / lados2[1])
    angulos_congruentes = angulo1 == angulo2
    return proporcao_lados and angulos_congruentes

def eh_semeAA(angulos1, angulos2):
    if len(angulos1) < 2 or len(angulos2) < 2:
        return False
    return angulos1[0] == angulos2[0] and angulos1[1] == angulos2[1]

def eh_semeLLL(lados1, lados2):
    if len(lados1) < 3 or len(lados2) < 3:
        return False
    return (lados1[0] / lados2[0] == lados1[1] / lados2[1] == lados1[2] / lados2[2])

def verifica_semelhanca():
    lados1 = list(map(float, input("Informe os lados do primeiro triângulo (separados por espaço): ").split()))
    lados2 = list(map(float, input("Informe os lados do segundo triângulo (separados por espaço): ").split()))
    angulos1 = list(map(float, input("Informe os ângulos do primeiro triângulo (separados por espaço): ").split()))
    angulos2 = list(map(float, input("Informe os ângulos do segundo triângulo (separados por espaço): ").split()))

    algum_criterio_valido = False

    if len(lados1) >= 2 and len(lados2) >= 2 and len(angulos1) >= 1 and len(angulos2) >= 1:
        if eh_semeLAL(lados1[:2], lados2[:2], angulos1[0], angulos2[0]):
            print("Os triângulos são semelhantes pelo critério LAL.")
            algum_criterio_valido = True
        else:
            print("Os triângulos não são semelhantes pelo critério LAL.")

    if len(angulos1) >= 2 and len(angulos2) >= 2:
        if eh_semeAA(angulos1, angulos2):
            print("Os triângulos são semelhantes pelo critério AA.")
            algum_criterio_valido = True
        else:
            print("Os triângulos não são semelhantes pelo critério AA.")

    if len(lados1) >= 3 and len(lados2) >= 3:
        if eh_semeLLL(lados1, lados2):
            print("Os triângulos são semelhantes pelo critério LLL.")
            algum_criterio_valido = True
        else:
            print("Os triângulos não são semelhantes pelo critério LLL.")

    if not algum_criterio_valido:
        print("Nenhum critério de semelhança foi atendido.")

if __name__ == "__main__":
    verifica_semelhanca()
