import os
os.system('cls')

# cadastro no e-commerce
dados = {
    'login':[],
    'senha':[],
    'produtos': {
        1:['Computador Dell', 5000.0],
        2:['Fone Apple', 2500.0],
        3:['Mouse Lenovo', 250.0],
        4:['Monitor Lenovo', 3000.0]
                }
}

print('CADASTRE-SE:')
cad_login = input('Cadastre seu login: ')
cad_senha = input('Cadastre sua senha: ')
dados['login'].append(cad_login)
dados['senha'].append(cad_senha)

# acessar o e-commerce
print('ACESSE A APLICAÇÃo: ')

sso_login = input('Digite seu login para continuar: \n')
sso_senha = input('digite sua senha para continuar: ')

if sso_login == dados['login'][0] and sso_senha == dados['senha'][0]:
    print('Seja bem-vindo(A) Ao E-commerce K')
    print("Produtos: ")

    produto = input(f'''
    
    {dados['produtos']} - escolha 1 - 2 - 3 - 4 ->>>

    

    ''')
    carrinho = []
    valores = []

    carrinho.append(dados['produto'][produto][0])
    valores.append(dados['produto'][produto][1])
    print(carrinho[0],valores[0])

    soma = sum(valores)
    print('Valor a pagar - R$', soma)
    pag = input('Selecione sua forma de pagamento: ')
    print('Forma de pagamento', pag)
    print('Obrigado volte sempre\n')


else:
    print('Seu login ou senha esta incorreto\n')
    print('Tente novamente')
# verificar a lista de produtos


# comprar um produto
# paga o produto