# EXERCÍCIOS 1: 
# Utilize condicionais

# Acessar a Aula - 8

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
print('Numero negativo ou positivo')

numero = int(input('Digite um numero: '))
if numero <0:
    print('O Numero e negativo')
elif numero == 0:
    print(' O numero e zero')
else:
    print('Numero e positivo')
print()

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
print('verificar idade')

idade = int(input('Digite sua idade: '))
if idade >=18:
    print('Pode votar') 
else:
    print('Não pode ainda')
print()

# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
print('Impar ou par')

numero = int(input('Digite um numero: '))

if numero % 2 == 0:
    print(f'{numero} e par')
else:
    print(f'{numero} e impar ')
print()


# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
print(' Crie um triangulo ')
medida1 = int(input('Digite a medida 1: '))
medida2 = int(input('Digite a medida 2: '))
medida3 = int(input('Digite a medida 3: '))

if medida1 == medida2 == medida3:
    print('e um trianngulo equilatero.')
elif medida1 == medida2:
    print('Triangulo isosceles')
elif medida3 == medida1:
    print('Triangulo isosceles')
elif medida2 == medida3:
     print('Triangulo isosceles')
else:
    print('Triangulo escaleno')
print()
# 5*

	# Determine se um número é múltiplo de 5 e 7.
print("verifique se o numero e multiplo de 5 e 7\n")
numero = int(input("Digite um numero: "))
if numero % 5 == 0 and numero % 7 == 0:
    print('este numero e multiplo de 5 e 7')
else:
    print('Este numero nao e multiplo')
print()
# 6*

# Verifique se um número é positivo e maior que 10
print('Numero positivo sendo maior que 10\n')
numero = int(input("Digite um numero: "))
if numero >10:
    print('Este numero e positivo')
else:
    print('Este numero e negativo')
print()

# 7*

# Verifique se um número é divisível por 3 ou 5.

print('numero divisivel por 3 ou 5')

numero = int(input('Digite algum numero: '))

if numero %3 == 0 and numero %5 == 0:
    print(f'Este numero: {numero} e divisivel por 3 e 5')
else:
    print(f'Este numero: {numero} nao e divisivel por 3 e 5 ')
