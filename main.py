from classess import *
# from funcoes import *

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
            curr_user.documentos.append(Documento(nome, titulo, texto, assinatura, modelo.layout))
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
                    bbb()
                
                elif y == 3:
                    for documento in curr_user.documentos:
                        print(documento)
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