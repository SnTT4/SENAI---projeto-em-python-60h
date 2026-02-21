

# - 3 chances de acessar o sistema


emails =  ['bea@gmail.com','Carlos@gmail.com'] 
senhas = ['123','456']


p = input('Deseja acessar o sistema: ')
while p == 'sim':
    
    for chances in range(3):
        senha = input('Digite sua senha: ')
        email = input('Digite seu e-mail: ')
        if senha in senhas and email in emails:
            print('SISTEMA DE NOTAS: ')
            # vai dar continuidade ao sistema
            #
            #
            #
            # 


            
        else:
            print('Senha incorreta...') 
            if chances  == 0:
                # print('conta bloqueada')
                p = input('Deseja acessar o sistema: ')   


        
        


else:
    print('senha bloqueada')






# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média





# - 3 chances de acessar o sistema






emails =  ['bea@gmail.com','Carlos@gmail.com'] 
senhas = ['123','456']


p = input('Deseja acessar o sistema: ')
while p == 'sim':
    
    for chances in range(3):
        senha = input('Digite sua senha: ')
        email = input('Digite seu e-mail: ')
        cadastrar =  input('Deseja verificar a média? ')
        while cadastrar =='sim':
            if senha in senhas and email in emails:
                print('SISTEMA DE NOTAS: ')
                notas = []
                nomes = []
                nome =  input('Nome Aluno: ')
                n1 =  float(input('Nota 1'))
                n2 =  float(input('Nota 2'))
                n3 =  float(input('Nota 3'))
                notas.extend([n1,n2,n3])
                media  =  sum(notas)/len(notas)
                print('Media do aluno ', nome)
                print(media)
                cadastrar =  input('deseja cadastra um novo aluno? ')
        else:
             print('Até logo')     


       
   
     
  
        
        


else:
    print('senha bloqueada')





input('Digite enter  para sair ... ')






# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média


# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***


# ***IMPORTANTE:***


# - Ao finalizar o código, insira na borda do script, no última linha:


# input(’Digite enter para sair’)


# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***


# ***IMPORTANTE:***


# - Ao finalizar o código, insira na borda do script, no última linha:


# input(’Digite enter para sair’)