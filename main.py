# from classess import *
# from funcoes import *
import pickle
import math
import os
from pathlib import Path

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.documentos = []

usuarios = []

usuarios.append(Usuario("kiara@gmail.com", "1234"))
usuarios.append(Usuario("eliott@gmail.com", "1234"))

#para testes rapidos
usuarios.append(Usuario("k", "1"))
usuarios.append(Usuario("e", "1"))
    
class Documento:
    def __init__(self, nome, titulo, texto, assinatura, layout):
        self.nome = nome
        self.titulo = titulo
        self.texto = texto
        self.assinatura = assinatura
        self.layout = layout
        
    def __repr__(self):
        return self.layout

class Modelo:
    def __init__(self, cod, layout):
        self.cod = cod
        self.layout = layout
        
    def __repr__(self):
        return self.cod, self.layout
modelos = []

def layout1(documento):
    return (f"""   
     {documento.nome}
    +--------------------+
    |{documento.titulo}{" "*(20 - len(documento.titulo))}|
    |                    |
    |{documento.texto}{" "*(20 - len(documento.texto))}|
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |{documento.assinatura}{" "*(20 - len(documento.assinatura))}|
    +--------------------+
                      """)
modelos.append(Modelo(1, layout1))

def layout2(documento):
    return (f"""   
     {documento.nome}
    +--------------------+
    |{" "*(20 - len(documento.titulo))}{documento.titulo}|
    |                    |
    |{documento.texto}{" "*(20 - len(documento.texto))}|
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |{" "*(20 - len(documento.assinatura))}{documento.assinatura}|
    +--------------------+
                      """)
modelos.append(Modelo(2, layout2))

def layout3(documento):
    return (f"""   
     {documento.nome}
    +--------------------+
    |{" "* math.floor((20 - len(documento.titulo))/2)}{documento.titulo}{" "* math.ceil((20 - len(documento.titulo))/2)}|
    |                    |
    |{documento.texto}{" "*(20 - len(documento.texto))}|
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |{" "* math.floor((20 - len(documento.assinatura))/2)}{documento.assinatura}{" "* math.ceil((20 - len(documento.assinatura))/2)}|
    +--------------------+
                      """)
modelos.append(Modelo(3, layout3))


curr_user = None

def cadastro():
    novo_email = input("Email: ")
    novo_senha = input("Senha: ")
    usuarios.append(Usuario(novo_email, novo_senha))

# curr_user = None
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
    titulo = input("Titulo: ")
    texto = input("Texto: ")
    assinatura = input("Assinatura: ")
    modelor = int(input("Modelo(cod): "))
    for modelo in modelos:
        if modelor == modelo.cod:
            curr_user.documentos.append(Documento(nome, titulo, texto, assinatura, None))
            for documento in curr_user.documentos:
                if documento.nome == nome:
                    documento.layout = modelo.layout(documento)
            break

firstdocs = usuarios

if os.path.exists('Docs.pkl'):
    with open('Docs.pkl', 'rb') as f:
        usuarios = pickle.load(f)

def aaa():
    global usuarios
    print("""
1 - Login de usuário
2 - Cadastro de usuário
          """)
    opcao = int(input("Opção: "))
    clear()
    if opcao == 1:
        print("Login de usuário\n")
        if login():
            clear()
            print("Login efetuado com sucesso. ")
            
            def bbb():
                global curr_user, usuarios
                print("""
1 - Gerar documento
2 - Editar documento
3 - Apagar documento
4 - Listar documentos
5 - Salvar Dados
6 - Apagar Dados
7 - Logout
                    """)
                y = int(input("Opção: "))
                clear()
                
                if y == 1:
                    print("Gerar documento\n")
                    criar_doc()
                    clear()
                    print("Documento criado.")
                    bbb()
                
                elif y == 2:
                    print("Editar documento\n")
                    edit = input("Nome do documento a ser editado: ")
                    for documento in curr_user.documentos:
                        if documento.nome == edit:
                            documento.titulo = input("Titulo: ")
                            documento.texto = input("Texto: ")
                            documento.assinatura = input("Assinatura: ")
                            lyy = int(input("Modelo(cod): "))
                            for modelo in modelos:
                                if modelo.cod == lyy:
                                    documento.layout = modelo.layout(documento)
                                    break
                    clear()
                    print("Documento alterado.")
                    bbb()    
                    
                elif y == 3:
                    print("Apagar documento\n")
                    lixo = input("Nome do documento à ser apagado: ")
                    for documento in curr_user.documentos:
                        if documento.nome == lixo:
                            curr_user.documentos.remove(documento)
                            break
                    clear()
                    print("Documento removido.")
                    bbb()
                
                elif y == 4:
                    for documento in curr_user.documentos:
                        print(documento.layout)
                    if not curr_user.documentos:
                        print("Nenhum documento salvo.")
                    voltar = input("\nDigite ENTER para sair. ")
                    clear()
                    bbb()
                        
                elif y == 5:
                    with open('Docs.pkl', 'wb') as f:
                        pickle.dump(curr_user.documentos, f)
                        clear()
                        print("Dados salvos.")
                        bbb()
                
                elif y == 6:
                    Path("Docs.pkl").unlink(missing_ok=True)
                    curr_user.documentos = firstdocs
                    clear()
                    print("Dados apagados.")
                    bbb()
                        
                elif y == 7:
                    curr_user = None
                    clear()
                    print("Logout efetuado.")
                    aaa()
                    
                else:
                    clear()
                    print("Opção inválida, tente novamente.")
                    bbb()
            bbb()
                
        else:
            clear()
            print("Email ou senha incorretos.")
            aaa()
        
    elif opcao == 2:
        print("Cadastro de usuário\n")
        cadastro()
        clear()
        print("Novo usuário cadastrado.")
        aaa()
    else:
        clear()
        print("Opção inválida, tente novamente.")
        aaa()
clear()
print ("Olá!")   
aaa()