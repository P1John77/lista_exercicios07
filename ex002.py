import time

def gerar_tabuada():
    while True:
        try:
            numero = int(input('Digite um numero para gerar a tabuada:'))
            break
        except ValueError:
            print('numero invalido! digite um numero inteiro para gerar a tabuada.')

    print(f'\ntabuada do {numero} :')
    print('-' * 20)

    for i in range (1, 11):
        resultado = numero * i 
        print(f'{numero} x {i} = {resultado}')
        time.sleep(1)
    
    
    print('-' * 20)     

gerar_tabuada()   






