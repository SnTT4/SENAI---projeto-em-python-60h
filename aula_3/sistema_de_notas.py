print('\nSistema de notas')
print('....' * 8 )

nome_aluno = input('Nome do aluno: ')

n1_port = float(input('\nNota de portugues: '))
n2_mat = float(input('\nNota matematica: '))
n3_ing = float(input('\nNota ingles: \n'))

media = (n1_port + n2_mat + n3_ing)/3

print('....\n' * 8)

if media >= 7:
    print('O aluno foi aprovado, sua nota foi', media)
elif media >= 5:
    print('O Aluno esta de recuperação, sua nota foi', media)
else:
    print('O aluno esta reprovado, sua nota foi', media)
