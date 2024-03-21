pergunta = " sim"
while pergunta == " sim":
   num_1 = int(input("Digite o primeiro numero: "))
   num_2 = int(input("Digite o segundo numero: "))
   multiplicacao = num_1 * num_2
   print(f"Resultado {num_1} * {num_2} e = {multiplicacao}")
   pergunta = input("Deseja continuar?")
   if pergunta != " sim": print("Programa encerrado!")