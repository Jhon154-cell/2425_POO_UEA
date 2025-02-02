# 🎮 Sistema de Tienda de Videojuegos
class Juego:
    def __init__(self, titulo, genero, precio):
        self.titulo = titulo
        self.genero = genero
        self.precio = precio

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.biblioteca = []

    def comprar_juego(self, juego):
        self.biblioteca.append(juego)
        print(f"{self.nombre} compró el juego '{juego.titulo}'.")

class Compra:
    def __init__(self, jugador, juego):
        self.jugador = jugador
        self.juego = juego

    def realizar_compra(self):
        self.jugador.comprar_juego(self.juego)

# Ejecución del Sistema de Tienda de Videojuegos
juego1 = Juego("The Legend of Zelda", "Aventura", 60)
jugador1 = Jugador("Mario")
compra1 = Compra(jugador1, juego1)
compra1.realizar_compra()
