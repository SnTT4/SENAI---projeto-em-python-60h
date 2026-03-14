import tkinter



def mostrar():
    m = input_.get()
    text_MOSTAR.config(text = m)
    





janela  =  tkinter.Tk()
janela.geometry('400x600')
janela.title('ISSO É UMA JANELA')


text = tkinter.Label(janela, text = 'ESCREVA ALGO',font=('Poplar Std', 15) )
text.pack(pady=20)


input_ = tkinter.Entry(janela, font=('arial', 15))
input_.pack(pady = 20)


btn = tkinter.Button(janela, text='CLIQUE AQUI' ,font=('arial', 15), command= mostrar)
btn.pack(pady=20)


text_MOSTAR = tkinter.Label(janela, text = '',font=('Poplar Std', 15) )
text_MOSTAR.pack(pady=20)



janela.mainloop()