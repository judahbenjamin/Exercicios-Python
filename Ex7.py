#EXERCICIO OPERADORES LÓGICOS
#PROF: MÁRCIO CLAY
# JUDAH BENJAMIN
# DATA: 04/03/2024

# 1. Operador OR

#Verifica se ao menos um dos valores é True

Valor1 = True
Valor2 = False

resultado = Valor1 or Valor2
print("Valor 1 ou Valor 2 =",resultado)

#Verifica se todos os valores são falsos

Valor3 = False
Valor4 = False

resultado = Valor3 or Valor4
print("Valor 3 ou Valor 4 =",resultado)

# 2. Operador AND

#Verifique se todos os valores são True

valor1 = True
valor2 = True

resultado = valor1 and valor2
print("valor1 e valor2 =",resultado)

#Verifique se ao menos um é falso

valor3 = True
valor4 = False 

resultado = valor3 and valor4
print("valor3 e valor4 =",resultado)

# 3. Operador Not

valor5 = True
valor6 = False

#inverte o valor lógico
resultado1 = not valor5
resultado2 = not valor6

print("Not valor 5 =", resultado1)
print("Not valor 6 =", resultado2)