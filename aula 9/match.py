#1 Impar ou par

i = int(input('Digite um numero: '))

match i:
    case x if i % 2 == 0:
        print('Par')
    case _:
        print('Impar')

#2 Positivo, negativo ou zero

a = int(input('Digite um numero: '))

match a:
    case x if a > 0:
        print('Este numero e positivo')
    case x if a < 0:
        print('Este numero e negativo')
    case x if a == 0:
        print('Este numero e zero')

#3 String vazia ou não

s = input('Digite uma frase: ')

match s:
    case x if 'Ola' in s:
        print('Palavra Ola Encontrada')
    case x if 'Tudo' not in s:
        print('Palavra Tudo nao esta na frase')
    case _:
        print('Tente novamente')

#4 Maior, menor ou igual a 10

p = int(input('Digite um numero: '))

match p:
    case o if p > 10:
        print('Este numero e maior que 10')
    case o if p < 10:
        print('Este numero e menor que 10')
    case o if p == 10:
        print('Este numero e igual a 10')

#5 Classificando uma idade em faixa etarias

c = int(input('Digite sua idade: '))

match c:
     case u if c <= 12:
        print('Sua faixa etaria e criança(12)')
     case u if c <= 17:
        print('Sua faixa etaria e adolescente(17)')
     case u if c <= 35:
        print('Sua faixa etaria e jovem(35)')
     case u if c > 35:
        print('Sua faixa etaria e adulto(35+)')
     case u if c > 65:
        print('Sua faixa etaria e idoso(65)')

