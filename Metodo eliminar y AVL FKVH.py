# Arbol binario Metodo eliminar y AVL || FERNANDO KENJI VILLARROEL HENZAN - 220030464

import tkinter as tk
from tkinter import simpledialog, messagebox

class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

def altura(nodo):
    if not nodo:
        return 0
    return nodo.altura
def actualizar_altura(nodo):
    if nodo:
        nodo.altura = 1 + max(altura(nodo.izquierda), altura(nodo.derecha))
def factor_equilibrio(nodo):
    if not nodo:
        return 0
    return altura(nodo.izquierda) - altura(nodo.derecha)
def rotacion_izquierda(z):
    y = z.derecha
    T2 = y.izquierda

    y.izquierda= z
    z.derecha= T2

    actualizar_altura(z)
    actualizar_altura(y)

    return y

def rotacion_derecha(y):
    x = y.izquierda
    T2 = x.derecha

    x.derecha = y
    y.izquierda = T2

    actualizar_altura(y)
    actualizar_altura(x)

    return x

def insertar_avl(raiz, valor, canvas):
    if not raiz:
        return NodoAVL(valor)
    elif valor < raiz.valor:
        raiz.izquierda = insertar_avl(raiz.izquierda, valor, canvas)
    else:
        raiz.derecha = insertar_avl(raiz.derecha, valor, canvas)

    actualizar_altura(raiz)
    balance = factor_equilibrio(raiz)

    # Caso izquierda-izquierda
    if balance > 1 and valor < raiz.izquierda.valor:
        return rotacion_derecha(raiz)

    # Caso derecha-derecha
    if balance < -1 and valor > raiz.derecha.valor:
        return rotacion_izquierda(raiz)

    # Caso izquierda-derecha
    if balance > 1 and valor > raiz.izquierda.valor:
        raiz.izquierda = rotacion_izquierda(raiz.izquierda)
        return rotacion_derecha(raiz)

    # Caso derecha-izquierda
    if balance < -1 and valor < raiz.derecha.valor:
        raiz.derecha = rotacion_derecha(raiz.derecha)
        return rotacion_izquierda(raiz)

    return raiz

def encontrar_minimo(nodo):
    while nodo.izquierda:
        nodo = nodo.izquierda
    return nodo

def eliminar_avl(raiz, valor, canvas):
    if not raiz:
        return raiz
    elif valor < raiz.valor:
        raiz.izquierda = eliminar_avl(raiz.izquierda, valor, canvas)
    elif valor > raiz.valor:
        raiz.derecha = eliminar_avl(raiz.derecha, valor, canvas)
    else:
        if not raiz.izquierda:
            return raiz.derecha
        elif not raiz.derecha:
            return raiz.izquierda
        else:
            min_derecha = encontrar_minimo(raiz.derecha)
            raiz.valor = min_derecha.valor
            raiz.derecha = eliminar_avl(raiz.derecha, min_derecha.valor, canvas)

    if not raiz:
        return raiz

    actualizar_altura(raiz)
    balance = factor_equilibrio(raiz)

    # Rebalanceo (similar a la inserción)
    if balance > 1 and factor_equilibrio(raiz.izquierda) >= 0:
        return rotacion_derecha(raiz)
    if balance > 1 and factor_equilibrio(raiz.izquierda) < 0:
        raiz.izquierda = rotacion_izquierda(raiz.izquierda)
        return rotacion_derecha(raiz)
    if balance < -1 and factor_equilibrio(raiz.derecha) <= 0:
        return rotacion_izquierda(raiz)
    if balance < -1 and factor_equilibrio(raiz.derecha) > 0:
        raiz.derecha = rotacion_derecha(raiz.derecha)
        return rotacion_izquierda(raiz)

    return raiz

class ArbolAVLGUI:
    def __init__(self, master):
        self.master = master
        master.title("Visualización de Árbol AVL")
        self.canvas_ancho = 800
        self.canvas_alto = 600
        self.canvas = tk.Canvas(master, width=self.canvas_ancho, height=self.canvas_alto, bg="white")
        self.canvas.pack(pady=10)

        self.raiz = None

        #Insertar
        self.insertar_frame = tk.Frame(master)
        self.insertar_frame.pack(pady=5)
        tk.Label(self.insertar_frame, text="Insertar valor:").pack(side=tk.LEFT)
        self.insertar_entry = tk.Entry(self.insertar_frame)
        self.insertar_entry.pack(side=tk.LEFT)
        tk.Button(self.insertar_frame, text="Insertar", command=self.insertar_valor).pack(side=tk.LEFT, padx=5)

        #Eliminar
        self.eliminar_frame = tk.Frame(master)
        self.eliminar_frame.pack(pady=5)
        tk.Label(self.eliminar_frame, text="Eliminar valor:").pack(side=tk.LEFT)
        self.eliminar_entry_eliminar = tk.Entry(self.eliminar_frame)
        self.eliminar_entry_eliminar.pack(side=tk.LEFT)
        tk.Button(self.eliminar_frame, text="Eliminar", command=self.eliminar_valor).pack(side=tk.LEFT, padx=5)

        self.dibujar_arbol()

    def insertar_valor(self):
        valor_str = self.insertar_entry.get()
        try:
            valor = int(valor_str)
            self.raiz = insertar_avl(self.raiz, valor, self.canvas)
            self.insertar_entry.delete(0, tk.END)
            self.dibujar_arbol()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero.")
    def eliminar_valor(self):
        valor_str = self.eliminar_entry_eliminar.get()
        try:
            valor = int(valor_str)
            self.raiz = eliminar_avl(self.raiz, valor, self.canvas)
            self.eliminar_entry_eliminar.delete(0, tk.END)
            self.dibujar_arbol()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero.")
    def dibujar_arbol(self, nodo=None, x=400, y=50, nivel=100):
        self.canvas.delete("all")
        self._dibujar_nodo(self.raiz, x, y, nivel)

    def _dibujar_nodo(self, nodo, x, y, nivel):
        if nodo:
            radio = 20
            self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="lightblue")
            self.canvas.create_text(x, y, text=str(nodo.valor))
            if nodo.izquierda:
                x_izquierda = x - nivel
                y_izquierda = y + 60
                self.canvas.create_line(x, y + radio, x_izquierda, y_izquierda - radio)
                self._dibujar_nodo(nodo.izquierda, x_izquierda, y_izquierda, nivel * 0.7)
            if nodo.derecha:
                x_derecha = x + nivel
                y_derecha = y + 60
                self.canvas.create_line(x, y + radio, x_derecha, y_derecha - radio)
                self._dibujar_nodo(nodo.derecha, x_derecha, y_derecha, nivel * 0.7)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ArbolAVLGUI(root)
    root.mainloop()
