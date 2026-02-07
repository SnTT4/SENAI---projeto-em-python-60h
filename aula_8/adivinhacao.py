import random


aleatorio = random.randint(1, 10)
chute = int(input('Chute um numero: '))


if aleatorio == chute:
    print('Acertei em cheio')
    print('O numero é ', aleatorio)
else:
    print('Errou feio')
    print('O numero e ', aleatorio)