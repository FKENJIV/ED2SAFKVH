#TAREA UNIDAD 2. ARBOLES M-VIAS || FERNANDO KENJI VILLARROEL HENZAN - 220030464
#Realizar la construcción de la estructura de datos abstracta de una arbol Mvias e implementar sus metodos primitivos getter y setter.

import tkinter as tk
from tkinter import simpledialog, messagebox

class NodoMvias:
    def __init__(self, orden):
        self._orden= orden
        self._claves= []
        self._hijos= []
    def get_orden(self):
        return self._orden
    def get_claves(self):
        return list(self._claves)
    def get_hijos(self):
        return list(self._hijos)
    def get_clave(self, indice):
        if 0 <= indice < len(self._claves):
            return self._claves[indice]
        else:
            return None
    def get_hijo(self, indice):
        if 0 <= indice < len(self._hijos):
            return self._hijos[indice]
        else:
            return None
    def es_hoja(self):
        return not self._hijos
    def esta_lleno(self):
        return len(self._claves) == self._orden - 1
    def set_claves(self, nuevas_claves):
        if len(nuevas_claves) <= self._orden - 1:
            self._claves = list(nuevas_claves)
        else:
            raise ValueError("La cantidad de claves excede el orden del nodo.")
    def set_hijos(self, nuevos_hijos):
        if len(nuevos_hijos) <= self._orden:
            self._hijos = list(nuevos_hijos)
        else:
            raise ValueError("La cantidad de hijos excede el orden del nodo.")
    def insertar_clave(self, clave, indice=None):
        if len(self._claves) < self._orden - 1:
            if indice is None:
                self._claves.append(clave)
                self._claves.sort()
            else:
                self._claves.insert(indice, clave)
        else:
            raise ValueError("El nodo está lleno, no se puede insertar más claves.")
    def insertar_hijo(self, hijo, indice=None):
        if len(self._hijos) < self._orden:
            if indice is None:
                self._hijos.append(hijo)
            else:
                self._hijos.insert(indice, hijo)
        else:
            raise ValueError("El nodo ha alcanzado el número máximo de hijos.")

    def eliminar_clave(self, clave):
        try:
            self._claves.remove(clave)
        except ValueError:
            print(f"La clave {clave} no se encontró en este nodo.")

    def eliminar_hijo(self, hijo):
        try:
            self._hijos.remove(hijo)
        except ValueError:
            print(f"{hijo} no se encontró en este nodo.")

class ArbolMvias:
    def __init__(self, orden, canvas):
        self._orden = orden
        self._raiz = None
        self.canvas = canvas
    def get_orden(self):
        return self._orden
    def get_raiz(self):
        return self._raiz
    def set_raiz(self, nueva_raiz):
        self._raiz = nueva_raiz

    def insertar(self, clave):
        if self._raiz is None:
            self._raiz = NodoMvias(self._orden)
            self._raiz.insertar_clave(clave)
        elif self._raiz.esta_lleno():
            nueva_raiz = NodoMvias(self._orden)
            nueva_raiz.insertar_hijo(self._raiz, 0)
            self._dividir_hijo(nueva_raiz, 0, self._raiz)
            self._insertar_no_lleno(nueva_raiz, clave)
            self._raiz = nueva_raiz
        else:
            self._insertar_no_lleno(self._raiz, clave)
        self.dibujar_arbol()

    def _insertar_no_lleno(self, nodo, clave):
        i = len(nodo.get_claves()) - 1
        if nodo.es_hoja():
            nodo.insertar_clave(clave)
        else:
            while i >= 0 and clave < nodo.get_clave(i):
                i -= 1
            i += 1
            if nodo.get_hijo(i).esta_lleno():
                self._dividir_hijo(nodo, i, nodo.get_hijo(i))
                if clave > nodo.get_clave(i):
                    i += 1
            self._insertar_no_lleno(nodo.get_hijo(i), clave)

    def _dividir_hijo(self, padre, indice_hijo, hijo):
        nuevo_hijo = NodoMvias(self._orden)
        padre.insertar_hijo(nuevo_hijo, indice_hijo + 1)
        padre.insertar_clave(hijo.get_claves()[self._orden // 2 - 1], indice_hijo)
        nuevo_hijo.set_claves(hijo.get_claves()[self._orden // 2:])
        hijo.set_claves(hijo.get_claves()[:self._orden // 2 - 1])

        if not hijo.es_hoja():
            nuevo_hijo.set_hijos(hijo.get_hijos()[self._orden // 2:])
            hijo.set_hijos(hijo.get_hijos()[:self._orden // 2])

    def buscar(self, clave):
        return self._buscar_recursivo(self._raiz, clave)

    def _buscar_recursivo(self, nodo, clave):
        i = 0
        while nodo and i < len(nodo.get_claves()) and clave > nodo.get_clave(i):
            i += 1
        if nodo and i < len(nodo.get_claves()) and clave == nodo.get_clave(i):
            return True
        if nodo and nodo.es_hoja():
            return False
        elif nodo:
            return self._buscar_recursivo(nodo.get_hijo(i), clave)
        return False

    def dibujar_arbol(self):
        self.canvas.delete("all")
        if self._raiz:
            self._dibujar_nodo(self._raiz, 400, 50, 200) # Ajustar coordenadas iniciales y espacio

    def _dibujar_nodo(self, nodo, x, y, espacio_horizontal):
        radio = 20
        num_claves = len(nodo.get_claves())
        ancho_total_claves = num_claves* (2 * radio + 10) # Radio + espacio entre claves
        x_inicio = x - ancho_total_claves/ 2
        for i, clave in enumerate(nodo.get_claves()):
            x_clave = x_inicio + i * (2* radio + 10) + radio
            self.canvas.create_oval(x_clave- radio, y - radio, x_clave + radio, y + radio, fill="lightblue")
            self.canvas.create_text(x_clave, y, text=str(clave))
        num_hijos = len(nodo.get_hijos())
        if num_hijos > 0:
            espacio_entre_hijos = espacio_horizontal/ num_hijos
            for i, hijo in enumerate(nodo.get_hijos()):
                x_hijo= x - espacio_horizontal/ 2 + (i + 0.5) * espacio_entre_hijos
                y_hijo= y + 70
                # Conectar al primer clave del hijo (simplificación)
                x_clave_padre = x_inicio + (len(nodo.get_claves()) // 2) * (2 * radio + 10) + radio
                self.canvas.create_line(x_clave_padre, y + radio, x_hijo, y_hijo - radio)
                self._dibujar_nodo(hijo, x_hijo, y_hijo, espacio_horizontal / (self._orden - 1)) # Reducir espacio

class ArbolMviasGUI:
    def __init__(self, orden):
        self.orden= orden
        self.ventana= tk.Tk()
        self.ventana.title("Visualización de Árbol M-vías")
        self.canvas_ancho= 800
        self.canvas_alto= 600
        self.canvas= tk.Canvas(self.ventana, width=self.canvas_ancho, height=self.canvas_alto, bg="white")
        self.canvas.pack(pady=10)
        self.arbol_mvias= ArbolMvias(self.orden, self.canvas)
        self.insertar_frame= tk.Frame(self.ventana)
        self.insertar_frame.pack(pady=5)
        self.insertar_label= tk.Label(self.insertar_frame, text="Insertar clave:")
        self.insertar_label.pack(side=tk.LEFT)
        self.insertar_entry= tk.Entry(self.insertar_frame)
        self.insertar_entry.pack(side=tk.LEFT)
        self.insertar_button= tk.Button(self.insertar_frame, text="Insertar", command=self.insertar_clave_gui)
        self.insertar_button.pack(side=tk.LEFT, padx=5)

    def insertar_clave_gui(self):
        clave_str = self.insertar_entry.get()
        try:
            clave= int(clave_str)
            self.arbol_mvias.insertar(clave)
            self.insertar_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero.")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    orden_del_arbol = 3
    gui = ArbolMviasGUI(orden_del_arbol)
    gui.run()