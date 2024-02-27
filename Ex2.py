#LOGICA E ALGORITMO DE PROGRAMACAO -  AULA 2
#PROF: MARCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 27/02/2024

print("/////////////// OPERADORES ARITMETICOS /////////////////")
n1 = 2
n2 = 10

soma = n1 + n2
print("soma:",soma)

subtracao = n1 - n2
print("subtracao:",subtracao)

multiplicacao = n1 * n2
print("multiplicacao:", multiplicacao)

divisao = n1 / n2
print("divisao:",divisao)

quociente = n1 // n2
print("quociente:",quociente)

resto = n1 % n2
print("resto:",resto)

exponenciacao = n1 ** n2
print("exponenciacao:",exponenciacao)

print("/////////////// OPERADORES RELACIONAIS ///////////////")
valor1 = 5
valor2 = 5
resultado = valor1 == valor2 #IGUAL A - verifica se dois valores são iguais.
print(resultado)

valor1 = 5
valor2 = 5
resultado = valor1 != valor2 #DIFERENTE DE - verifica se dois valores são diferentes.
print(resultado)

valor1 = 5
valor2 = 5
resultado = valor1 > valor2 #MAIOR QUE - verifica se o primeiro valor é maior que o segundo.
print(resultado)

valor1 = 5
valor2 = 5
resultado = valor1 < valor2 #MENOR QUE - verifica se o primeiro valor é menor que o segundo.
print(resultado)

valor1 = 5
valor2 = 5
resultado = valor1 >= valor2 #MAIOR OU IGUAL A - verifica se o primeiro valor é maior ou igual ao segundo.
print(resultado)

valor1 = 5
valor2 = 5
resultado = valor1 <= valor2 #MENOR OU IGUAL A - verifica se o primeiro valor é menor ou igual ao segundo.
print(resultado)

print("///////////////// OPERADORES LOGICOS /////////////")

#NOT (NÃO)
valor = True

Resultado = not valor #NOT - inverte o valor do operando.
print(Resultado)

#AND (E)

Num1 = 10
Num2 = 5

if Num1 > 10 and Num2 < 5 : #AND - retorna true se ambos os operandos forem true.
    print("Oi")
else :
    print("Outra")
    
    
valA = True
valB = True

resultado = valA and valB
print(resultado)

#OR (OU)

Num1 = 11
Num2 = 5

if Num1 > 10 or Num2 < 5 : #OR - retorna true se pelo menos um dos operandos for true.
    print("Oi")
else :
    print("Outra")
    

valorA = True
valorB = False

resultado = valorA or valorB
print(resultado)

