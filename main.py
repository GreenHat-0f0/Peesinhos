from classess import *
from funcoes import *

def aaa():
    print("""
          
          1 - Login de usuario
          2 - Cadastrar usuario
          
          """)
    opcao = int(input())
    
    if opcao == 1:
        if login():
            print("Login efetuado com sucesso. ")
            
            print("""
                  1 - Gerar documento
                  2 - Criar Modelo de documento
                  """)
            y = int(input())
            
            if y == 1:
                pass
            
            elif y == 2:
                pass
        else:
            print("email ou senha incorretos.")
            aaa()
        
    elif opcao == 2:
        cadastro()
        aaa()
        
aaa()