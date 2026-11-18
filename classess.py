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