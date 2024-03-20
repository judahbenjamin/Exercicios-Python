#CENTRO ESTADUAL DE EDUCACAO TÉCNICA VASCO COUTINHO
#PROVA DE LÓGICA E ALGORITMO DE PROGRAMAÇÃO
#PROFESSOR: MÁRCIO CLAY
#ALUNO: JUDAH BENJAMIN MUNIR MATOS OLIVEIRA
#DATA: 12/03/2024
#CURSO: TÉCNICO EM INFORMÁTICA
#MÓDULO 1
#TURNO: MATUTINO

"""
1.	 Formatar uma string com f-string:
	Crie uma variável com o nome de uma pessoa.
	Crie uma variável com a idade da pessoa.
	Formate uma string usando f-string para exibir o nome e a idade da pessoa.
	Exiba a string formatada na tela.
"""

nome_pessoa = "Judah"
idade_pessoa = 18

mensagem = (f"Seu nome e {nome_pessoa} e sua idade e {idade_pessoa}")
print(mensagem)

"""
 2.	Explique o que é uma variável e qual sua função em um programa.    
"""

#R: Variável é quando guardamos um valor em algum espaço de memória do computador e utilizamos ela para algo.
#Basicamente é como fosse uma "caixa" para guardar uma informação.

"""
3.	Marque abaixo os itens que representam declaração de variável em Python.  
(  ) String nome= “Pedro”
(X) nome= “Pedro”
(X) numero = 10
(X) _numero= 10.5
(  )  print = “Olavo”    
"""

"""
 4.	Dê exemplo dos tipos de dados em Python abaixo:
- Lógico ----> valor = True, resultado = False
- Aritmético ----> multiplicacao = 20 * 20, divisao = 10 / 2
- Textual ----> nome_pessoa = "Carlos", comida = "Lasanha"
"""

"""
5.	Faça um Programa que peça dois números e imprima a soma.
"""

#Numero1 = int(input("Digite o primeiro numero:"))
#Numero2 = int(input("Digite o segundo numero:"))

#Soma = Numero1 + Numero2

#print(f"A soma dos dois numeros sera {Soma}")

"""
6.Crie um algoritmo que verifique se um número digitado pelo usuário é maior ou menor que 10     
"""

#Numero = int(input("Digite um Numero:"))

#if Numero > 10:
    #print("O Numero e maior que 10")
#else:
    #print("O Numero e menor que 10")
    
"""
7.	Crie um algoritmo que verifique se um numero é lido é par e maior que 10. 
Condições:
- Deve ser usado o operador: “and”.
- Utilize f’string para formatar a saída de dados.   
"""

number = int(input("Digite um numero:"))

if number % 2 == 0 and number >  10 :
    print(f"O numero e PAR e maior que 10.")
else:
    print(f"O numero e IMPAR e menor que 10.")