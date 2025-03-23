import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📅 Mi Agenda Personal ✨")
        self.root.geometry("550x450")
        self.root.configure(bg="#FFDEE9")

        # Frame para entrada de datos
        frame_entry = tk.Frame(self.root, padx=10, pady=10, bg="#FFC3A0")
        frame_entry.pack(fill=tk.X)

        tk.Label(frame_entry, text="📆 Fecha:", bg="#FFC3A0", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5,
                                                                                              pady=5)
        self.date_entry = DateEntry(frame_entry, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entry, text="⏰ Hora:", bg="#FFC3A0", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5,
                                                                                             pady=5)
        self.time_entry = tk.Entry(frame_entry, width=10)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_entry, text="📝 Descripción:", bg="#FFC3A0", font=("Arial", 10, "bold")).grid(row=1, column=0,
                                                                                                    padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entry, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Frame para botones
        frame_buttons = tk.Frame(self.root, padx=10, pady=5, bg="#FFB6C1")
        frame_buttons.pack(fill=tk.X)

        tk.Button(frame_buttons, text="➕ Agregar Evento", command=self.add_event, bg="#FFD700",
                  font=("Arial", 10, "bold"), relief=tk.RAISED).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buttons, text="❌ Eliminar Evento", command=self.delete_event, bg="#FF6347",
                  font=("Arial", 10, "bold"), relief=tk.RAISED).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buttons, text="🚪 Salir", command=self.root.quit, bg="#00CED1", font=("Arial", 10, "bold"),
                  relief=tk.RAISED).pack(side=tk.RIGHT, padx=5)

        # Frame para lista de eventos
        frame_list = tk.Frame(self.root, padx=10, pady=10, bg="#E6E6FA")
        frame_list.pack(fill=tk.BOTH, expand=True)

        columns = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_list, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        if not time or not desc:
            messagebox.showwarning("⚠️ Advertencia", "Todos los campos deben ser completados")
            return

        self.tree.insert("", "end", values=(date, time, desc))
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("⚠️ Advertencia", "Seleccione un evento para eliminar")
            return

        confirm = messagebox.askyesno("🗑️ Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
        if confirm:
            self.tree.delete(selected_item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
