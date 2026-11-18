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
    #     return f"""
    
    #  {self.nome}
    # +--------------------+
    # |{self.titulo}{" "*(20 - len(self.titulo))}|
    # |                    |
    # |{self.texto}{" "*(20 - len(self.texto))}|
    # |                    |
    # |                    |
    # |                    |
    # |                    |
    # |                    |
    # |                    |
    # |{self.assinatura}{" "*(20 - len(self.assinatura))}|
    # +--------------------+
    # 
    # """
curr_user = None


class Modelo:
    def __init__(self, cod, layout):
        self.cod = cod
        self.layout = layout
        titulo = documento.titulo
        
    def __repr__(self):
        return self.cod, self.layout

documento = None
modelos = []
modelos.append(Modelo(1, f"""
    
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
              
                      
                      """))
        
# modelos.append(Modelo(2, f"""
    
#      {curr_user.nome}
#     +--------------------+
#     |{curr_user.titulo}{" "*(20 - len(curr_user.titulo))}|
#     |                    |
#     |{curr_user.texto}{" "*(20 - len(curr_user.texto))}|
#     |                    |
#     |                    |
#     |                    |
#     |                    |
#     |                    |
#     |                    |
#     |{curr_user.assinatura}{" "*(20 - len(curr_user.assinatura))}|
#     +--------------------+
              
                      
#                       """))