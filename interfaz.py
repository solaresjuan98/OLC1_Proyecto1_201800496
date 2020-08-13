from tkinter import *
#from tkinter import messasebox as MessageBox
from io import open
from tkinter import filedialog
import os

# función para abrir archivo de texto

textoArchivo = ""


def abrirArchivo():
    # ABRIENDO ARCHIVO
    filename = filedialog.askopenfilename(
        initialdir="c://", title="Seleccionar archivo",
        filetypes=(("archivos javascript", "*.js"), ("archivos HTML", "*.html"), ("archivos CSS", "*.css")))
    # imprime la ruta
    ruta = filename
    # print(filename)
    split_ = os.path.splitext(filename)
    #print("Extensión del archivo '% s': " %filename, split_[1], "\n")
    extension = split_[1]
    # print(extension)

    try:
        with open(filename, 'r') as UseFile:
            textoArchivo = UseFile.read()
            textoEntrada.insert(INSERT, textoArchivo)
            # print(UseFile.read())

    except:
        print("El archivo no existe.")

def limpiarCajaTexto():
    textoEntrada.delete('1.0', END)

def analizarEntrada(entrada, extension):
    pass

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
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Guardar como...")
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

textoEntrada = Text(ventana)
textoEntrada.place(x=10, y=60)
textoEntrada.config(width=65, height=35, font=("Consolas", 9),
                    padx=5, pady=5)
textoEntrada.insert(INSERT, textoArchivo)

textoSalida = Text(ventana)
textoSalida.place(x=505, y=60)
textoSalida.config(width=60, height=35, font=("Consolas", 9),
                   padx=5, pady=5, state=DISABLED)


# BOTONES

botonAnalizar = Button(ventana, text="Analizar")
botonAnalizar.place(x=780, y=10)
botonAnalizar.config(padx=3, pady=3, font=(
    "sans-serif", 10))

botonBorrar = Button(ventana, text="Borrar")
botonBorrar.place(x=850, y=10)
botonBorrar.config(padx=3, pady=3, font=(
    "sans-serif", 10), command=limpiarCajaTexto)


ventana.mainloop()
