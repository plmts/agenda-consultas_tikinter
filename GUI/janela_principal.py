import tkinter as tk
from janela_pacientes import janela_pacientes

#Funções dos botões
def click_pacientes():
  janela_pacientes()

def click_consultas():
  label.config(text="Puxar Consultas")
  print(entry.get())

def click_medicos():
  label.config(text="Puxar Médicos")
  print(entry.get())

def fechar():
  tela_inicial.destroy()


#Confg da tela
tela_inicial = tk.Tk()
tela_inicial.title("Tela Inicial")
tela_inicial.geometry("800x600")
tela_inicial.resizable(False, False) 
tela_inicial.configure(bg="lightblue")

entry = tk.Entry(tela_inicial)


label = tk.Label(tela_inicial, text="Bem vindo! O que você deseja fazer?")
label.place(relx=0.5, rely=0.1, anchor='center')

#Botões
botao_pacientes = tk.Button(tela_inicial, text="Pacientes", bg="green", fg="white", height=2)
botao_pacientes.place(relx=0.4, rely=0.4, anchor='center')
botao_pacientes.config(command=click_pacientes)
botao_consultas = tk.Button(tela_inicial, text="Consultas", bg="yellow", height=2)
botao_consultas.place(relx=0.5, rely=0.4, anchor='center')
botao_consultas.config(command=click_consultas)
botao_medicos = tk.Button(tela_inicial, text="Médicos", bg="blue", fg="white", height=2)
botao_medicos.place(relx=0.6, rely=0.4, anchor='center')
botao_medicos.config(command=click_medicos)
sair = tk.Button(tela_inicial, text="Sair", height=2)
sair.pack(side="bottom")
sair.config(command=fechar)

tela_inicial.mainloop()