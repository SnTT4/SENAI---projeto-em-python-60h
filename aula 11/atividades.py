# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    n = int(input('Digite um numero inteiro: '))
    print('Voce digitou um numero inteiro')
except ValueError:
    print('Digite um valor inteiro')
print()







# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
print('Divisão com Try e Except')
try:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))
    resultado = (n1 / n2)
    print('seu resultado da divisao foi:', resultado)
except ZeroDivisionError:
    print('Ocorreu um erro, tente novamente.')




# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

frutas = ['Maça', 'Banana', 'Uva']
print(frutas)
try:
    print('0 Maça, 1 Banana, 2 - Uva\n')
    escolha = int(input('Digite o numero da fruta: '))
    print(f'Você escolheu {frutas[escolha]}')
except (ValueError, IndexError):
    print('Algo deu errado, tente novamente')

        





