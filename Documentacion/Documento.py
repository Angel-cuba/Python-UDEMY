def saludar(arg):
        """Esto es un ejemplo de comentarios"""
        print("Hola ", arg)
help(saludar)

################################################################
class Persona():
          def __init__(self):
              """Ejemplo 2.1"""
              pass
          def estado(self):
              """Segundo ejemplo 2.2"""
              pass

i = Persona()
#Este help() puede ser usado desde cualquier otro archivo externo
#de esta manera podemos leer cualquier comentario hecho anteriormente
help(i) 