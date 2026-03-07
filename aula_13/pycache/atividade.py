#main.py

import os
os.system('cls')

import meu_modulo

#**1 - Crie um número aleatório de 5,10**
# **2 - Crie 3 números aleatórios**
print('Atividade 1 e 2')
aleatorio = meu_modulo.atividade_1(5,10)
print(aleatorio)
print(aleatorio)
print(aleatorio)
print('----' * 20)
# **3 - Crie um número aleatório entre 10 a 30 utilize o range()**
print('Atividade 3')
atividade_3 = meu_modulo.atividade_3(10, 30)
print(atividade_3)
print('----' * 20)
# **4 - Contagem regressiva simples**
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)
print('Atividade 4')
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for lista in range(10, 0, -1):
    print(lista)
print('Fogo!!!')    
print('----' * 20)

# **5 - Soma de números pares**

# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.

# ```python
# # Peça ao usuário que insira um número inteiro 
# # faça o loop com range e for ate´o numero
# # positivo e, em seguida, calcule a soma de 
# # todos os números pares de 2 até o número inserido.
# ```

# (use módulo, if, for)


def somar_pares(limite):
    """
    Calcula a soma de todos os números pares de 2 até o limite inserido.
    """
    soma = 0
    # O loop range(2, limite + 1, 2) começa em 2, vai até o limite+1 (para incluir o número),
    # com passo 2 para pegar apenas pares.
    for i in range(2, limite + 1, 2):
        soma += i
    return soma

# Peça ao usuário que insira um número inteiro positivo
try:
    numero = int(input("Insira um número inteiro positivo: "))
    
    if numero < 2:
        print("A soma de pares até", numero, "é 0 (não há pares entre 2 e", numero, ").")
    else:
        resultado = somar_pares(numero)
        print(f"A soma dos números pares de 2 até {numero} é: {resultado}")

except ValueError:
    print("Por favor, insira um número inteiro válido.")



print('----' * 20)


# **6 - Tabuada de multiplicação**

# ***Utilize print() na saída***

# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.

# (while ou for )
print('Atividade 6')
def atividade_6(n):
    n = int(input('Digite um numero: '))
    lista = [1,2,3,4,5,6,7,8,9,10]
    for i in lista:
        a=n*i
        print(n, 'x', i, '=', a)
print(atividade_6(0))
print('----' * 20)

# **7 -  Números ímpares reversos**

# Exiba uma contagem regressiva de números ímpares de 99 a 1.

# (for) -->
print('Atividade 7')
def atividade_7(num):
    for i in range(101, 1, -2):
        print(i)
print(atividade_7(2))
   