# 📚 Sistema de Biblioteca
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre

    def pedir_libro(self, libro):
        libro.prestar()

    def devolver_libro(self, libro):
        libro.devolver()

# Ejecución del Sistema de Biblioteca
libro1 = Libro("El Quijote", "Cervantes")
miembro1 = Miembro("Ana")
miembro1.pedir_libro(libro1)
miembro1.devolver_libro(libro1)