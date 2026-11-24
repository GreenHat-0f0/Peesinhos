# from classess import *
# from funcoes import *
import pickle
import math
import os
import getpass


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
        doc_exemplo = Documento("Exemplo", "Título", "Texto", "Assinatura", None)
        return f"Modelo: {self.cod}\n{self.layout(doc_exemplo)}"
modelos = []

def layout1(documento):
    return (f"""   
    Nome: {documento.nome}
    +--------------------+
    | {documento.titulo}{" "*(19 - len(documento.titulo))}|
    |                    |
    | {documento.texto}{" "*(19 - len(documento.texto))}|
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    | {documento.assinatura}{" "*(19 - len(documento.assinatura))}|
    +--------------------+
                      """)
modelos.append(Modelo(1, layout1))

def layout2(documento):
    return (f"""   
    Nome: {documento.nome}
    +--------------------+
    |{" "*(19 - len(documento.titulo))}{documento.titulo} |
    |                    |
    |{" "*(19 - len(documento.texto))}{documento.texto} |
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |{" "*(19 - len(documento.assinatura))}{documento.assinatura} |
    +--------------------+
                      """)
modelos.append(Modelo(2, layout2))

def layout3(documento):
    return (f"""   
     {documento.nome}
    +--------------------+
    |{" "* math.floor((20 - len(documento.titulo))/2)}{documento.titulo}{" "* math.ceil((20 - len(documento.titulo))/2)}|
    |                    |
    |{" "* math.floor((20 - len(documento.texto))/2)}{documento.texto}{" "* math.ceil((20 - len(documento.texto))/2)}|
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
    while True:
        novo_email = input("Email: ")
        if any(usuario.email == novo_email for usuario in usuarios):
            print("Email já cadastrado, utilize outro.")
        else:
            break
    
    novo_senha = getpass.getpass("Senha: ")
    usuarios.append(Usuario(novo_email, novo_senha))

def login():
    global curr_user
    sup_email = input("Email: ")
    sup_senha = getpass.getpass("Senha: ")
    
    for usuario in usuarios:
        if sup_email == usuario.email and sup_senha == usuario.senha:
            curr_user = usuario
            return True
    
def criar_doc():
    while True:
        nome = input("Nome do documento: ")
        if any(documento.nome == nome for documento in curr_user.documentos):
            print("Nome já existente, escolha outro.")
        else:
            break
            
    titulo = input("Titulo: ")
    texto = input("Texto: ")
    assinatura = input("Assinatura: ")
    for modelo in modelos:
        print(modelo.__repr__())
        print()
    modelor = int(input("Modelo(cod): "))
    for modelo in modelos:
        if modelor == modelo.cod:
            curr_user.documentos.append(Documento(nome, titulo, texto, assinatura, None))
            for documento in curr_user.documentos:
                if documento.nome == nome:
                    documento.layout = modelo.layout(documento)
            break

def aaa():
    global usuarios, documentos
    
    if os.path.exists('Dados.pkl'):
        with open('Dados.pkl', 'rb') as f:
            usuarios = pickle.load(f)
        
    
    while True:
        try:
            print("""
1 - Login de usuário
2 - Cadastro de usuário
0 - Sair
            """)
            opcao = int(input("Opção: "))
            break
        except ValueError:
            clear()
            print("Opção inválida, tente novamente.")
    
    clear()
    if opcao == 1:
        print("Login de usuário\n")
        if login():
            clear()
            print("Login efetuado com sucesso. ")
            
            def bbb():
                global curr_user, usuarios, documentos
                
                
                
                while True:
                    try:
                        print("""
1 - Gerar documento
2 - Editar documento
3 - Apagar documento
4 - Listar documentos
5 - Salvar Dados
6 - Apagar Dados
0 - Logout
                        """)
                        y = int(input("Opção: "))
                        break
                    except ValueError:
                        clear()
                        print("Opção inválida, tente novamente.")
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
                    with open('Dados.pkl', 'wb') as f:
                        pickle.dump(usuarios, f)
                        clear()
                        print("Dados salvos.")
                    bbb()
                
                elif y == 6:
                    curr_user.documentos = []
                    with open('Dados.pkl', 'wb') as f:
                        pickle.dump(usuarios, f)
                    clear()
                    print("Dados apagados.")
                    bbb()
                        
                elif y == 0:
                    if os.path.exists('Dados.pkl'):
                        with open('Dados.pkl', 'rb') as f:
                            usuarios = pickle.load(f)
                    
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
        
        with open('Dados.pkl', 'wb') as f:
            pickle.dump(usuarios, f)
            
        clear()
        print("Novo usuário cadastrado.")
        aaa()
        
    elif opcao == 0:
        clear()
        pass
        
    else:
        clear()
        print("Opção inválida, tente novamente.")
        aaa()
clear()
print ("Olá!")   
aaa()
