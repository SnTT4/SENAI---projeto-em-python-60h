# variáveis locais, globais e parâmetros

# ***1*** 

# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

def soma(n1, n2):
    p1 = 'par' if n1 % 2 == 0 else 'impar'
    p2 = 'par' if n2 % 2 == 0 else 'impar'
    return(f'{n1} é {p1} e {n2} e {p2}')
print(soma(10, 5))




# ***2***

# ***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

def mult(m1, m2, m3):
    i1 = m1 * 2 
    i2 = m2 * 3
    i3 = m3 * 4
    return(f'{m1} x 2 = {i1}  |  {m2} x 3 = {i2}  |  {m3} x 4 ={i3}')
print(mult(5, 10, 15))


# ***3***

# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

def ele():
    e1 = int(input('Digite um numero: '))
    e2 = int(input('Digite o numero para elevar ao anterior: '))
    elev = e1 ** e2
    return(f' o numero {e1} elevado ao {e2} o resultado é {elev}')
print(ele())

# ***4***

# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

def idade():
    i = int(input('Digite sua idade: '))
    if i == 18:
        print('você tem 18 anos.')
    else:
        print('Voce nao pode ver a mensagem secreta')
print(idade())
# ***5***

def calcular_idade(ano_atual):
    ano_nascimento = int(input('Digite o ano em que você nasceu: '))
    idade_resultado = ano_atual - ano_nascimento
    
    return idade_resultado
resultado = calcular_idade(2026)

print(f'Em 2026, sua idade será: {resultado} anos.')

# ***6***

# ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***

def copa():
    perg = int(input('qual foi o ultimo ano que o Brasil conquistou o titulo da copa: '))
    if perg == 1999:
        print('O Brasil foi campeão americano em 1999 nos penaltis.')
    else:
        print('Digite outro valor')
print(copa())

# ***7*** 

# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  

# ***1 - Função -  cumprimentar o cliente***

comidas = ['Salada', 'Macarronada', 'Sanduiche', 'Sorvete']

# 1. Defina a função comida primeiro
def comida():
    print(f'Temos: {", ".join(comidas)}')
    p = input('O que gostaria de comer: ')
    print(f'\nVocê escolheu {p} para comer')
    print('Obrigado pela compra, volte sempre!')

# 2. Depois defina a saudação que chama a comida
def saudacao():
    print('Olá cliente, seja bem-vindo.\n')
    try:
        resp = int(input('Gostaria de comer algo? (1 para Sim, 0 para Não): '))
        if resp == 1:
            comida()
        else:
            print('Obrigado, volte sempre!')
    except ValueError:
        print('Erro: Por favor, digite apenas números.')

# chamando a função principal.
saudacao()


# ***3 - Sugestão utilize listas  e loops***