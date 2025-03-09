class Libro:
    # Representa un libro en la biblioteca
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    # Representa un usuario de la biblioteca
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista para almacenar libros prestados dinámicamente

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id}), Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    # Clase que gestiona los libros y usuarios
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros con ISBN como clave (búsqueda eficiente)
        self.usuarios = set()  # Conjunto para asegurar unicidad de IDs de usuario
        self.registro_usuarios = {}  # Diccionario para asociar IDs de usuario con objetos Usuario

    def agregar_libro(self, libro):
        # Agregar un libro al catálogo
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya está en la biblioteca.")

    def eliminar_libro(self, isbn):
        # Eliminar un libro del catálogo
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        # Registrar un nuevo usuario
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)  # Se usa un conjunto para asegurar unicidad
            self.registro_usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def eliminar_usuario(self, user_id):
        # Eliminar un usuario de la biblioteca
        if user_id in self.usuarios:
            del self.registro_usuarios[user_id]
            self.usuarios.remove(user_id)
            print(f"Usuario con ID {user_id} eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        # Prestar un libro a un usuario
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.registro_usuarios[user_id]
            libro = self.libros.pop(isbn)  # Remueve el libro del catálogo
            usuario.libros_prestados.append(libro)  # Se usa lista para manejar múltiples préstamos
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        # Devolver un libro a la biblioteca
        if user_id in self.usuarios:
            usuario = self.registro_usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Lo devuelve al catálogo
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        # Buscar libros por título, autor o categoría
        encontrados = [str(libro) for libro in self.libros.values() if valor.lower() in getattr(libro, criterio).lower()]
        print("\n".join(encontrados) if encontrados else "No se encontraron libros.")

    def listar_libros_prestados(self, user_id):
        # Listar los libros prestados a un usuario
        if user_id in self.usuarios:
            usuario = self.registro_usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("No tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Ejemplo de uso
biblio = Biblioteca()
libro1 = Libro("1984", "George Orwell", "Ficción", "123456789")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "987654321")
libro3 = Libro("El tercer ojo", "Lobsang Rampa", "Misticismo", "111111111")
libro4 = Libro("Viaje al centro de la Tierra", "Julio Verne", "Aventura", "222222222")
libro5 = Libro("Veinte mil leguas de viaje submarino", "Julio Verne", "Aventura", "333333333")
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("Jhon Santana", "U002")
usuario3 = Usuario("Vanny Cobeña", "U003")
usuario4 = Usuario("Edith Chica", "U004")
usuario5 = Usuario("Jhony Santana", "U005")

biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.agregar_libro(libro3)
biblio.agregar_libro(libro4)
biblio.agregar_libro(libro5)
biblio.registrar_usuario(usuario1)
biblio.registrar_usuario(usuario2)
biblio.registrar_usuario(usuario3)
biblio.registrar_usuario(usuario4)
biblio.registrar_usuario(usuario5)
biblio.prestar_libro("U001", "123456789")
biblio.listar_libros_prestados("U001")
biblio.devolver_libro("U001", "123456789")
