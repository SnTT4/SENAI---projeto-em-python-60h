import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def conectar():
    return sqlite3.connect('leads_agencia.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS leads(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            interesse TEXT,
            status TEXT
        )       
    ''')
    conn.commit()
    conn.close()


def inserir_lead():
    nome = entry_nome.get()
    email = entry_email.get()
    tel = entry_tel.get()
    interesse = entry_interesse.get()
    status = combo_status.get()

    if nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('''INSERT INTO leads (nome, email, telefone, interesse, status) 
                     VALUES (?, ?, ?, ?, ?)''', (nome, email, tel, interesse, status))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Lead cadastrado com sucesso!')
        limpar_campos()
        mostrar_leads()
    else:
        messagebox.showerror('Erro', 'Nome e E-mail são obrigatórios!')

def mostrar_leads():
    for row in tree.get_children():   
        tree.delete(row)
    
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM leads')
    leads = c.fetchall()
    for lead in leads:
        tree.insert("", "end", values=lead)
    conn.close()    

def deletar_lead():
    selecionado = tree.selection()
    if selecionado:
        lead_id = tree.item(selecionado)['values'][0]
        if messagebox.askyesno("Confirmar", "Deseja excluir este lead?"):
            conn = conectar()
            c = conn.cursor()    
            c.execute('DELETE FROM leads WHERE id = ?', (lead_id,))
            conn.commit()
            conn.close()
            mostrar_leads()
    else:
        messagebox.showwarning('Aviso', 'Selecione um lead para deletar.')

def atualizar_lead():
    selecionado = tree.selection()
    if selecionado:
        lead_id = tree.item(selecionado)['values'][0]
        conn = conectar()
        c = conn.cursor()    
        c.execute('''UPDATE leads SET nome=?, email=?, telefone=?, interesse=?, status=? 
                     WHERE id=?''', 
                  (entry_nome.get(), entry_email.get(), entry_tel.get(), 
                   entry_interesse.get(), combo_status.get(), lead_id))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Dados atualizados!')
        mostrar_leads()
    else:
        messagebox.showerror('Erro', 'Selecione um lead na tabela para editar.')

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_tel.delete(0, tk.END)
    entry_interesse.delete(0, tk.END)
    combo_status.set("Em andamento")

janela = tk.Tk()
janela.title('Sistema de Gestão de Leads - Marketing Digital')
janela.geometry("850x600")

campos = [
    ("Nome:", 0), ("E-mail:", 1), 
    ("Telefone:", 2), ("Interesse:", 3)
]

entries = {}
for texto, linha in campos:
    tk.Label(janela, text=texto).grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(janela, width=30)
    entry.grid(row=linha, column=1, padx=10, pady=5)
    entries[texto] = entry

entry_nome = entries["Nome:"]
entry_email = entries["E-mail:"]
entry_tel = entries["Telefone:"]
entry_interesse = entries["Interesse:"]

tk.Label(janela, text="Status:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
combo_status = ttk.Combobox(janela, values=["Em andamento", "Convertido", "Perdido"], state="readonly")
combo_status.set("Em andamento")
combo_status.grid(row=4, column=1, padx=10, pady=5)

frame_btns = tk.Frame(janela)
frame_btns.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(frame_btns, text='Salvar Novo', command=inserir_lead, bg="green", fg="white", width=12).pack(side="left", padx=5)
tk.Button(frame_btns, text='Atualizar', command=atualizar_lead, bg="blue", fg="white", width=12).pack(side="left", padx=5)
tk.Button(frame_btns, text='Deletar', command=deletar_lead, bg="red", fg="white", width=12).pack(side="left", padx=5)


colunas = ('ID', 'NOME', 'E-MAIL', 'TELEFONE', 'INTERESSE', 'STATUS')
tree = ttk.Treeview(janela, columns=colunas, show='headings')
tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=130)

criar_tabela()
mostrar_leads()

janela.mainloop()