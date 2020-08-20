
#from Tokencss import *
#from tkinter import messagebox as MessageBox
from enum import Enum


class Tokencss(Enum):
    # selectores
    """ palabras reservadas de html como p, h1, *(universal), ID, clases, pseudoclases div etc...
        reglas con <DIV>...
    """
    # reglas (palabras reservadas), puede tener o no el ';' al final
    # comentarios
    # propiedades
    # delimitadores
    # valores
    # - unidades de medida
    # - ID y numeros
    # - porcentajes
    # - numeros hexadecimales de colores
    # - URL
    # - cadenas

    PROPIEDAD = "Propiedad"
    SELECTOR_UNIVERSAL = "Selector universal"
    SELECTOR_CLASE = "Selector de clase"
    SELECTOR_ID = "Selector de id"
    COMENTARIO = "Comentario"
    UNIDAD_MEDIDA = "Unidad de medida"
    URL = "url"
    PORCENTAJE = "Porcentaje"
    COLOR = "Color"
    CADENA = "Cadena"
    IDENTIFICADOR = "Identificador"
    NUMERO = "Numero"
    URL_ = "Url"
    PUNTO_Y_COMA = "Punto y coma"

    def __init__(self, token):
        super().__init__()

        self.Token = token

    def ObtenerTipoTokenCSS(self):
        return self.Token

#####


class AnalizadorLexicocss():

    def __init__(self):
        super().__init__()

        self.auxLex = ""
        self.listaTokens = []
        self.listaErroresLex = []
        self.salida = ""
        self.estado = 0
        self.fila = 0
        self.columna = 0

    def ClasificarToken(self):
        # Clasificar los tokens de la lista
        pass

    ####################

    def AgregarToken(self, Tokencss):
        #
        #token = Tokencss("ENTRADA", "hola")
        # print(self.listaTokens[:])
        pass

    ####################

    def Escanear(self, entrada):
        # Recorrer texto de entrada
        estado = self.estado
        cadena = ""
        numero = ""
        fila = self.fila
        col = self.columna

        for letra in range(len(entrada)):

            if estado == 0:
                cadena = ""
                print("Estoy en estado 0")
                range(len(entrada) - 1)

                # LEYENDO COMENTARIOS DE UNA O MAS LINEAS
                if entrada[letra] == "/":
                    cadena += entrada[letra]
                    estado = 1
                ##
                elif entrada[letra].isalpha():
                    cadena += entrada[letra]
                    estado = 4
                ##
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    estado = 5
                ##
                elif entrada[letra] == "\"":
                    cadena += entrada[letra]
                    print("Lei una comilla doble")
                    estado = 6
                ##
                elif entrada[letra] == "'":
                    cadena += entrada[letra]
                    print("Lei una comilla simple")
                    estado = 6
                ##
                elif entrada[letra] == "." or entrada[letra] == "#":
                    cadena += entrada[letra]
                    estado = 8
                ##
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    token_ = Tokencss(Tokencss.SELECTOR_UNIVERSAL)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenCSS(), cadena])
                    cadena = ""
                ##
                elif entrada[letra] == ";":
                    cadena += entrada[letra]
                    token_ = Tokencss(Tokencss.PUNTO_Y_COMA)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenCSS(), cadena])
                    cadena = ""
                ##
                elif entrada[letra] == "%":
                    print("Error")
                ##
                elif entrada[letra] == "$":
                    print("Error")
                ## 
                elif entrada[letra] == "\n":
                    print("Salto de linea")
                ##
                elif entrada[letra] == "\t":
                    print("Tabulación")
            ##
            elif estado == 1:
                print("Estoy en estado 1")
                if entrada[letra] == "*":
                    print("lei un asterisco")
                    cadena += entrada[letra]
                    estado = 2
                ##
                elif entrada[letra] == " ":
                    print("lei un espacio")
                    cadena += entrada[letra]
                    estado = 2
                ##

                elif entrada[letra] == "\"":
                    print("Lei comillas dobles")
                    cadena += entrada[letra]
                    estado = 2
                ##
                elif entrada[letra] == "\n":
                    print("Lei un salto de linea")
                    cadena += entrada[letra]
                    estado = 2
                ##
                elif entrada[letra] == "/":
                    print("Lei una diagonal")
                    cadena += entrada[letra]
                    estado = 3
            ##
            elif estado == 2:
                print("Estoy en estado 2")

                # LETRAS Y NUMEROS
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    print("Lei una letra")
                ##
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    print("Lei un numero")
                ##
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    print("Lei un espacio")

                # SIGNOS DE PUNTUACION
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    print("Lei un punto")
                ##
                elif entrada[letra] == ",":
                    cadena += entrada[letra]
                    print("Lei una coma")
                ##
                elif entrada[letra] == ":":
                    cadena += entrada[letra]
                    print("Lei dos puntos")
                ##
                elif entrada[letra] == ";":
                    cadena += entrada[letra]
                    print("Lei punto y coma")

                # SIMBOLOS DE AGRUPACION
                elif entrada[letra] == "(":
                    cadena += entrada[letra]
                    print("Lei parentesis izq")
                ##
                elif entrada[letra] == ")":
                    cadena += entrada[letra]
                    print("Lei parentesis der")
                ##
                elif entrada[letra] == "<":
                    cadena += entrada[letra]
                    print("Lei bracket izq")
                ##
                elif entrada[letra] == ">":
                    cadena += entrada[letra]
                    print("Lei bracket der")
                ##
                elif entrada[letra] == "{":
                    cadena += entrada[letra]
                    print("Lei parentesis izq")
                ##
                elif entrada[letra] == "}":
                    cadena += entrada[letra]
                    print("Lei parentesis der")
                ##
                elif entrada[letra] == "[":
                    cadena += entrada[letra]
                    print("Lei corchete izq")
                ##
                elif entrada[letra] == "]":
                    cadena += entrada[letra]
                    print("Lei corchete der")

                # GUIONES
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    print("Lei un guión")
                ##
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    print("Lei un guion bajo")
                ##

                # OPERADORES
                elif entrada[letra] == "+":
                    cadena += entrada[letra]
                    print("Lei un signo más")
                ##
                elif entrada[letra] == "=":
                    cadena += entrada[letra]
                    print("Lei un signo igual")
                ##

                # SIGNOS DE INTERROGACION/EXCLAMACIÓN
                elif entrada[letra] == "!":
                    cadena += entrada[letra]
                    print("Lei un signo exlamación")
                ##
                elif entrada[letra] == "¡":
                    cadena += entrada[letra]
                    print("Lei un signo exclamación")
                ##
                elif entrada[letra] == "¿":
                    cadena += entrada[letra]
                    print("Lei un signo interrogación")
                ##
                elif entrada[letra] == "?":
                    cadena += entrada[letra]
                    print("Lei un signo interrogación")
                ##

                # SIMBOLOS
                elif entrada[letra] == "@":
                    cadena += entrada[letra]
                    print("Lei un arroba")
                ##
                elif entrada[letra] == "$":
                    cadena += entrada[letra]
                    print("Lei un signo de dolar")
                ##
                elif entrada[letra] == "^":
                    cadena += entrada[letra]
                    print("Lei un signo de potencia")
                ##
                elif entrada[letra] == "%":
                    cadena += entrada[letra]
                    print("Lei un signo de porcentaje")
                ##
                elif entrada[letra] == "&":
                    cadena += entrada[letra]
                    print("Lei un signo aspersand")
                ##
                elif entrada[letra] == "\n":
                    cadena += entrada[letra]
                    print("Lei un salto de linea")
                ##
                elif entrada[letra] == "\t":
                    cadena += entrada[letra]
                    print("Lei una tabulación")
                ##
                elif entrada[letra] == "|":
                    cadena += entrada[letra]
                    print("Lei un pipe")
                ##
                elif entrada[letra] == "°":
                    cadena += entrada[letra]
                    print("Lei una orden")
                ##
                elif entrada[letra] == "¬":
                    cadena += entrada[letra]
                    print("Lei un simbolo raro")
                ##
                elif entrada[letra] == "'":
                    cadena += entrada[letra]
                    print("Lei una comilla simple")
                ##
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    print("Lei un asterisco")
                    estado = 1
            ##
            elif estado == 3:
                # ESTADO DE ACEPTACIÓN
                print(cadena)
                print("Lectura de comentario finalizada")
                token_ = Tokencss(Tokencss.COMENTARIO)
                self.listaTokens.append([token_.ObtenerTipoTokenCSS(), cadena])
                cadena = ""
                estado = 0
            ##
            elif estado == 4:

                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    print("Lei una letra")
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    print("Lei un numero")
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    print("Lei un guion")
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    print("Lei un guion bajo")
                else:  # aceptar el ID o detectar el error lexico
                    # print(cadena)
                    self.AgregarToken(cadena)
                    cadena = ""
                    estado = 0
            ##
            elif estado == 5:
                #numero = ""
                print("estoy en estado 5")
                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                else:

                    token_ = Tokencss(Tokencss.NUMERO)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenCSS(), cadena])
                    numero = ""
                    ##range(len(entrada) - 1)
                    estado = 0
            ##
            elif estado == 6:
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                elif entrada[letra] == "\\":
                    cadena += entrada[letra]
                elif entrada[letra] == "\"" or entrada[letra] == "'":
                    cadena += entrada[letra]
                    estado = 7
            ##
            elif estado == 7:
                token_ = Tokencss(Tokencss.CADENA)
                self.listaTokens.append([token_.ObtenerTipoTokenCSS(), cadena])
                cadena = ""
                estado = 0
            ##
            elif estado == 8:
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                elif entrada[letra] == " ":
                    token_ = Tokencss(Tokencss.SELECTOR_ID)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenCSS(), cadena])
                    cadena = ""
                    estado = 0

    ####################

    def AgregarToken(self, token):

        if token == "h1":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])

        # RECONOCIENDO PROPIEDADES
        elif token == "color":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "border":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "text-align":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "font-weight":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "padding-left":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "padding-top":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "line-height":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "margin-top":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "margin-left":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "display":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "top":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "float":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "min-width":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "background-color":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "Opacity":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "font-family":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "font-size":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "padding-right":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "padding":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "margin-right":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "width":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "margin":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "position":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "right":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "clear":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "max-height":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "background-image":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "font-style":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "font":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "padding-bottom":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "border-style":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "bottom":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "left":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "max-width":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "min-height":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "url":
            token_ = Tokencss(Tokencss.URL_)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])

        ######## VALORES ########
        # Unidades de medida
        elif token == "px":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "em":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "vh":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "background-image":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "background-image":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "vw":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "in":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "cm":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "mm":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "pt":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "pc":
            token_ = Tokencss(Tokencss.UNIDAD_MEDIDA)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        else:
            token_ = Tokencss(Tokencss.SELECTOR_CLASE)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])

    ####################

    def ImprimirListaTokens(self):
        lista = self.listaTokens
        for token in lista:
            print(token)

    ####################

    def GenerarBitcacora(self):
        bitacora = self.salida

        bitacora += "\t :: BITACORA DE RECORRIDO \n"

        bitacora += " >> Recorrido por los estados aceptados"

        bitacora += "\t :: LISTADO DE TOKENS ACEPTADOS: \n"
        for token in self.listaTokens:
            bitacora += token

        bitacora += "\t :: LISTADO DE ERRORES LEXICOS \n"
        # imprimir lista de errores

    ####################
