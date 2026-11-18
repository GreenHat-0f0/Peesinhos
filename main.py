# from classess import *
# from funcoes import *

import math
class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.documentos = []
        
class Documento:
    def __init__(self, nome, titulo, texto, assinatura, layout):
        self.nome = nome
        self.titulo = titulo
        self.texto = texto
        self.assinatura = assinatura
        self.layout = layout
        
    def __repr__(self):
        return self.layout
curr_user = None


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


usuarios = []

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

def aaa():
    print("""
          
          1 - Login de usuario
          2 - Cadastrar usuario
          
          """)
    opcao = int(input())
    
    if opcao == 1:
        if login():
            print("Login efetuado com sucesso. ")
            
            def bbb():
                global curr_user
                print("""
                    1 - Gerar documento
                    2 - Editar documento
                    3 - Listar documentos
                    4 - Logout
                    """)
                y = int(input())
                
                if y == 1:
                    criar_doc()
                    bbb()
                    
                elif y == 2:
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
                            
                    bbb()
                
                elif y == 3:
                    for documento in curr_user.documentos:
                        print(documento.layout)
                    bbb()
                        
                elif y == 4:
                    curr_user = None
                    aaa()
            bbb()
                
        else:
            print("email ou senha incorretos.")
            aaa()
        
    elif opcao == 2:
        cadastro()
        aaa()
        
aaa()