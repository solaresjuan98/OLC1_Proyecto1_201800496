
#from Tokencss import *
#from tkinter import messagebox as MessageBox

class AnalizadorLexicocss():

    def __init__(self):
        super().__init__()

        self.auxLex = ""
        self.listaTokens = []
        self.estado = 0

    def ClasificarToken(self):
        # Clasificar los tokens de la lista
        pass

    def AgregarToken(self, Tokencss):
        #
        #token = Tokencss("ENTRADA", "hola")
        # print(self.listaTokens[:])
        pass

    def Escanear(self, entrada):
        # Recorrer texto de entrada
        estado = self.estado
        char = ""

        for letra in range(len(entrada)):

            if estado == 0:
                print("Estoy en estado 0")
                range(len(entrada) - 1)

                # LEYENDO COMENTARIOS DE UNA O MAS LINEAS
                if entrada[letra] == "/":
                    char += entrada[letra]
                    estado = 1
                ##
                elif entrada[letra].isalpha():
                    char += entrada[letra]
                    estado = 4
                ##

            ##
            elif estado == 1:
                print("Estoy en estado 1")
                if entrada[letra] == "*":
                    print("lei un asterisco")
                    char += entrada[letra]
                    estado = 2
                ##
                elif entrada[letra] == " ":
                    print("lei un espacio")
                    char += entrada[letra]
                    estado = 2
                ##

                elif entrada[letra] == "\"":
                    print("Lei comillas dobles")
                    char += entrada[letra]
                    estado = 2
                ##
                elif entrada[letra] == "\n":
                    print("Lei un salto de linea")
                    char += entrada[letra]
                    estado = 2
                ##
                elif entrada[letra] == "/":
                    print("Lei una diagonal")
                    char += entrada[letra]
                    estado = 3
            ##
            elif estado == 2:
                print("Estoy en estado 2")

                # LETRAS Y NUMEROS
                if entrada[letra].isalpha():
                    char += entrada[letra]
                    print("Lei una letra")
                ##
                elif entrada[letra].isdigit():
                    char += entrada[letra]
                    print("Lei un numero")
                ##
                elif entrada[letra] == " ":
                    char += entrada[letra]
                    print("Lei un espacio")

                # SIGNOS DE PUNTUACION
                elif entrada[letra] == ".":
                    char += entrada[letra]
                    print("Lei un punto")
                ##
                elif entrada[letra] == ",":
                    char += entrada[letra]
                    print("Lei una coma")
                ##
                elif entrada[letra] == ":":
                    char += entrada[letra]
                    print("Lei dos puntos")
                ##
                elif entrada[letra] == ";":
                    char += entrada[letra]
                    print("Lei punto y coma")

                # SIMBOLOS DE AGRUPACION
                elif entrada[letra] == "(":
                    char += entrada[letra]
                    print("Lei parentesis izq")
                ##
                elif entrada[letra] == ")":
                    char += entrada[letra]
                    print("Lei parentesis der")
                ##
                elif entrada[letra] == "<":
                    char += entrada[letra]
                    print("Lei bracket izq")
                ##
                elif entrada[letra] == ">":
                    char += entrada[letra]
                    print("Lei bracket der")
                ##
                elif entrada[letra] == "{":
                    char += entrada[letra]
                    print("Lei parentesis izq")
                ##
                elif entrada[letra] == "}":
                    char += entrada[letra]
                    print("Lei parentesis der")
                ##
                elif entrada[letra] == "[":
                    char += entrada[letra]
                    print("Lei corchete izq")
                ##
                elif entrada[letra] == "]":
                    char += entrada[letra]
                    print("Lei corchete der")

                # GUIONES
                elif entrada[letra] == "-":
                    char += entrada[letra]
                    print("Lei un guión")
                ##
                elif entrada[letra] == "_":
                    char += entrada[letra]
                    print("Lei un guion bajo")
                ##

                # OPERADORES
                elif entrada[letra] == "+":
                    char += entrada[letra]
                    print("Lei un signo más")
                ##
                elif entrada[letra] == "=":
                    char += entrada[letra]
                    print("Lei un signo igual")
                ##

                # SIGNOS DE INTERROGACION/EXCLAMACIÓN
                elif entrada[letra] == "!":
                    char += entrada[letra]
                    print("Lei un signo exlamación")
                ##
                elif entrada[letra] == "¡":
                    char += entrada[letra]
                    print("Lei un signo exclamación")
                ##
                elif entrada[letra] == "¿":
                    char += entrada[letra]
                    print("Lei un signo interrogación")
                ##
                elif entrada[letra] == "?":
                    char += entrada[letra]
                    print("Lei un signo interrogación")
                ##

                # SIMBOLOS
                elif entrada[letra] == "@":
                    char += entrada[letra]
                    print("Lei un arroba")
                ##
                elif entrada[letra] == "$":
                    char += entrada[letra]
                    print("Lei un signo de dolar")
                ##
                elif entrada[letra] == "^":
                    char += entrada[letra]
                    print("Lei un signo de potencia")
                ##
                elif entrada[letra] == "%":
                    char += entrada[letra]
                    print("Lei un signo de porcentaje")
                ##
                elif entrada[letra] == "&":
                    char += entrada[letra]
                    print("Lei un signo aspersand")
                ##
                elif entrada[letra] == "\n":
                    char += entrada[letra]
                    print("Lei un salto de linea")
                ##
                elif entrada[letra] == "\t":
                    char += entrada[letra]
                    print("Lei una tabulación")
                ##
                elif entrada[letra] == "|":
                    char += entrada[letra]
                    print("Lei un pipe")
                ##
                elif entrada[letra] == "°":
                    char += entrada[letra]
                    print("Lei una orden")
                ##
                elif entrada[letra] == "¬":
                    char += entrada[letra]
                    print("Lei un simbolo raro")
                ##
                elif entrada[letra] == "'":
                    char += entrada[letra]
                    print("Lei una comilla simple")
                ##
                elif entrada[letra] == "*":
                    char += entrada[letra]
                    print("Lei un asterisco")
                    estado = 1
            ##
            elif estado == 3:
                # ESTADO DE ACEPTACIÓN
                self.listaTokens.append(char)
                print(char)
                print("Lectura de comentario finalizada")
                char = ""
                estado = 0
            ##
            elif estado == 4:

                if entrada[letra].isalpha():
                    char += entrada[letra]
                    print("Lei una letra")
                elif entrada[letra].isdigit():
                    char += entrada[letra]
                    print("Lei un numero")
                elif entrada[letra] == "-":
                    char += entrada[letra]
                    print("Lei un guion")
                elif entrada[letra] == "_":
                    char += entrada[letra]
                    print("")
                else: #aceptar el ID o detectar el error lexico
                    self.listaTokens.append(char)
                    print(char)
                    print("Lectura de ID finalizada")
                    char = ""
                    estado = 0
