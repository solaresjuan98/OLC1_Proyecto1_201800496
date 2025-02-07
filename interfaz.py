# Librerias de python
from tkinter import *
from tkinter import messagebox as MessageBox
from io import open
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import os
import re

# Analizadores lexicos
from Analizadores.AnalizadorLexicocss import *
from Analizadores.AnalizadorLexicoJS import *
from Analizadores.AnalizadorLexicohtml import *
from Analizadores.Lexrmt import *

# Analizador sintactico de expresiones
from Analizadores.Sintactico import *

textoArchivo = ""
bitacora = ""


def abrirArchivo():
    # ABRIENDO ARCHIVO
    filename = filedialog.askopenfilename(
        initialdir="C://Users//jsola//Desktop", title="Seleccionar archivo",
        filetypes=(("archivos javascript", "*.js"), ("archivos HTML", "*.html"), ("archivos CSS", "*.css"), ("archivos rmt", "*.rmt")))
    # imprime la ruta
    ruta = filename
    # print(filename)
    split_ = os.path.splitext(filename)
    #print("Extensión del archivo '% s': " %filename, split_[1], "\n")
    extension = split_[1]
    labelFormato.config(text=extension)
    try:
        with open(filename, 'r') as UseFile:
            textoArchivo = UseFile.read()
            textoEntrada.insert(INSERT, textoArchivo)
            # print(UseFile.read())

    except:
        print("El archivo no existe.")

#######################


def limpiarCajaTexto():
    textoEntrada.delete('1.0', END)
    textoSalida.delete('1.0', END)

#######################

def analizarEntrada():
    # atrapa la extensión del archivo
    ext = labelFormato['text']

    if ext == ".js":

        entrada = textoEntrada.get("1.0", "end-1c")
        MessageBox.showinfo(
            "Aviso", "Analisis del archivo JavaScript iniciado")
        analizadorJS = AnalizadorLexicoJS()
        analizadorJS.Escanear(entrada)
        print("\n\n")
        analizadorJS.ImprimirListaTokens()
        analizadorJS.GenerarReporte()
        analizadorJS.GenerarSalida()
        tokens = analizadorJS.ImprimirListaTokens()
        textoSalida.insert(INSERT, "\t :: LISTADO DE TOKENS :: \n")
        textoSalida.insert(INSERT, tokens)
        print(analizadorJS.fila)

    elif ext == ".css":

        entrada = textoEntrada.get("1.0", "end-1c")
        MessageBox.showinfo("Aviso", "Analisis del archivo CSS iniciado.")
        analizadorCSS = AnalizadorLexicocss()
        analizadorCSS.Escanear(entrada)
        analizadorCSS.ImprimirListaTokens()
        analizadorCSS.ImprimirListaErrores()
        analizadorCSS.GenerarReporte()
        bitacora = analizadorCSS.GenerarBitacora()
        analizadorCSS.GenerarArchivoSalida()
        textoSalida.insert(INSERT, bitacora)
        # print(bitacora)
        print(analizadorCSS.fila)

    elif ext == ".html":

        entrada = textoEntrada.get("1.0", "end-1c")
        MessageBox.showinfo("Aviso", "Analisis del archivo HTML iniciado")
        analizadorHTML = AnalizadorLexicohtml()
        analizadorHTML.Escanear(entrada)
        tokensHTML = analizadorHTML.imprimirListaTokens()
        textoSalida.insert(INSERT, "\t :: LISTADO DE TOKENS :: \n")
        textoSalida.insert(INSERT, tokensHTML)
        analizadorHTML.GenerarReporteErrores()
        analizadorHTML.GenerarSalida()
        print(analizadorHTML.fila)

    elif ext == ".rmt":

        entrada = textoEntrada.get("1.0", "end-1c")
        MessageBox.showinfo("Aviso", "Analisis del archivo rmt iniciado")
        analizadorRMT = Lexrmt()
        analizadorRMT.Escanear(entrada)
        analizadorRMT.imprimirExpresiones()
        # Iniciar analisis sintactico
        sintactico = Sintactico()
        sintactico.Parse(analizadorRMT.listaExpr)
        # print(sintactico.pilaVacia())
        resultadoSintactico = sintactico.mostrarReporte()
        textoSalida.insert(INSERT, resultadoSintactico)
        sintactico.GenerarReporteErrores()
        #sintactico = AnalizadorSintactico()
        # sintactico.Parsear(analizadorRMT.ListaTokens)

    else:
        print("Formato no permitido / archivo no cargado")

#######################

def guardarArchivo():

    archivos = [('Archivos Javascript', '*.js'), ('Archivos CSS', '*.css'),
                ('Archivos HTML', '*.html'), ('Archivos rmt', '*.rmt')]

    archivo = asksaveasfile(mode='w', filetypes=archivos,
                            defaultextension=archivos)
    archivoDestino = textoEntrada.get(1.0, END)
    archivo.write(archivoDestino)
    archivo.close()

#######################

def colorearJS():
    pass

#######################


ventana = Tk()
ventana.title("OLC PROYECTO 1 - 201800496")
ventana.resizable(False, False)

# insertar frame
miFrame = Frame(ventana, width=950, height=600, bg="#292D3E")
miFrame.pack()

# BARRA DE MENÚ
# insetar barra de menu
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu)

filemenu = Menu(barraMenu)
filemenu = Menu(barraMenu, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir", command=abrirArchivo)
filemenu.add_command(label="Guardar", command=guardarArchivo)
filemenu.add_separator()
filemenu.add_command(label="Salir")

analizar = Menu(barraMenu)
analizar = Menu(barraMenu, tearoff=0)
analizar.add_command(label="Ejecutar análisis")

reportes = Menu(barraMenu)
reportes = Menu(barraMenu, tearoff=0)
reportes.add_command(label="Ver reportes")

# titulos de las pestañas de la barra de menu
barraMenu.add_cascade(label="Archivo", menu=filemenu)
barraMenu.add_cascade(label="Analizar", menu=analizar)
barraMenu.add_cascade(label="Reportes", menu=reportes)


# COMPONENTES QUE VAN DENTRO DEL FRAME
labelTitulo = Label(ventana, text="Editor de texto")
labelTitulo.place(x=10, y=10)
labelTitulo.config(padx=5, pady=5, font=("sans-serif", 10))

labelFormato = Label(ventana, text="")
labelFormato.place(x=120, y=10)
labelFormato.config(padx=5, pady=5, font=("sans-serif", 10))

# scroll bar1
scrollbar1 = Scrollbar(ventana)
scrollbar1.pack(side=RIGHT, fill=Y)

# CAJA TEXTO ENTRADA
textoEntrada = Text(ventana)
textoEntrada.place(x=10, y=60)
textoEntrada.insert(INSERT, textoArchivo)
textoEntrada.config(width=65, height=35, font=("Consolas", 9),
                    padx=5, pady=5, yscrollcommand=scrollbar1.set)
scrollbar1.config(command=textoEntrada.yview)


# scroll bar1
scrollbar2 = Scrollbar(ventana)
scrollbar2.pack(side=RIGHT, fill=Y)

# CAJA TEXTO QUE MUESTRA LA SALIDA
textoSalida = Text(ventana)
textoSalida.place(x=505, y=60)
textoSalida.config(width=60, height=35, font=("Consolas", 9),
                   padx=5, pady=5, yscrollcommand=scrollbar2.set)
scrollbar2.config(command=textoSalida.yview)


# BOTONES
botonAnalizar = Button(ventana, text="Analizar")
botonAnalizar.place(x=780, y=10)
botonAnalizar.config(padx=3, pady=3, font=(
    "sans-serif", 10), command=analizarEntrada)

botonBorrar = Button(ventana, text="Borrar")
botonBorrar.place(x=850, y=10)
botonBorrar.config(padx=3, pady=3, font=(
    "sans-serif", 10), command=limpiarCajaTexto)


ventana.mainloop()
