
import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    def regresaRaiz(self):
        return self.raiz

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
            return True

        return self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
                return True
            return self._insertar(nodo.izquierdo, dato)

        if dato > nodo.dato:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
                return True
            return self._insertar(nodo.derecho, dato)

        return False

    def busqueda(self, dato):
        return self._buscar(self.raiz, dato)

    def buscar(self, dato):
        return self.busqueda(dato)

    def _buscar(self, nodo, dato):
        if nodo is None:
            return None

        if dato == nodo.dato:
            return nodo

        if dato < nodo.dato:
            return self._buscar(nodo.izquierdo, dato)

        return self._buscar(nodo.derecho, dato)

    def preOrden(self):
        resultado = []
        self._preOrden(self.raiz, resultado)
        return resultado

    def _preOrden(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preOrden(nodo.izquierdo, resultado)
            self._preOrden(nodo.derecho, resultado)

    def inOrden(self):
        resultado = []
        self._inOrden(self.raiz, resultado)
        return resultado

    def _inOrden(self, nodo, resultado):
        if nodo is not None:
            self._inOrden(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inOrden(nodo.derecho, resultado)

    def postOrden(self):
        resultado = []
        self._postOrden(self.raiz, resultado)
        return resultado

    def _postOrden(self, nodo, resultado):
        if nodo is not None:
            self._postOrden(nodo.izquierdo, resultado)
            self._postOrden(nodo.derecho, resultado)
            resultado.append(nodo.dato)

    def recorridoNiveles(self):
        resultado = []

        if self.raiz is None:
            return resultado

        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.dato)

            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)

            if nodo.derecho is not None:
                cola.append(nodo.derecho)

        return resultado

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0

        izquierda = self._altura(nodo.izquierdo)
        derecha = self._altura(nodo.derecho)

        return 1 + max(izquierda, derecha)

    def cantidadHojas(self):
        return self._cantidadHojas(self.raiz)

    def _cantidadHojas(self, nodo):
        if nodo is None:
            return 0

        if nodo.izquierdo is None and nodo.derecho is None:
            return 1

        return (
            self._cantidadHojas(nodo.izquierdo)
            + self._cantidadHojas(nodo.derecho)
        )

    def cantidadNodos(self):
        return self._cantidadNodos(self.raiz)

    def _cantidadNodos(self, nodo):
        if nodo is None:
            return 0

        return (
            1
            + self._cantidadNodos(nodo.izquierdo)
            + self._cantidadNodos(nodo.derecho)
        )

    def esLleno(self):
        return self._esLleno(self.raiz)

    def _esLleno(self, nodo):
        if nodo is None:
            return True

        if nodo.izquierdo is None and nodo.derecho is None:
            return True

        if nodo.izquierdo is not None and nodo.derecho is not None:
            return (
                self._esLleno(nodo.izquierdo)
                and self._esLleno(nodo.derecho)
            )

        return False

    def esCompleto(self):
        if self.raiz is None:
            return True

        cola = deque([self.raiz])
        encontradoVacio = False

        while cola:
            nodo = cola.popleft()

            if nodo.izquierdo is not None:
                if encontradoVacio:
                    return False

                cola.append(nodo.izquierdo)
            else:
                encontradoVacio = True

            if nodo.derecho is not None:
                if encontradoVacio:
                    return False

                cola.append(nodo.derecho)
            else:
                encontradoVacio = True

        return True

    def eliminarPredecesor(self, dato):
        eliminado = [False]
        self.raiz = self._eliminarPredecesor(
            self.raiz, dato, eliminado
        )
        return eliminado[0]

    def _eliminarPredecesor(self, nodo, dato, eliminado):
        if nodo is None:
            return None

        if dato < nodo.dato:
            nodo.izquierdo = self._eliminarPredecesor(
                nodo.izquierdo, dato, eliminado
            )

        elif dato > nodo.dato:
            nodo.derecho = self._eliminarPredecesor(
                nodo.derecho, dato, eliminado
            )

        else:
            eliminado[0] = True

            if nodo.izquierdo is None:
                return nodo.derecho

            if nodo.derecho is None:
                return nodo.izquierdo

            anterior = nodo.izquierdo

            while anterior.derecho is not None:
                anterior = anterior.derecho

            nodo.dato = anterior.dato
            nodo.izquierdo = self._eliminarMaximo(
                nodo.izquierdo
            )

        return nodo

    def _eliminarMaximo(self, nodo):
        if nodo.derecho is None:
            return nodo.izquierdo

        nodo.derecho = self._eliminarMaximo(nodo.derecho)
        return nodo

    def eliminarSucesor(self, dato):
        eliminado = [False]
        self.raiz = self._eliminarSucesor(
            self.raiz, dato, eliminado
        )
        return eliminado[0]

    def _eliminarSucesor(self, nodo, dato, eliminado):
        if nodo is None:
            return None

        if dato < nodo.dato:
            nodo.izquierdo = self._eliminarSucesor(
                nodo.izquierdo, dato, eliminado
            )

        elif dato > nodo.dato:
            nodo.derecho = self._eliminarSucesor(
                nodo.derecho, dato, eliminado
            )

        else:
            eliminado[0] = True

            if nodo.izquierdo is None:
                return nodo.derecho

            if nodo.derecho is None:
                return nodo.izquierdo

            siguiente = nodo.derecho

            while siguiente.izquierdo is not None:
                siguiente = siguiente.izquierdo

            nodo.dato = siguiente.dato
            nodo.derecho = self._eliminarMinimo(
                nodo.derecho
            )

        return nodo

    def _eliminarMinimo(self, nodo):
        if nodo.izquierdo is None:
            return nodo.derecho

        nodo.izquierdo = self._eliminarMinimo(nodo.izquierdo)
        return nodo

    def muestraAcostado(self):
        resultado = []
        self._muestraAcostado(self.raiz, 0, resultado)
        return "\n".join(resultado)

    def mostrarAcostado(self):
        return self.muestraAcostado()

    def _muestraAcostado(self, nodo, nivel, resultado):
        if nodo is not None:
            self._muestraAcostado(
                nodo.derecho, nivel + 1, resultado
            )

            resultado.append("    " * nivel + str(nodo.dato))

            self._muestraAcostado(
                nodo.izquierdo, nivel + 1, resultado
            )

    def eliminarArbol(self):
        self.raiz = None

    def graficarArbol(self, canvas, encontrado=None):
        canvas.delete("all")

        if self.raiz is None:
            canvas.create_text(
                300, 150,
                text="El arbol esta vacio",
                font=("Arial", 16)
            )
            canvas.configure(scrollregion=(0, 0, 700, 350))
            return

        posiciones = {}
        contador = [0]

        def calcularPosiciones(nodo, nivel):
            if nodo is None:
                return

            calcularPosiciones(nodo.izquierdo, nivel + 1)

            x = 70 + contador[0] * 90
            y = 60 + nivel * 100

            posiciones[id(nodo)] = (x, y)
            contador[0] += 1

            calcularPosiciones(nodo.derecho, nivel + 1)

        calcularPosiciones(self.raiz, 0)

        ancho = max(700, contador[0] * 90 + 100)
        alto = max(350, self.altura() * 100 + 100)

        canvas.configure(scrollregion=(0, 0, ancho, alto))

        def dibujarLineas(nodo):
            if nodo is None:
                return

            x, y = posiciones[id(nodo)]

            if nodo.izquierdo is not None:
                xi, yi = posiciones[id(nodo.izquierdo)]
                canvas.create_line(
                    x, y, xi, yi,
                    width=2,
                    fill="#555555"
                )
                dibujarLineas(nodo.izquierdo)

            if nodo.derecho is not None:
                xd, yd = posiciones[id(nodo.derecho)]
                canvas.create_line(
                    x, y, xd, yd,
                    width=2,
                    fill="#555555"
                )
                dibujarLineas(nodo.derecho)

        def dibujarNodos(nodo):
            if nodo is None:
                return

            x, y = posiciones[id(nodo)]

            color = "lightblue"

            if nodo.dato == encontrado:
                color = "lightgreen"

            canvas.create_oval(
                x - 23, y - 23,
                x + 23, y + 23,
                fill=color,
                outline="black",
                width=2
            )

            canvas.create_text(
                x, y,
                text=str(nodo.dato),
                font=("Arial", 11, "bold")
            )

            dibujarNodos(nodo.izquierdo)
            dibujarNodos(nodo.derecho)

        dibujarLineas(self.raiz)
        dibujarNodos(self.raiz)


class ArbolApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.arbol = Arbol()
        self.elementoEncontrado = None

        self.ventanaGrafica = None
        self.canvasGrafica = None

        self.ventana.title("Arbol Binario de Busqueda")
        self.ventana.geometry("1150x750")
        self.ventana.minsize(850, 600)

        self.crearInterfaz()

    def crearInterfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="ARBOL BINARIO DE BUSQUEDA",
            font=("Arial", 19, "bold")
        )
        titulo.pack(pady=12)

        marcoPrincipal = tk.Frame(self.ventana)
        marcoPrincipal.pack(
            fill=tk.BOTH,
            expand=True,
            padx=12,
            pady=8
        )

        marcoIzquierdo = tk.Frame(marcoPrincipal)
        marcoIzquierdo.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=5
        )

        marcoDerecho = tk.Frame(marcoPrincipal)
        marcoDerecho.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True,
            padx=5
        )

        tk.Label(
            marcoIzquierdo,
            text="MENU DE OPERACIONES",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        self.opciones = [
            "1. Insertar elemento",
            "2. Mostrar arbol completo acostado",
            "3. Graficar arbol completo",
            "4. Buscar un elemento en el arbol",
            "5. PreOrden",
            "6. InOrden",
            "7. PostOrden",
            "8. Eliminar nodo del arbol PREDECESOR",
            "9. Eliminar nodo del arbol SUCESOR",
            "10. Recorrer por niveles (Amplitud)",
            "11. Altura del arbol",
            "12. Cantidad de hojas",
            "13. Cantidad de nodos",
            "14. Informacion general del arbol",
            "15. Revisa si es un arbol binario completo",
            "16. Revisa si es un arbol binario lleno",
            "17. Eliminar el arbol"
        ]

        self.menu = ttk.Combobox(
            marcoIzquierdo,
            values=self.opciones,
            state="readonly",
            width=43
        )
        self.menu.pack(pady=5)
        self.menu.current(0)

        marcoEntrada = tk.Frame(marcoIzquierdo)
        marcoEntrada.pack(pady=8)

        tk.Label(
            marcoEntrada,
            text="Elemento:",
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=4)

        self.entrada = tk.Entry(
            marcoEntrada,
            width=12,
            font=("Arial", 11)
        )
        self.entrada.pack(side=tk.LEFT, padx=4)

        tk.Button(
            marcoEntrada,
            text="Ejecutar",
            command=self.ejecutar,
            width=11
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            marcoEntrada,
            text="Limpiar salida",
            command=self.limpiarSalida,
            width=13
        ).pack(side=tk.LEFT, padx=4)

        tk.Label(
            marcoIzquierdo,
            text="RESULTADOS",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        marcoTexto = tk.Frame(marcoIzquierdo)
        marcoTexto.pack(fill=tk.BOTH, expand=True)

        scrollTexto = tk.Scrollbar(marcoTexto)
        scrollTexto.pack(side=tk.RIGHT, fill=tk.Y)

        self.salida = tk.Text(
            marcoTexto,
            height=18,
            width=48,
            font=("Consolas", 10),
            wrap=tk.WORD,
            yscrollcommand=scrollTexto.set
        )
        self.salida.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        scrollTexto.config(command=self.salida.yview)

        tk.Label(
            marcoDerecho,
            text="REPRESENTACION DEL ARBOL",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        marcoCanvas = tk.Frame(marcoDerecho)
        marcoCanvas.pack(fill=tk.BOTH, expand=True)

        scrollX = tk.Scrollbar(
            marcoCanvas,
            orient=tk.HORIZONTAL
        )
        scrollX.pack(side=tk.BOTTOM, fill=tk.X)

        scrollY = tk.Scrollbar(
            marcoCanvas,
            orient=tk.VERTICAL
        )
        scrollY.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas = tk.Canvas(
            marcoCanvas,
            background="white",
            xscrollcommand=scrollX.set,
            yscrollcommand=scrollY.set
        )
        self.canvas.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        scrollX.config(command=self.canvas.xview)
        scrollY.config(command=self.canvas.yview)

        self.mostrarMensaje(
            "Bienvenido al programa de arboles binarios.\n"
            "Selecciona una operacion del menu para comenzar."
        )

        self.actualizarGrafica()

    def mostrarMensaje(self, mensaje):
        self.salida.insert(tk.END, str(mensaje) + "\n\n")
        self.salida.see(tk.END)

    def limpiarSalida(self):
        self.salida.delete("1.0", tk.END)

    def obtenerDato(self):
        texto = self.entrada.get().strip()

        if texto == "":
            messagebox.showwarning(
                "Dato requerido",
                "Ingresa un numero."
            )
            return None

        try:
            return int(texto)
        except ValueError:
            messagebox.showerror(
                "Dato incorrecto",
                "Ingresa solamente numeros enteros."
            )
            return None

    def actualizarGrafica(self):
        self.arbol.graficarArbol(
            self.canvas,
            self.elementoEncontrado
        )

        if self.canvasGrafica is not None:
            if self.canvasGrafica.winfo_exists():
                self.arbol.graficarArbol(
                    self.canvasGrafica,
                    self.elementoEncontrado
                )

    def dibujarArbol(self, canvas):
        self.arbol.graficarArbol(
            canvas,
            self.elementoEncontrado
        )

    def graficarVentana(self):
        if (
            self.ventanaGrafica is not None
            and self.ventanaGrafica.winfo_exists()
        ):
            self.ventanaGrafica.lift()
            self.actualizarGrafica()
            return

        self.ventanaGrafica = tk.Toplevel(self.ventana)
        self.ventanaGrafica.title("Grafica del arbol binario")
        self.ventanaGrafica.geometry("850x600")

        tk.Label(
            self.ventanaGrafica,
            text="GRAFICA DEL ARBOL BINARIO",
            font=("Arial", 15, "bold")
        ).pack(pady=10)

        marco = tk.Frame(self.ventanaGrafica)
        marco.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        scrollHorizontal = tk.Scrollbar(
            marco,
            orient=tk.HORIZONTAL
        )
        scrollHorizontal.pack(side=tk.BOTTOM, fill=tk.X)

        scrollVertical = tk.Scrollbar(
            marco,
            orient=tk.VERTICAL
        )
        scrollVertical.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvasGrafica = tk.Canvas(
            marco,
            background="white",
            xscrollcommand=scrollHorizontal.set,
            yscrollcommand=scrollVertical.set
        )
        self.canvasGrafica.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        scrollHorizontal.config(
            command=self.canvasGrafica.xview
        )
        scrollVertical.config(
            command=self.canvasGrafica.yview
        )

        self.actualizarGrafica()

    def mostrarInformacion(self):
        if self.arbol.esVacio():
            self.mostrarMensaje(
                "INFORMACION GENERAL DEL ARBOL\n\n"
                "El arbol esta vacio.\n"
                "Cantidad de nodos: 0\n"
                "Cantidad de hojas: 0\n"
                "Altura: 0"
            )
            return

        completo = "Si" if self.arbol.esCompleto() else "No"
        lleno = "Si" if self.arbol.esLleno() else "No"

        informacion = (
            "INFORMACION GENERAL DEL ARBOL\n\n"
            "Raiz: " + str(self.arbol.regresaRaiz().dato) + "\n"
            "Cantidad de nodos: "
            + str(self.arbol.cantidadNodos()) + "\n"
            "Cantidad de hojas: "
            + str(self.arbol.cantidadHojas()) + "\n"
            "Altura: " + str(self.arbol.altura()) + "\n"
            "Arbol completo: " + completo + "\n"
            "Arbol lleno: " + lleno + "\n\n"
            "Recorrido por niveles:\n"
            + str(self.arbol.recorridoNiveles())
        )

        self.mostrarMensaje(informacion)

    def ejecutar(self):
        seleccion = self.menu.get()

        if not seleccion:
            return

        numero = int(seleccion.split(".")[0])

        if numero in [1, 4, 8, 9]:
            dato = self.obtenerDato()

            if dato is None:
                return

        if numero == 1:
            if self.arbol.insertar(dato):
                self.elementoEncontrado = None
                self.mostrarMensaje(
                    "Elemento " + str(dato)
                    + " insertado correctamente."
                )
                self.actualizarGrafica()
            else:
                self.mostrarMensaje(
                    "El elemento " + str(dato)
                    + " ya existe en el arbol."
                )

        elif numero == 2:
            if self.arbol.esVacio():
                self.mostrarMensaje("El arbol esta vacio.")
            else:
                self.mostrarMensaje(
                    "ARBOL COMPLETO ACOSTADO\n\n"
                    + self.arbol.muestraAcostado()
                )

        elif numero == 3:
            self.graficarVentana()

        elif numero == 4:
            encontrado = self.arbol.busqueda(dato)

            if encontrado is not None:
                self.elementoEncontrado = dato
                self.mostrarMensaje(
                    "El elemento " + str(dato)
                    + " si existe en el arbol."
                )
            else:
                self.elementoEncontrado = None
                self.mostrarMensaje(
                    "El elemento " + str(dato)
                    + " no existe en el arbol."
                )

            self.actualizarGrafica()

        elif numero == 5:
            self.mostrarMensaje(
                "RECORRIDO PREORDEN\n"
                + str(self.arbol.preOrden())
            )

        elif numero == 6:
            self.mostrarMensaje(
                "RECORRIDO INORDEN\n"
                + str(self.arbol.inOrden())
            )

        elif numero == 7:
            self.mostrarMensaje(
                "RECORRIDO POSTORDEN\n"
                + str(self.arbol.postOrden())
            )

        elif numero == 8:
            if self.arbol.eliminarPredecesor(dato):
                self.elementoEncontrado = None
                self.mostrarMensaje(
                    "Elemento " + str(dato)
                    + " eliminado utilizando el predecesor."
                )
                self.actualizarGrafica()
            else:
                self.mostrarMensaje(
                    "El elemento " + str(dato)
                    + " no existe en el arbol."
                )

        elif numero == 9:
            if self.arbol.eliminarSucesor(dato):
                self.elementoEncontrado = None
                self.mostrarMensaje(
                    "Elemento " + str(dato)
                    + " eliminado utilizando el sucesor."
                )
                self.actualizarGrafica()
            else:
                self.mostrarMensaje(
                    "El elemento " + str(dato)
                    + " no existe en el arbol."
                )

        elif numero == 10:
            self.mostrarMensaje(
                "RECORRIDO POR NIVELES (AMPLITUD)\n"
                + str(self.arbol.recorridoNiveles())
            )

        elif numero == 11:
            self.mostrarMensaje(
                "Altura del arbol: "
                + str(self.arbol.altura())
            )

        elif numero == 12:
            self.mostrarMensaje(
                "Cantidad de hojas: "
                + str(self.arbol.cantidadHojas())
            )

        elif numero == 13:
            self.mostrarMensaje(
                "Cantidad de nodos: "
                + str(self.arbol.cantidadNodos())
            )

        elif numero == 14:
            self.mostrarInformacion()

        elif numero == 15:
            if self.arbol.esCompleto():
                self.mostrarMensaje(
                    "El arbol binario SI es completo."
                )
            else:
                self.mostrarMensaje(
                    "El arbol binario NO es completo."
                )

        elif numero == 16:
            if self.arbol.esLleno():
                self.mostrarMensaje(
                    "El arbol binario SI es lleno."
                )
            else:
                self.mostrarMensaje(
                    "El arbol binario NO es lleno."
                )

        elif numero == 17:
            if self.arbol.esVacio():
                self.mostrarMensaje("El arbol ya esta vacio.")
            else:
                respuesta = messagebox.askyesno(
                    "Eliminar arbol",
                    "Estas seguro de que deseas eliminar todo el arbol?"
                )

                if respuesta:
                    self.arbol.eliminarArbol()
                    self.elementoEncontrado = None
                    self.actualizarGrafica()
                    self.mostrarMensaje(
                        "Se elimino todo el arbol correctamente."
                    )


if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = ArbolApp(ventana)
    ventana.mainloop()
