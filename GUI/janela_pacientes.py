import tkinter as tk

def janela_pacientes():
  def add_pacientes():
    label.config(text="Adicionar pacientes")
    print(entry.get())

  def ver_pacientes():
    label.config(text="Ver pacientes")
    print(entry.get())

  def deletar_pacientes():
    label.config(text="Deletar pacientes")
    print(entry.get())

  def sair():
    label.config(text="Voltar")
    print(entry.get())


  #config da tela
  janela_pacientes = tk.Toplevel()
  janela_pacientes.title("Pacientes")
  janela_pacientes.geometry("800x600")
  janela_pacientes.resizable(False, False)
  janela_pacientes.configure(bg="lightblue")
  entry = tk.Entry(janela_pacientes)

  label = tk.Label(janela_pacientes, text="O que você deseja fazer?")
  label.place(relx=0.5, rely=0.1, anchor='center')

  #Botões
  add_paciente = tk.Button(janela_pacientes, text="Adicionar um novo paciente", bg="green", height=2)
  add_paciente.place(relx=0.155, rely=0.4, anchor='center')
  add_paciente.config(command=add_pacientes)
  ver_paciente = tk.Button(janela_pacientes, text="Verificar pacientes cadastrados", bg="yellow", height=2)
  ver_paciente.place(relx=0.5, rely=0.4, anchor='center')
  ver_paciente.config(command=ver_pacientes)
  deletar_paciente = tk.Button(janela_pacientes, text="Deletar um paciente cadastrado", bg="red", height=2)
  deletar_paciente.place(relx=0.85, rely=0.4, anchor='center')
  deletar_paciente.config(command=deletar_pacientes)
  voltar = tk.Button(janela_pacientes, text="Voltar", height=2)
  voltar.pack(side="bottom")
  voltar.config(command=sair)

  janela_pacientes.mainloop()