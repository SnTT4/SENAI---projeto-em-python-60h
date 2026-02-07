import os
os.system('cls')

print('Seja bem vindo a E-Commerce')



ecommerce = {
'livro':25.15,
'tablet':3000.0,
'fone':500.0
}


carrinho = {
'produtos':[],
'valores':[]
}


produto1 = input('produto: ')
produto2 = input('produto: ')



carrinho['produtos'].append(produto1)
carrinho['produtos'].append(produto2)
carrinho['valores'].append(ecommerce[produto1])
carrinho['valores'].append(ecommerce[produto2])


soma =  sum(carrinho['valores'])


print('Total -  R$', soma)


print(carrinho)


formas_pagamento = ['pix', 'Cartão credito', 'Cartão Debito', 'dinheiro']
print('Formas de pagamento:', formas_pagamento)
escolha_forma = input('Digite sua forma de pagamento: ')
indice = formas_pagamento.index(escolha_forma)
print('Sua forma de pagamento escolhida foi:', escolha_forma )
print()
print('Obrigado por comprar a loja')