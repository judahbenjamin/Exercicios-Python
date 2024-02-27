#EXERCICIOS PYTHON CEET
#PROF MARCIO CLAY
#ALUNO: JUDAH BENJAMIN
#DATA: 26/02/2024

"""1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
"""
print("Ola, Mundo!")

"""
    2 - Faça um Programa que leia um número digitado e então mostre a mensagem O número 
    informado foi [número].
"""

#numero = int(input("Digite um numero:"))
#print("O numero informado foi:", numero)

"""
    3 - Faça um Programa que peça dois números e imprima a soma.
"""

N1 = 20
N2 = 15
Soma = N1 + N2
print(Soma)

"""4 - Faça um Programa que peça as 2 notas bimestrais e mostre a média.
"""

#nota1 = float(input("Informe a primeria nota do bimestre:"))
#nota2 = float(input("Informe a segunda nota do bimestre:"))

#media = (nota1 + nota2)/2

#print("A media foi:",media)

"""5 - Crie um algoritmo com as seguintes instruções: A) Declarar uma variável string, uma variável 
float e uma variável tipo inteiro. B) Imprimir na tela o valor da variável e seu tipo(type).
"""

nome = "Marcos"
nota = 9.5
idade = 20

print("valor:",nome, "Tipo:",type(nome))
print("valor:",nota, "Tipo:",type(nota))
print("valor:",idade, "Tipo:",type(idade))

"""6 - Crie uma calculadora que multiplique um valor lido e dê o resultado de toda tabuada.
    Exemplo Valor lido =3, Impressão na tela: 3x1 = , 3x2=, 3x3=, 3x4= até o 3x10=. 
"""

#tabuada = int(input("Tabuada do numero: "))

#for count in range(10) :
    #print("%d * %d = %d" % (tabuada, count+1, tabuada*(count+1)))
    
"""7 - Calculadora Básica:
 Leia dois números (a e b)
 Exiba a soma (a + b)
 Exiba a diferença (a - b)
 Exiba o produto (a * b)
 Exiba a divisão (a / b)
 Exiba o quociente (a // b)
 Exiba o resto (a % b)
 Exiba o resultado do expoente (a ** b)
"""
print("///////// CALCULADORA BASICA //////////")
numb1 = 12
numb2 = 2

print("Os dois numeros:", numb1,"e",numb2)
soma = numb1 + numb2
print("Soma:",soma)

subtracao = numb1 - numb2
print("Diferenca:",subtracao)

multiplicacao = numb1 * numb2
print("Multiplicacao:",multiplicacao)

divisao = numb1 / numb2
print("Divisao:", divisao)

quociente = numb1 // numb2
print("Quociente:", quociente)

resto = numb1 % numb2
print("Resto:", resto)

resultado_expoente = numb1 ** numb2
print("Resultado do expoente:", resultado_expoente)

"""8 - Crie um questionário:
     Leia, nome, telefone, email, data nascimento.
     Imprima na tela
 """
 
print("////////// QUESTIONÁRIO ///////////")

Nome = input("Digite seu nome:")
Telefone = input("Digite seu telefone:")
Email = input("Digite seu e-mail:")
DataNasc = input("Digite sua data de nascimento:")

print("//// SEUS DADOS ////")

print(Nome)
print(Telefone)
print(Email)
print(DataNasc)