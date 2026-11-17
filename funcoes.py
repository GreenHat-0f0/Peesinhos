from classess import *

usuarios = []

def cadastro():
    novo_email = input("Email: ")
    novo_senha = input("Senha: ")
    usuarios.append(Usuario(novo_email, novo_senha))

def login():
    sup_email = input("Email: ")
    sup_senha = input("Senha: ")
    
    for usuario in usuarios:
        if sup_email == usuario.email and sup_senha == usuario.senha:
            return True
    