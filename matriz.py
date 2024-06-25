#ALGORITMO E LÓGICA DE PROGRAMAÇÃO
#DATA: 25/06/2024
#EXERCICIO

from time import sleep

teste_1 = []
teste_2 = []
teste_3 = []
matriz = [teste_1,teste_2,teste_3]
print()
print('               <<<<     MATRIZ 3 X 3     >>>>                  ')
print()
sleep(0.4)
print('=-'*30)
pergunta_1 = input('Deseja iniciar o programa? (S/N) ')

if pergunta_1 in 'Ss':
    # print('OK')
    cont1 = 0
    quant_num = 3
    
    while cont1 < quant_num:
        sleep(0.2)
        num = int(input('NÚMERO: '))
        teste_1.append(num)
        cont1 += 1
        
    print(f'Primeiro vetor adicionado: {matriz}',flush=True)
    print()
    pergunta_2 = input('Deseja continuar? (S/N) ')
    
    if pergunta_2 in 'Ss':
        cont2 = 0
        quant_num = 3
        while cont2 < quant_num:
            sleep(0.2)
            num = int(input('NÚMERO: '))
            teste_2.append(num)
            cont2 += 1
            
        print(f'Segundo vetor adicionado: {matriz}',flush=True)
        print()
        pergunta_3 = input('Deseja continuar mais uma vez? (S/N) ')
        
        if pergunta_3 in 'Ss':
            cont3 = 0
            quant_num = 3
            
            while cont3 < quant_num:
                sleep(0.2)
                num = int(input('NÚMERO: '))
                teste_3.append(num)
                cont3 += 1
            
            print(f'Terceiro vetor adicionado: {matriz}',flush=True)
            print('=-'*30)
            print()
            print('APRESENTAÇÃO DA MATRIZ')
            
            for linha in matriz:
                print(linha)
                
            with open('matriz.txt','a') as arquivo:
                arquivo.write(f'{matriz}')
                
        else:
            print(f'Matriz incompleta: {matriz}')
            
    else:
        print('Fim')
    
else:
    print('FIM DO PROGRAMA!')

