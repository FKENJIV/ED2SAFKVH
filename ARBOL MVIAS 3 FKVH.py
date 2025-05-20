#Reto Unidad 2 : Arboles M-vias || FERNANDO KENJI VILLARROEL HENZAN - 220030464

import tkinter as tk

class NodoMvias:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def dibujar_arbol(canvas, nodo, x, y, espacio_horizontal, espacio_vertical):
    radio = 20
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="lightblue")
    canvas.create_text(x, y, text=str(nodo.valor))

    num_hijos = len(nodo.hijos)
    if num_hijos > 0:
        ancho_total_hijos = num_hijos * espacio_horizontal
        x_inicio_hijos = x - ancho_total_hijos / 2 + espacio_horizontal / 2
        for i, hijo in enumerate(nodo.hijos):
            x_hijo= x_inicio_hijos + i * espacio_horizontal
            canvas.create_line(x, y + radio, x_hijo, y + espacio_vertical - radio)
            dibujar_arbol(canvas, hijo, x_hijo, y + espacio_vertical, espacio_horizontal *0.5, espacio_vertical)

def crear_arbol_ejemplo():
    raiz = NodoMvias(10)
    nodo2 = NodoMvias(20)
    nodo3 = NodoMvias(30)
    nodo4 = NodoMvias(40)
    nodo5 = NodoMvias(50)
    nodo6 = NodoMvias(60)
    nodo7 = NodoMvias(70)
    nodo8 = NodoMvias(80)
    nodo9 = NodoMvias(90)
    nodo10 = NodoMvias(100)
    nodo11 = NodoMvias(200)
    nodo12 = NodoMvias(300)

    raiz.hijos = [nodo2,nodo3, nodo4]
    nodo2.hijos = [nodo5, nodo6, nodo7]
    nodo3.hijos = [nodo8, nodo9]
    nodo4.hijos = [nodo10, nodo11, nodo12]

    return raiz
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Árbol M-vías")
    canvas_ancho=1000
    canvas_alto= 400
    canvas = tk.Canvas(ventana, width=canvas_ancho, height=canvas_alto, bg="white")
    canvas.pack()

    raiz_arbol= crear_arbol_ejemplo()
    espacio_horizontal_inicial = canvas_ancho/ (len(raiz_arbol.hijos) + 2) if raiz_arbol.hijos else canvas_ancho/ 2
    espacio_vertical = 70
    x_raiz = canvas_ancho/2
    y_raiz = 70

    dibujar_arbol(canvas, raiz_arbol, x_raiz, y_raiz, espacio_horizontal_inicial, espacio_vertical)
    ventana.mainloop()