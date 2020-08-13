from tkinter import *
#from tkinter import messasebox as MessageBox
from io import open


ventana = Tk()
ventana.title("OLC PROYECTO 1 - 201800496")
ventana.resizable(False, False)

# insertar frame
miFrame = Frame(ventana, width=950, height=600, bg="#292D3E")
miFrame.pack()

### BARRA DE MENÚ

# insetar barra de menu
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu)

filemenu = Menu(barraMenu)
filemenu = Menu(barraMenu, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
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


### COMPONENTES QUE VAN DENTRO DEL FRAME
labelTitulo = Label(ventana, text="Editor de texto")
labelTitulo.place(x=10, y =10)
labelTitulo.config(padx=5, pady=5, font=("sans-serif", 10))

textoEntrada = Text(ventana)
textoEntrada.place(x=10, y=60)
textoEntrada.config(width=65, height=35, font=("Consolas", 9),
    padx=5, pady=5)


textoSalida = Text(ventana)
textoSalida.place(x=505, y=60)
textoSalida.config(width=60, height=35, font=("Consolas", 9),
    padx=5, pady=5)

ventana.mainloop()
