import random

while True:
    entrada = int(input('\nDigite um numero entre 1 e 100 para adivinhar qual numero foi gerado: '))
    sorteio = random.randint(1, 100)

    if entrada > 100:
       print("Por favor esse numero não é válido")
    else:
        if entrada == sorteio:
            print('Parabens, Você acertou! o numero gerado aleatoriamente foi {}.'.format(sorteio))
            break
        else: 
            if entrada > sorteio:
                print('\nvocê errou!! O numero informado é MAIOR do que o numero gerado aleatoriamente. Tente Novamente!')
            else:
                print('\nvocê errou!! O numero informado é MENOR do que o numero gerado aleatoriamente. Tente Novamente!')
        