import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("¡Hey!", "Primero escribe algo antes de agregarlo.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista - ¡Agrega tu Estilo!")
ventana.geometry("500x400")
ventana.configure(bg="#282c34")

# Estilos visuales
definir_fuente = ("Arial", 12, "bold")
color_fondo = "#61afef"
color_texto = "white"

# Etiqueta
etiqueta = tk.Label(ventana, text="Escribe algo cool:", font=definir_fuente, bg="#282c34", fg=color_texto)
etiqueta.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada_texto.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="➕ Agregar", font=definir_fuente, bg=color_fondo, fg=color_texto, command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10, font=("Arial", 12))
lista_datos.pack(pady=10)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="🗑 Limpiar", font=definir_fuente, bg="red", fg=color_texto, command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
