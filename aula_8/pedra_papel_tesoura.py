import os
os.system('cls')

import random

numero_aleatorio = random.randint(1,10)
print(numero_aleatorio)

print('Pedra, Papel Tesoura')

lista_maquina = ['🪨', '🧻', '✂️']

chute_maquina = random.choice(lista_maquina)

minha_lista = ['🪨', '🧻', '✂️']

print('Escolha seu icone')
print(' 0 - 🪨 | 1 - 🧻 | 2- ✂️\n')

meu_chute = int(input('Escolha pelo indice: '))



if chute_maquina == minha_lista[meu_chute]:
    print('Escolha da maquina - ', chute_maquina)
    print('Minha escolha - ', minha_lista[meu_chute])
    print()
    print('EMPATE')
if chute_maquina == '🪨' and minha_lista[meu_chute] == '✂️':
    print('Escolha da maquina - ', chute_maquina)
    print('Minha escolha - ', minha_lista[meu_chute])
    print()
    print('Vitoria da maquina')
if chute_maquina == '🧻' and minha_lista[meu_chute] == '🪨':
    print('Escolha da maquina - ', chute_maquina)
    print('Minha escolha - ', minha_lista[meu_chute])
    print()
    print('Vitoria da maquina')
if chute_maquina == '✂️' and minha_lista[meu_chute] == '🧻':
    print('Escolha da maquina - ', chute_maquina)
    print('Minha escolha - ', minha_lista[meu_chute])
    print()
    print('Vitoria da maquina')

print()

if minha_lista[meu_chute] == '🪨' and chute_maquina ==  '✂️':
    print('Minha escolha - ', minha_lista[meu_chute])
    print('Escolha da maquina - ', chute_maquina)
    print()
    print('Vitoria do Jogador')
if minha_lista[meu_chute] == '🧻' and chute_maquina ==  '🪨':
    print('Minha escolha - ', minha_lista[meu_chute])
    print('Escolha da maquina - ', chute_maquina)
    print()
    print('Vitoria do Jogador')
if minha_lista[meu_chute] == '✂️' and chute_maquina ==  '🧻':
    print('Minha escolha - ', minha_lista[meu_chute])
    print('Escolha da maquina - ', chute_maquina)
    print()
    print('Vitoria do Jogador')