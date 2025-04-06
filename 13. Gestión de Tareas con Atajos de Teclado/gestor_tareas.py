import tkinter as tk
from tkinter import messagebox

# Crear ventana principal con un color de fondo
root = tk.Tk()
root.title("🌟 Gestor de Tareas 🌟")
root.geometry("420x500")
root.configure(bg="#f0f4f8")  # Fondo suave

tareas = []

# Función para actualizar la lista visual
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea, completada in tareas:
        texto = f"✅ {tarea}" if completada else f"📝 {tarea}"
        lista_tareas.insert(tk.END, texto)

# Añadir una nueva tarea
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        tareas.append((tarea, False))
        entrada_tarea.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("❗ Campo vacío", "Por favor, escribe una tarea.")

# Marcar como completada
def completar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        tarea, _ = tareas[indice]
        tareas[indice] = (tarea, True)
        actualizar_lista()
    else:
        messagebox.showinfo("⚠️ Selección requerida", "Selecciona una tarea para completarla.")

# Eliminar tarea
def eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        tareas.pop(seleccion[0])
        actualizar_lista()
    else:
        messagebox.showinfo("⚠️ Selección requerida", "Selecciona una tarea para eliminarla.")

# Cerrar app con Escape
def cerrar_aplicacion(event=None):
    root.quit()

# ------------------ INTERFAZ ------------------

# Encabezado colorido
titulo = tk.Label(root, text="🎯 Tu Lista de Tareas", font=("Comic Sans MS", 18, "bold"), bg="#f0f4f8", fg="#4a4e69")
titulo.pack(pady=10)

# Frame para organizar entrada y botones
frame_entrada = tk.Frame(root, bg="#f0f4f8")
frame_entrada.pack(pady=10)

# Entrada
entrada_tarea = tk.Entry(frame_entrada, font=("Arial", 12), width=25, bg="#ffffff", fg="#333")
entrada_tarea.grid(row=0, column=0, padx=5)

# Botón Añadir
boton_agregar = tk.Button(frame_entrada, text="➕ Añadir", bg="#57cc99", fg="white", font=("Arial", 11, "bold"),
                          activebackground="#38a3a5", command=agregar_tarea)
boton_agregar.grid(row=0, column=1, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, font=("Arial", 12), bg="#ffffff", fg="#222", selectbackground="#c9c9ff",
                          activestyle="none", height=12)
lista_tareas.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

# Frame para los botones de acciones
frame_botones = tk.Frame(root, bg="#f0f4f8")
frame_botones.pack(pady=5)

# Botón completar
boton_completar = tk.Button(frame_botones, text="✅ Completar", bg="#f9c74f", fg="#000",
                            font=("Arial", 11, "bold"), command=completar_tarea)
boton_completar.grid(row=0, column=0, padx=10)

# Botón eliminar
boton_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", bg="#f94144", fg="white",
                           font=("Arial", 11, "bold"), command=eliminar_tarea)
boton_eliminar.grid(row=0, column=1, padx=10)

# Footer
footer = tk.Label(root, text="💡 Usa Enter, C, D/Delete, Esc como atajos de teclado", font=("Arial", 9),
                  bg="#f0f4f8", fg="#6c757d")
footer.pack(pady=5)

# ------------------ ATAJOS DE TECLADO ------------------
entrada_tarea.bind("<Return>", agregar_tarea)
root.bind("<c>", completar_tarea)
root.bind("<C>", completar_tarea)
root.bind("<d>", eliminar_tarea)
root.bind("<D>", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)
root.bind("<Escape>", cerrar_aplicacion)

# Iniciar la aplicación
root.mainloop()
