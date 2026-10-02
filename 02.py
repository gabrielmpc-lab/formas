# Crie um algoritmo que leia 3 valores (lados de um triângulo)
# Determine se formam um triângulo,e se formar verifique 
# Se é um equilatero, escaleno ou isóceles.

lado_1 = float(input("Digite a medida do primeiro lado: "))
lado_2 = float(input("E a medida do segundo lado: "))
lado_3 = float (input("Agora a medida da base: "))

# Determine se formam um triângulo
if (lado_1 + lado_2) > lado_3 and (lado_1 + lado_3) > lado_2 and (lado_2 + lado_3) > lado_1:
    forma = "formam um triângulo"

else: 
    forma = "não formam um triângulo"

# Se é um equilatero, escaleno ou isóceles
if forma == "formam um triângulo":
    if lado_1 == lado_2 and lado_2 == lado_3:
        tipo_do_triangulo = "equilátero"

    if lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
        tipo_do_triangulo = "isósceles"

    if lado_1 != lado_2 and lado_2 != lado_3:
        tipo_do_triangulo = "escaleno"


print (f"As medidas {forma}")
print (f"O seu triângulo é um {tipo_do_triangulo}")