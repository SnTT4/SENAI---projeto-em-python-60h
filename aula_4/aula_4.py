
### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

num = 2
print(num ** 2)
print()
### 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

nome = 'Cauan'
sobrenome = 'Santana'
print(f'meu nome e {nome} e meu sobrenome e {sobrenome}')
print()
### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print()
soma = num1 + num2
print(f'{num1} + {num2} = {soma}')
print()
### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

palavra = 'python'
numero = 10

print(f'{palavra} e nota {numero}')
print()
### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado. 

frase = 'No Brasil e um clima tropical?'
print()
print(f'{frase}')
final = input('De uma resposta a questão acima: ')
print()
print(f'{frase} {final}')

## ATIVIDADES:


### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.


numero =  10
print(numero ** 2)


### 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.


nome, sobrenome =  'Lucas', 'Almeida'


nome = 'Kaue'
sobrenome = 'Santos'


print(nome, sobrenome)


# Concatenações: 
print(nome + ' ' +sobrenome)
print('{} {}'.format(nome, sobrenome))
print('%s %s'%(nome, sobrenome))
print(f'{nome} {sobrenome}')





### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.


n1  =  int(input('numero: '))
n2  =  int(input('numero: '))


print('{} {}'.format(n1, n2))


### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
palavra  =  'Python'
n  =  5
print(palavra, n)


### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.


frase  =  'seja bem vindo(a)'
nome  = input('Digite sue nome:  ')


print(frase, nome)