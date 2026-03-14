# ---

# **ATIVIDADE 2** 

# Crie um formulário em Tkinter

# Problema: Sistema de Cadastro de Clientes

# Você é um desenvolvedor de software e foi contratado por uma empresa de serviços para criar um sistema de cadastro de clientes. O sistema deve permitir que os clientes forneçam suas informações pessoais, como nome, idade, e-mail, endereço, celular...

# ***Atividade:***
# Crie um formulário em Tkinter que contenha os seguintes campos:
# Nome
# Idade
# E-mail
# Endereço
# Celular

# Cep

# Cidade

# Cursos

# O formulário deve ter um botão de "Enviar" que, quando clicado, imprima as informações do cliente na console.

# Tamanho  da tela  = '1700x750’

import tkinter as tk


def mostrar_shell():
    print(f'''

        NOME - {nome.get()}
        IDADE - {idade.get()}
        ENDEREÇO - {endereco.get()}
        CIDADE - {cidade.get()}
        E-MAIL - {email.get()}
        CELULAR - {celular.get()}
        




         ''')




root = tk.Tk()
root.geometry('1700x750')
root.iconbitmap('icon.ico')

tk.Label(root, text='FORMULARIO', font=('System')).pack(pady=10)

tk.Label(root, text='Nome: ', font=('System')).pack(pady=10)
nome =  tk.Entry(root)
nome.pack()

tk.Label(root, text='Cidade: ', font=('System')).pack(pady=10)
cidade =  tk.Entry(root)
cidade.pack()

tk.Label(root, text='Idade: ', font=('System')).pack(pady=10)
idade =  tk.Entry(root)
idade.pack()

tk.Label(root, text='E-mail: ', font=('System')).pack(pady=10)
email =  tk.Entry(root)
email.pack()

tk.Label(root, text='Endereço: ', font=('System')).pack(pady=10)
endereco =  tk.Entry(root)
endereco.pack()

tk.Label(root, text='Celular: ', font=('System')).pack(pady=10)
celular =  tk.Entry(root)
celular.pack()

btn = tk.Button(root, text= 'envia par o shell', command=mostrar_shell)
btn.pack(pady = 20)


root.mainloop()


input('digite enter para sair...')