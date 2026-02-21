import os
os.system('cls')

# ## ***ATIVIDADE 1***

# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
c = 0

while c <= 1001:
    print(c)
    c = c + 1

# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

nome = []
perg = input('quer digitar o nome dos seus amigos?: ')

while perg == 'sim':
     n = input('Digite Nomes: ')
     nome.append(n)
     print(nome)
     perg = input('Deseja continuar?: ')
else:
    print('Obrigado volte sempre')

# ## ***ATIVIDADE 2***

# Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***
emails =  ['santana@gmail.com','valdiney@gmail.com'] 
senhas = ['251','072']


p = input('Deseja acessar o sistema: ')
while p == 'sim':
    
    for chances in range(3):
        senha = input('Digite sua senha: ')
        email = input('Digite seu e-mail: ')
        if senha in senhas and email in emails:
            print('SISTEMA DE NOTAS: ')
            # vai dar continuidade ao sistema
            print('Notas do robson: ')
            notaP = int(input('Digite a nota de portugues: '))
            notaM = int(input('Digite a nota de matematica: '))
            notaH = int(input('Digite a nota de historia: '))
            notaE = int(input('Digite a nota de educação fisica: '))
            notafinal = notaP + notaM + notaH + notaE
            media = notafinal / 4
            print('A media do robson foi de', media)
            break
            #
            #     
        else:
            print('Senha incorreta...') 
            if chances  == 0:
                # print('conta bloqueada')
                p = input('Deseja acessar o sistema: ')   
else:
    print('senha bloqueada')


    
print(input('Digite enter para sair'))

#  **Sistema de notas de alunos**

# - ***Visão do professor***

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média

# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

# ***IMPORTANTE:***

# - Ao finalizar o código, insira na borda do script, no última linha:

# input(’Digite enter para sair’)