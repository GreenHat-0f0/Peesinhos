from classess import *

usuarios = []

def cadastro():
    novo_email = input("Email: ")
    novo_senha = input("Senha: ")
    usuarios.append(Usuario(novo_email, novo_senha))

curr_user = None
def login():
    global curr_user
    sup_email = input("Email: ")
    sup_senha = input("Senha: ")
    
    for usuario in usuarios:
        if sup_email == usuario.email and sup_senha == usuario.senha:
            curr_user = usuario
            return True
    
def criar_doc():
    nome = input("Nome do documento: " )
    curr_user.documentos.append(Documento(nome, "Titulo,", "Texto", "Assinatura"))