import tkinter as tk
from tkinter import messagebox

def agendar():
    pnome = nome.get()
    pcpf = cpf.get()
    pdoutor = doutor.get()
    pdata = data.get()
    phorario = horario.get()

    if pnome and pcpf and pdoutor and pdata and phorario:
        with open("agendamentos.txt", "a") as arquivo:
            arquivo.write(f"Nome: {pnome}\nCPF: {pcpf}\nDoutor: {pdoutor}\nData: {pdata}\nHorário: {phorario}\n\n")
        
        messagebox.showinfo("Agendamento Confirmado", "Seu agendamento foi realizado com sucesso!")
        
        nome.delete(0, tk.END)
        cpf.delete(0, tk.END)
        doutor.delete(0, tk.END)
        data.delete(0, tk.END)
        horario.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

janela = tk.Tk()
janela.geometry("500x600")
janela.title("Agendamento - TecMed")
janela.config(bg="Light Blue")

titulo = tk.Label(janela, text="Agendamento de Consultas", font=("Arial", 18, "bold"), fg="#333", bg="Light Blue")
titulo.pack(pady=20)

tk.Label(janela, text="Nome Completo:", font=("Arial", 12), bg="Light Blue").pack(pady=5)
nome = tk.Entry(janela, font=("Arial", 12), bd=2, relief="groove", width=30)
nome.pack(pady=10)

tk.Label(janela, text="CPF:", font=("Arial", 12), bg="Light Blue").pack(pady=5)
cpf = tk.Entry(janela, font=("Arial", 12), bd=2, relief="groove", width=30)
cpf.pack(pady=10)

tk.Label(janela, text="Doutor:", font=("Arial", 12), bg="Light Blue").pack(pady=5)
doutor = tk.Entry(janela, font=("Arial", 12), bd=2, relief="groove", width=30)
doutor.pack(pady=10)

tk.Label(janela, text="Data (dd/mm/aaaa):", font=("Arial", 12), bg="Light Blue").pack(pady=5)
data = tk.Entry(janela, font=("Arial", 12), bd=2, relief="groove", width=30)
data.pack(pady=10)

tk.Label(janela, text="Horário (hh:mm):", font=("Arial", 12), bg="Light Blue").pack(pady=5)
horario = tk.Entry(janela, font=("Arial", 12), bd=2, relief="groove", width=30)
horario.pack(pady=10)

botao_agendar = tk.Button(janela, text="Agendar", font=("Arial", 14, "bold"), fg="white", bg="Green", bd=0, relief="raised", width=20, height=2, command=agendar)
botao_agendar.pack(pady=20)

rodape = tk.Label(janela, text="TecMed - Agendamento de Consultas", font=("Arial", 10), fg="#333", bg="Light Blue")
rodape.pack(side="bottom", pady=10)

janela.mainloop()
