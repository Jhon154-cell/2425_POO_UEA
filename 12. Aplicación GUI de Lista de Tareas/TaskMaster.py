import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas

# Colores llamativos con degradado
BG_COLOR_START = "#0f4c75"  # Azul oscuro fuerte
BG_COLOR_END = "#3282b8"  # Azul claro vibrante
TEXT_COLOR = "#ffffff"  # Texto blanco
BTN_COLOR = "#1b262c"  # Azul grisáceo oscuro
BTN_TEXT = "#ffffff"  # Texto blanco
LISTBOX_BG = "#bbe1fa"  # Celeste claro
LISTBOX_TEXT = "#000000"  # Texto negro


class TaskMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskMaster - Lista de Tareas")
        self.root.geometry("500x600")

        # Crear degradado de fondo
        self.canvas = Canvas(root, width=500, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.create_gradient()

        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, font=("Arial", 16), bg=TEXT_COLOR, fg=BTN_COLOR, insertbackground=BTN_COLOR)
        self.entry.place(x=30, y=40, width=440, height=40)
        self.entry.bind("<Return>", self.add_task)

        # Lista de tareas
        self.listbox = tk.Listbox(root, font=("Arial", 16), bg=LISTBOX_BG, fg=LISTBOX_TEXT, selectbackground=BTN_COLOR,
                                  selectforeground=BTN_TEXT)
        self.listbox.place(x=30, y=100, width=440, height=350)

        # Botones con nuevo estilo
        self.add_btn = tk.Button(root, text="➕ Añadir", bg=BTN_COLOR, fg=BTN_TEXT, font=("Arial", 14, "bold"),
                                 command=self.add_task, padx=10, pady=5, borderwidth=3)
        self.add_btn.place(x=30, y=480, width=140, height=50)

        self.complete_btn = tk.Button(root, text="✔ Completar", bg=BTN_COLOR, fg=BTN_TEXT, font=("Arial", 14, "bold"),
                                      command=self.complete_task, padx=10, pady=5, borderwidth=3)
        self.complete_btn.place(x=180, y=480, width=140, height=50)

        self.delete_btn = tk.Button(root, text="🗑 Eliminar", bg=BTN_COLOR, fg=BTN_TEXT, font=("Arial", 14, "bold"),
                                    command=self.delete_task, padx=10, pady=5, borderwidth=3)
        self.delete_btn.place(x=330, y=480, width=140, height=50)

    def create_gradient(self):
        for i in range(600):
            color = self.interpolate_color(BG_COLOR_START, BG_COLOR_END, i / 600)
            self.canvas.create_line(0, i, 500, i, fill=color, width=1)

    def interpolate_color(self, start_color, end_color, factor):
        s = [int(start_color[i:i + 2], 16) for i in (1, 3, 5)]
        e = [int(end_color[i:i + 2], 16) for i in (1, 3, 5)]
        rgb = [int(s[j] + (e[j] - s[j]) * factor) for j in range(3)]
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "No puedes agregar una tarea vacía.")

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            self.listbox.delete(index)
            self.listbox.insert(tk.END, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskMaster(root)
    root.mainloop()
