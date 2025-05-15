import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import subprocess as spr

# Configurações do tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Função para abrir a tela de login
def abrir_login():
    login_screen()

# Função para a tela de login
def login_screen():
    login_window = ctk.CTk()
    login_window.geometry("300x300")
    login_window.title("TecMed")

    def abrir_agendamento():
        agendamento_screen()

    ctk.CTkLabel(login_window, text="Fazer Login:").pack(pady=5)
    ctk.CTkLabel(login_window, text="CPF cadastrado:").pack(pady=5)
    ctk.CTkEntry(login_window).pack(pady=5)
    ctk.CTkButton(login_window, text="Ir Para Agendamento", command=abrir_agendamento).pack(pady=5)

    login_window.mainloop()

# Função para abrir a tela de agendamento
def agendamento_screen():
    agendamento_window = ctk.CTk()
    agendamento_window.geometry("323x300")
    agendamento_window.title("Agendamento")

    def cancelar_agendamento():
        cancelamento_screen()

    def agendado():
        # Salvar dados do agendamento
        tipo_agendamento = opção.get()
        data_agendamento = entry_data.get()
        with open("agendamento.txt", "a") as file:
            file.write(f"Tipo: {tipo_agendamento}, Data: {data_agendamento}\n")
        messagebox.showinfo("Concluido!!", "Agendamento realizado com sucesso!")

    opção = ctk.IntVar()

    ctk.CTkLabel(agendamento_window, text="Faça seu agendamento:").pack(pady=5)
    ctk.CTkRadioButton(agendamento_window, text="Consulta", variable=opção, value=1).pack(pady=5)
    ctk.CTkRadioButton(agendamento_window, text="Exame", variable=opção, value=2).pack(pady=5)
    ctk.CTkRadioButton(agendamento_window, text="Retorno", variable=opção, value=3).pack(pady=5)
    ctk.CTkLabel(agendamento_window, text="Data do agendamento:").pack(pady=5)
    entry_data = ctk.CTkEntry(agendamento_window)
    entry_data.pack(pady=5)
    ctk.CTkButton(agendamento_window, text="Agendar", command=agendado).pack(pady=5)
    ctk.CTkButton(agendamento_window, text="Cancelar Agendamento", command=cancelar_agendamento).pack(pady=5)

    agendamento_window.mainloop()

# Função para a tela de cancelamento
def cancelamento_screen():
    cancelamento_window = ctk.CTk()
    cancelamento_window.geometry("300x300")
    cancelamento_window.title("Cancelar")

    def cancelamento():
        messagebox.showwarning("Concluido", "Cancelado com sucesso!")

    ctk.CTkLabel(cancelamento_window, text="Cancele aqui: ").pack(pady=5)
    ctk.CTkButton(cancelamento_window, text="Cancelar", command=cancelamento).pack(pady=5)

    cancelamento_window.mainloop()

# Função para a tela de cadastro
def cadastro_screen():
    cadastro_window = ctk.CTk()
    cadastro_window.geometry("800x800")
    cadastro_window.title("TecMed")

    def login():
        login_screen()

    opção = ctk.IntVar()

    def salvar_dados_cadastro():
        nome_usuario = entry_nome.get()
        data_nascimento = entry_data_nascimento.get()
        cpf = entry_cpf.get()
        rg = entry_rg.get()
        telefone = entry_telefone.get()
        sexo = "Masculino" if opção.get() == 1 else "Feminino"

        # Salvar dados do cadastro no arquivo
        with open("cadastro.txt", "a") as file:
            file.write(f"Nome: {nome_usuario}, Data Nascimento: {data_nascimento}, CPF: {cpf}, RG: {rg}, Telefone: {telefone}, Sexo: {sexo}\n")
        messagebox.showinfo("Concluido", "Cadastro realizado com sucesso!")

    ctk.CTkLabel(cadastro_window, text="Já é cadastrado?").pack(pady=5)
    ctk.CTkButton(cadastro_window, text="Login", command=abrir_login).pack(pady=5)
    ctk.CTkLabel(cadastro_window, text="Não é cadastrado? Cadastre AQUI EM BAIXO:").pack(pady=5)

    ctk.CTkLabel(cadastro_window, text="Nome:").pack(pady=5)
    entry_nome = ctk.CTkEntry(cadastro_window)
    entry_nome.pack(pady=5)
    ctk.CTkLabel(cadastro_window, text="Data de Nascimento:").pack(pady=5)
    entry_data_nascimento = ctk.CTkEntry(cadastro_window)
    entry_data_nascimento.pack(pady=5)
    ctk.CTkLabel(cadastro_window, text="CPF:").pack(pady=5)
    entry_cpf = ctk.CTkEntry(cadastro_window)
    entry_cpf.pack(pady=5)
    ctk.CTkLabel(cadastro_window, text="RG:").pack(pady=5)
    entry_rg = ctk.CTkEntry(cadastro_window)
    entry_rg.pack(pady=5)
    ctk.CTkLabel(cadastro_window, text="Numero de Contato:").pack(pady=5)
    entry_telefone = ctk.CTkEntry(cadastro_window)
    entry_telefone.pack(pady=5)

    ctk.CTkLabel(cadastro_window, text="Sexo:").pack(pady=5)
    ctk.CTkRadioButton(cadastro_window, text="Masculino", variable=opção, value=1).pack(pady=5)
    ctk.CTkRadioButton(cadastro_window, text="Feminino", variable=opção, value=2).pack(pady=5)
    ctk.CTkButton(cadastro_window, text="Finalizar", command=salvar_dados_cadastro).pack(pady=5)

    cadastro_window.mainloop()

# Iniciar a tela de cadastro
cadastro_screen()
