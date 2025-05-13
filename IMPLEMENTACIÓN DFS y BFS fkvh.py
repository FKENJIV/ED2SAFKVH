# Tarea : Realizar la implemetacion de los metodos sobre ABB || FERNANDO KENJI VILLARROEL HENZAN - 220030464
import tkinter as tk
from tkinter import simpledialog, messagebox
from collections import deque  # búsqueda BFS

class NodoArbol:
    def __init__(self, valor):
        self.valor=valor
        self.izquierda= None
        self.derecha= None
class ArbolBinario:
    def __init__(self):
        self.raiz = None
    def EsVacio(self):
        return self.raiz is None
    def EsHoja(self, nodo):
        return nodo is not None and nodo.izquierda is None and nodo.derecha is None
    def InsertarNodo(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    def _insertar_recursivo(self, nodo_actual,valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda,valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)
    def BuscarX(self, valor):
        return self._buscar_recursivo_con_recorrido(self.raiz,valor, [])
    def _buscar_recursivo_con_recorrido(self, nodo_actual, valor,recorrido):
        if nodo_actual is None:
            return False, "VALOR NO ENCONTRADO", recorrido
        recorrido = recorrido + [nodo_actual.valor]
        if valor == nodo_actual.valor:
            return True, "VALOR ENCONTRADO", recorrido
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo_con_recorrido(nodo_actual.izquierda, valor, recorrido)
        else:
            return self._buscar_recursivo_con_recorrido(nodo_actual.derecha, valor, recorrido)
    def InOrden(self):
        resultado = []
        self._inorden_recursivo(self.raiz,resultado)
        return resultado
    def _inorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierda, resultado)
            resultado.append(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecha, resultado)
    def PreOrden(self):
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            resultado.append(nodo_actual.valor)
            self._preorden_recursivo(nodo_actual.izquierda, resultado)
            self._preorden_recursivo(nodo_actual.derecha, resultado)

    def PostOrden(self):
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            self._postorden_recursivo(nodo_actual.izquierda, resultado)
            self._postorden_recursivo(nodo_actual.derecha, resultado)
            resultado.append(nodo_actual.valor)

    def DFS(self, valor):
        """Búsqueda en profundidad (Depth-First Search) para encontrar un valor."""
        return self._dfs_recursivo(self.raiz, valor, [])

    def _dfs_recursivo(self, nodo_actual, valor, recorrido):
        if nodo_actual is None:
            return False, "VALOR NO ENCONTRADO(DFS)",recorrido
        recorrido = recorrido + [nodo_actual.valor]
        if nodo_actual.valor == valor:
            return True, "VALOR ENCONTRADO(DFS)", recorrido
        #izquierda (una de las posibles estrategias DFS)
        resultado_izquierda, mensaje_izquierda, recorrido_izquierda = self._dfs_recursivo(nodo_actual.izquierda, valor, list(recorrido)) # Pasar una copia del recorrido
        if resultado_izquierda:
            return resultado_izquierda, mensaje_izquierda, recorrido_izquierda
        resultado_derecha, mensaje_derecha, recorrido_derecha = self._dfs_recursivo(nodo_actual.derecha, valor, list(recorrido)) # Pasar una copia del recorrido
        return resultado_derecha, mensaje_derecha, recorrido_derecha
    def BFS(self, valor):
        """busqueda en anchura (Breadth-First Search) para encontrar un valor."""
        if self.raiz is None:
            return False, "Árbol vacío (BFS)", []
        cola = deque([(self.raiz, [self.raiz.valor])]) # Almacenamos el nodo y su recorrido
        visitados = {self.raiz}

        while cola:
            nodo_actual, recorrido = cola.popleft()

            if nodo_actual.valor == valor:
                return True, "VALOR ENCONTRADO (BFS)", recorrido

            if nodo_actual.izquierda and nodo_actual.izquierda not in visitados:
                visitados.add(nodo_actual.izquierda)
                cola.append((nodo_actual.izquierda, recorrido + [nodo_actual.izquierda.valor]))

            if nodo_actual.derecha and nodo_actual.derecha not in visitados:
                visitados.add(nodo_actual.derecha)
                cola.append((nodo_actual.derecha, recorrido + [nodo_actual.derecha.valor]))

        return False, "VALOR NO ENCNTRADO (BFS)", [nodo.valor for nodo in visitados] # Devolvemos los visitados si no se encuentra

class ArbolBinarioApp:
    def __init__(self, master):
        self.master = master
        master.title("Visualización de Árbol Binario con Búsquedas")

        self.arbol = ArbolBinario()
        self._inicializar_arbol()

        self.label_recorridos = tk.Label(master, text="Recorridos del Árbol:")
        self.label_recorridos.pack()

        self.label_inorden = tk.Label(master, text=f"In-Orden: {self.arbol.InOrden()}")
        self.label_inorden.pack()

        self.label_preorden = tk.Label(master, text=f"Pre-Orden: {self.arbol.PreOrden()}")
        self.label_preorden.pack()

        self.label_postorden = tk.Label(master, text=f"Post-Orden: {self.arbol.PostOrden()}")
        self.label_postorden.pack()

        self.btn_buscar_dfs = tk.Button(master, text="Buscar (DFS) Valor (1-100)", command=self.buscar_dfs_numero)
        self.btn_buscar_dfs.pack(pady=5)

        self.label_resultado_dfs = tk.Label(master, text="")
        self.label_resultado_dfs.pack()

        self.btn_buscar_bfs = tk.Button(master, text="Buscar (BFS) Valor (1-100)", command=self.buscar_bfs_numero)
        self.btn_buscar_bfs.pack(pady=5)

        self.label_resultado_bfs = tk.Label(master, text="")
        self.label_resultado_bfs.pack()

    def _inicializar_arbol(self):
        """Iniciar el árbol con algunos valores de ejemplo."""
        self.arbol.InsertarNodo(50)
        self.arbol.InsertarNodo(30)
        self.arbol.InsertarNodo(70)
        self.arbol.InsertarNodo(20)
        self.arbol.InsertarNodo(25)
        self.arbol.InsertarNodo(35)
        self.arbol.InsertarNodo(40)
        self.arbol.InsertarNodo(45)
        self.arbol.InsertarNodo(60)
        self.arbol.InsertarNodo(80)
        self.arbol.InsertarNodo(15)
        self.arbol.InsertarNodo(35)
        self.arbol.InsertarNodo(65)
        self.arbol.InsertarNodo(85)
        self.arbol.InsertarNodo(100)

    def buscar_dfs_numero(self):
        """Abre un diálogo para que el usuario ingrese un número y muestra el recorrido DFS."""
        numero_str = simpledialog.askstring("Buscar (DFS) Número", "Ingrese un número entre 1 y 100:")
        if numero_str:
            try:
                numero = int(numero_str)
                if 1 <= numero <= 100:
                    encontrado, mensaje, recorrido = self.arbol.DFS(numero)
                    resultado_texto = f"Búsqueda (DFS) de {numero}: {mensaje}\nRecorrido: {recorrido}"
                    self.label_resultado_dfs.config(text=resultado_texto)
                else:
                    messagebox.showerror("Error", "Por favor, ingrese un número entre 1 y 100.")
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido.")

    def buscar_bfs_numero(self):
        """Abre un diálogo para que el usuario ingrese un número y muestra el recorrido BFS."""
        numero_str = simpledialog.askstring("Buscar (BFS) Número", "Ingrese un número entre 1 y 100:")
        if numero_str:
            try:
                numero = int(numero_str)
                if 1 <= numero <= 100:
                    encontrado, mensaje, recorrido = self.arbol.BFS(numero)
                    resultado_texto = f"Búsqueda (BFS) de {numero}: {mensaje}\nRecorrido: {recorrido}"
                    self.label_resultado_bfs.config(text=resultado_texto)
                else:
                    messagebox.showerror("ERROR", "Por favor, ingrese un número entre 1 y 100.")
            except ValueError:
                messagebox.showerror("ERROR", "Por favor, ingrese un número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArbolBinarioApp(root)
    root.mainloop()