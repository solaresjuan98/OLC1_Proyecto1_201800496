
#from Tokencss import *
#from tkinter import messagebox as MessageBox
from enum import Enum
from io import open


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

    SELECTOR = "Selector HTML"
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
        self.fila = 1
        self.columna = 0

    def ClasificarToken(self):
        # Clasificar los tokens de la lista
        pass

    ####################

    def partirLexNumero(self, lexema):

        print(lexema)
        #aux ="100px"
        #aux = lexema
        subestado = 0
        pre = ""
        final = ""

        try:
            # concatena el pentultimo y ultimo caracter del lexema
            final += lexema[-2]
            final += lexema[-1]
            pre = lexema.replace("px", "")
            # agregar numero
            token_numero = Tokencss(Tokencss.NUMERO)
            self.listaTokens.append([token_numero.ObtenerTipoTokenCSS(), pre])
            self.salida += "   Token de numero aceptado.\n"
            print("TOKEN NUMERO ACEPTADO")

            unidad_medida = Tokencss(Tokencss.UNIDAD_MEDIDA)
            # ACEPTAR UNIDAD DE MEDIDA
            if final == "px":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "em":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "vh":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "em":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "vw":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "in":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "cm":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "mm":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "pt":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            elif final == "pc":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.salida += "   Token de unidad de medida aceptado.\n"
            else:
                # no pasa nada
                pass
            pass
            print(pre)
            print(final)

        except IndexError:
            print("---")

    ####################

    def Escanear(self, entrada):
        # Recorrer texto de entrada
        estado = self.estado
        cadena = ""
        numero = ""
        sufijo = ""
        # fila = self.fila
        # col = self.columna

        for letra in range(len(entrada)):
            """
                Estados de aceptación de tokens:
                estado = 3 (comentario)
                estado = 4 (palabra reservada)
                estado = 5 (Digito y medida)
                estado = 7 (Cadenas de texto, como urls)
                estado = 8 (Selector ID o selector de clase)
            """
            if estado == 0:
                cadena = ""
                #print("Estoy en estado 0")
                self.salida += "Analizador en estado 0\n"
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
                elif entrada[letra] == "(":
                    pass
                ##
                elif entrada[letra] == ")":
                    pass
                ##
                elif entrada[letra] == "{":
                    pass
                ##
                elif entrada[letra] == "}":
                    pass
                ##
                elif entrada[letra] == "[":
                    pass
                ##
                elif entrada[letra] == "]":
                    pass
                ##
                elif entrada[letra] == ",":
                    pass
                ##
                ## ERRORES LÉXICOS
                elif entrada[letra] == "%":
                    print("Error")
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "$":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "@":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "|":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "?":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "¿":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "!":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "¡":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "¬":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "~":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "+":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "´":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "^":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == ">":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "<":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "=":
                    cadena += entrada[letra]
                    self.listaErroresLex.append(cadena)
                    cadena = ""
                    estado = 0
                ##
                elif entrada[letra] == "\n":
                    self.fila += 1
                    print("Salto de linea")
                ##
                elif entrada[letra] == "\t":
                    print("Tabulación")
            ##
            elif estado == 1:
                self.salida += "Analizador en estado 1\n"
                #print("Estoy en estado 1")
                if entrada[letra] == "*":
                    #print("lei un asterisco")
                    cadena += entrada[letra]
                    estado = 2
                ##
                elif entrada[letra] == " ":
                    #print("lei un espacio")
                    cadena += entrada[letra]
                    estado = 2
                ##

                elif entrada[letra] == "\"":
                    #print("Lei comillas dobles")
                    cadena += entrada[letra]
                    estado = 2
                ##
                elif entrada[letra] == "\n":
                    #print("Lei un salto de linea")
                    cadena += entrada[letra]
                    self.fila += 1
                    estado = 2
                ##
                elif entrada[letra] == "/":
                    #print("Lei una diagonal")
                    cadena += entrada[letra]
                    estado = 3
            ##
            elif estado == 2:
                self.salida += "Analizador en estado 2\n"
                #print("Estoy en estado 2")

                # LETRAS Y NUMEROS
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    #print("Lei una letra")
                ##
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    #print("Lei un numero")
                ##
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    #print("Lei un espacio")

                # SIGNOS DE PUNTUACION
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    #print("Lei un punto")
                ##
                elif entrada[letra] == ",":
                    cadena += entrada[letra]
                    #print("Lei una coma")
                ##
                elif entrada[letra] == ":":
                    cadena += entrada[letra]
                    #print("Lei dos puntos")
                ##
                elif entrada[letra] == ";":
                    cadena += entrada[letra]
                    #print("Lei punto y coma")

                # SIMBOLOS DE AGRUPACION
                elif entrada[letra] == "(":
                    cadena += entrada[letra]
                    #print("Lei parentesis izq")
                ##
                elif entrada[letra] == ")":
                    cadena += entrada[letra]
                    #print("Lei parentesis der")
                ##
                elif entrada[letra] == "<":
                    cadena += entrada[letra]
                    #print("Lei bracket izq")
                ##
                elif entrada[letra] == ">":
                    cadena += entrada[letra]
                    #print("Lei bracket der")
                ##
                elif entrada[letra] == "{":
                    cadena += entrada[letra]
                    #print("Lei parentesis izq")
                ##
                elif entrada[letra] == "}":
                    cadena += entrada[letra]
                    #print("Lei parentesis der")
                ##
                elif entrada[letra] == "[":
                    cadena += entrada[letra]
                    #print("Lei corchete izq")
                ##
                elif entrada[letra] == "]":
                    cadena += entrada[letra]
                    #print("Lei corchete der")

                # GUIONES
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    #print("Lei un guión")
                ##
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    #print("Lei un guion bajo")
                ##

                # OPERADORES
                elif entrada[letra] == "+":
                    cadena += entrada[letra]
                    #print("Lei un signo más")
                ##
                elif entrada[letra] == "=":
                    cadena += entrada[letra]
                    #print("Lei un signo igual")
                ##

                # SIGNOS DE INTERROGACION/EXCLAMACIÓN
                elif entrada[letra] == "!":
                    cadena += entrada[letra]
                    #print("Lei un signo exlamación")
                ##
                elif entrada[letra] == "¡":
                    cadena += entrada[letra]
                    #print("Lei un signo exclamación")
                ##
                elif entrada[letra] == "¿":
                    cadena += entrada[letra]
                    #print("Lei un signo interrogación")
                ##
                elif entrada[letra] == "?":
                    cadena += entrada[letra]
                    #print("Lei un signo interrogación")
                ##

                # SIMBOLOS
                elif entrada[letra] == "@":
                    cadena += entrada[letra]
                    #print("Lei un arroba")
                ##
                elif entrada[letra] == "$":
                    cadena += entrada[letra]
                    #print("Lei un signo de dolar")
                ##
                elif entrada[letra] == "^":
                    cadena += entrada[letra]
                    #print("Lei un signo de potencia")
                ##
                elif entrada[letra] == "%":
                    cadena += entrada[letra]
                    #print("Lei un signo de porcentaje")
                ##
                elif entrada[letra] == "&":
                    cadena += entrada[letra]
                    #print("Lei un signo aspersand")
                ##
                elif entrada[letra] == "\n":
                    cadena += entrada[letra]
                    self.fila += 1
                    #print("Lei un salto de linea")
                ##
                elif entrada[letra] == "\t":
                    cadena += entrada[letra]
                    #print("Lei una tabulación")
                ##
                elif entrada[letra] == "|":
                    cadena += entrada[letra]
                    #print("Lei un pipe")
                ##
                elif entrada[letra] == "°":
                    cadena += entrada[letra]
                    #print("Lei una orden")
                ##
                elif entrada[letra] == "¬":
                    cadena += entrada[letra]
                    #print("Lei un simbolo raro")
                ##
                elif entrada[letra] == "'":
                    cadena += entrada[letra]
                    #print("Lei una comilla simple")
                ##
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    #print("Lei un asterisco")
                    estado = 1
            ##
            elif estado == 3:
                self.salida += "Analizador en estado 3\n"
                # ESTADO DE ACEPTACIÓN
                token_ = Tokencss(Tokencss.COMENTARIO)
                self.listaTokens.append([token_.ObtenerTipoTokenCSS(), cadena])
                self.salida += "   Token de tipo comentario aceptado\n"
                cadena = ""
                estado = 0
            ##
            elif estado == 4:
                self.salida += "Analizador en estado 4\n"
                # ESTADO DE ACEPTACIÓN
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
                # declarar prefijo (es la cadena que se esta leyendo) y sufijo
                sufijo = ""
                self.salida += "Analizador en estado 5\n"
                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                elif entrada[letra] == "%":
                    cadena += entrada[letra]
                elif entrada[letra].isalpha():
                    cadena += entrada[letra]
                else:
                    self.partirLexNumero(cadena)
                    range(len(entrada) - 1)
                    estado = 0
            ##
            elif estado == 6:
                self.salida += "Analizador en estado 6\n"
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
                self.salida += "Analizador en estado 7\n"
                token_ = Tokencss(Tokencss.CADENA)
                self.listaTokens.append([token_.ObtenerTipoTokenCSS(), cadena])
                self.salida += "   Token cadena de texto reconocida\n"
                cadena = ""
                estado = 0
            ##
            elif estado == 8:
                self.salida += "Analizador en estado 8\n"
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
                    self.salida += "  Token identificador reconocido \n"
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

    def ImprimirListaErrores(self):
        errores = self.listaErroresLex
        for error in errores:
            print(error)

    ####################

    def GenerarBitacora(self):
        bitacora = self.salida

        print(bitacora)
        return bitacora
        # imprimir lista de errores

    ####################

    def CantidadLineas(self):
        return self.fila

    ####################

    def GenerarReporte(self):
        contador = 1 ## contador del numero de errores
        reporte = open("Reportes/ErroresCSS.html", "w")

        contenido = "<!DOCTYPE html>"\
                    "<html lang=\"en\">"\
                    "<head>"\
                    "<meta charset=\"UTF-8\">"\
                    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"\
                    "<link href=\"https://fonts.googleapis.com/css2?family=Mulish:wght@300&family=Roboto:wght@300;400&display=swap\""\
                    "rel=\"stylesheet\">"\
                    "<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\"/>"\
                    "<link rel=\"stylesheet\" type=\"text/css\" href=\"responsive.css\"/>"\
                    "<title>Reporte</title>"\
                    "</head>"\
                    "<body>"\
                    "<header id=\"header\">"\
                    "<div class=\"center\">"\
                    "<div id=\"logo\">"\
                    "<h2>Reporte de errores</h2>"\
                    "</div>"\
                    "<div class=\"clearfix\"></div>"\
                    "</div>"\
                    "</header>"\
                    "<section id=\"content\">"\
                    "<h2 class=\"subtitle\">Errores encontrados</h2>"\
                    "<div id=\"tasks\">"\
                    "<br><br>"\
                    "<table class=\"card\">"\
                    "<tr>"\
                    "<th>No</th>"\
                    "<th>Linea</th>"\
                    "<th>Columna</th>"\
                    "<th>Descripcion</th>"\
                    "</tr>"\
        
        reporte.write(contenido)

        print()
        contenido2 = ""\
        
        for error in self.listaErroresLex:
            
            print(contador)
            contenido2 = "<tr>"\
                        "<td>"\
                        + str(contador) +\
                        "</td>"\
                        "<td>---</td>"\
                        "<td>---</td>"\
                        "<td>"\
                        + error +\
                        "</td>"\
                        "</tr>"\
                        "\n"
            contador += 1
            reporte.write(contenido2)

                        
        contenido3 = "</table>"\
                     "</div>"\
                     "</section>"\
                     "</body>"\
                     "</html>"\
                     ""\

        
        reporte.write(contenido3)
        reporte.close()




