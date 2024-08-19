import tkinter as tk

#Cria a janela da tela inicial
tela_inicial = tk.Tk()
tela_inicial.title("Tela Inicial")
tela_inicial.geometry("800x640")
tela_inicial.resizable(False, False) 
tela_inicial.configure(bg="lightblue")
tela_inicial.attributes('-alpha', 0.95)


label = tk.Label(tela_inicial, text="Bem vindo! O que você deseja fazer:")
label.place(relx=0.5, rely=0.1, anchor='center')


botao_pacientes = tk.Button(tela_inicial, text="Pacientes", bg="green", fg="white", height=2)
botao_pacientes.place(relx=0.4, rely=0.4, anchor='center')
botao_consultas = tk.Button(tela_inicial, text="Consultas", bg="yellow", height=2)
botao_consultas.place(relx=0.5, rely=0.4, anchor='center')
botao_medicos = tk.Button(tela_inicial, text="Médicos", bg="blue", fg="white", height=2)
botao_medicos.place(relx=0.6, rely=0.4, anchor='center')



tela_inicial.mainloop()