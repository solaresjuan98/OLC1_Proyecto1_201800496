
#from Tokencss import *
#from tkinter import messagebox as MessageBox
from enum import Enum
from io import open
import os


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

    SELECTOR = "Selector"
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
    PAR_IZQ = "Parentesis izq"
    PAR_DER = "Parentesis der"
    LLAVE_IZQ = "Llave izq"
    LLAVE_DER = "Llave der"

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
        self.bitacora = ""
        self.salida = ""  # archivo limpiado
        self.estado = 0
        self.fila = 1
        self.columna = 1
        # ruta del archivo donde estará la salida
        self.dir_salida = ""
        self.banderaArchivo = False

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
            self.bitacora += "   Token de numero aceptado.\n"
            print("TOKEN NUMERO ACEPTADO")

            unidad_medida = Tokencss(Tokencss.UNIDAD_MEDIDA)
            # ACEPTAR UNIDAD DE MEDIDA
            if final == "px":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "em":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "vh":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "em":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "vw":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "in":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "cm":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "mm":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "pt":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
            elif final == "pc":
                self.listaTokens.append(
                    [unidad_medida.ObtenerTipoTokenCSS(), final])
                self.bitacora += "   Token de unidad de medida aceptado.\n"
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

        for letra in range(len(entrada)):
            """
                Estados de aceptación de tokens CSS:
                estado = 3 (comentario)
                estado = 4 (palabra reservada)
                estado = 5 (Digito y medida)
                estado = 7 (Cadenas de texto, como urls)
                estado = 8 (Selector ID o selector de clase)
            """
            
            if estado == 0:
                cadena = ""
                #print("Estoy en estado 0")
                self.bitacora += "Estado q0, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                range(len(entrada) - 1)

                # LEYENDO COMENTARIOS DE UNA O MAS LINEAS
                if entrada[letra] == "/":
                    #cadena += entrada[letra]
                    self.columna += 1
                    self.bitacora += "q0 -> q1 \n"
                    self.salida += entrada[letra]
                    estado = 1
                ##
                elif entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.columna += 1
                    self.bitacora += "q0 -> q4 \n"
                    self.salida += entrada[letra]
                    estado = 4
                ##
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.columna += 1
                    self.bitacora += "q0 -> q5 \n"
                    self.salida += entrada[letra]
                    estado = 5
                ##
                elif entrada[letra] == "\"":
                    cadena += entrada[letra]
                    self.columna += 1
                    print("Lei una comilla doble")
                    self.bitacora += "q0 -> q6 \n"
                    self.salida += entrada[letra]
                    estado = 6
                ##
                elif entrada[letra] == "'":
                    cadena += entrada[letra]
                    self.columna += 1
                    print("Lei una comilla simple")
                    self.bitacora += "q0 -> q6 \n"
                    self.salida += entrada[letra]
                    estado = 6
                ##
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == "." or entrada[letra] == "#":
                    cadena += entrada[letra]
                    self.columna += 1
                    self.bitacora += "q0 -> q8 \n"
                    self.salida += entrada[letra]
                    estado = 8
                ##
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    self.columna += 1
                    self.salida += entrada[letra]
                    token_ = Tokencss(Tokencss.SELECTOR_UNIVERSAL)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenCSS(), cadena])
                    cadena = ""
                ##
                elif entrada[letra] == ";":
                    cadena += entrada[letra]
                    self.columna += 1
                    self.salida += entrada[letra]
                    token_ = Tokencss(Tokencss.PUNTO_Y_COMA)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenCSS(), cadena])
                    cadena = ""
                ##
                elif entrada[letra] == "(":
                    self.salida += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == "-":
                    self.columna += 1
                    self.salida += entrada[letra]
                    self.bitacora += "q0 -> q5 \n"
                    estado = 5
                ##
                elif entrada[letra] == ")":
                    self.salida += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == "{":
                    self.salida += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == "}":
                    self.salida += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == "[":
                    self.salida += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == "]":
                    self.salida += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == ",":
                    self.salida += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == ".":
                    self.salida += entrada[letra]
                    self.columna += 1
                ##
                elif entrada[letra] == "\n":
                    self.salida += entrada[letra]
                    self.fila += 1
                    self.columna = 1
                    #print("Salto de linea")
                ##
                elif entrada[letra] == "\t":
                    self.salida += entrada[letra]
                    self.fila += 4
                    # print("Tabulación")

                # ATRAPAR ERRORES
                else:
                    cadena += entrada[letra]
                    #self.salida += entrada[letra]
                    self.AgregarError(cadena, self.fila, self.columna)
                    self.columna += 1
                    cadena == ""
            ##
            elif estado == 1:
                self.bitacora += "Estado q1, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                #print("Estoy en estado 1")
                if entrada[letra] == "*":
                    #print("lei un asterisco")
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.bitacora += "q1 -> q2 \n"
                    estado = 2
                ##

                ##
                elif entrada[letra] == "\"":
                    #print("Lei comillas dobles")
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.bitacora += "q1 -> q2 \n"
                    estado = 2
                ##
                elif entrada[letra] == "\n":
                    #print("Lei un salto de linea")
                    cadena += entrada[letra]
                    self.fila += 1
                    self.columna = 1
                    self.salida += entrada[letra]
                    self.bitacora += "q1 -> q2 \n"
                    estado = 2
                ##
                elif entrada[letra] == "/":
                    #print("Lei una diagonal")
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.bitacora += "q1 -> q3 \n"
                    estado = 3
            ##
            elif estado == 2:
                self.bitacora += "Estado q2, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                #print("Estoy en estado 2")

                # LETRAS Y NUMEROS
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei una letra")
                ##
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un numero")
                ##
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un espacio")

                # SIGNOS DE PUNTUACION
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un punto")
                ##
                elif entrada[letra] == ",":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei una coma")
                ##
                elif entrada[letra] == ":":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei dos puntos")
                ##
                elif entrada[letra] == "\\":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei dos puntos")
                ##
                elif entrada[letra] == ";":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei punto y coma")

                # SIMBOLOS DE AGRUPACION
                elif entrada[letra] == "(":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei parentesis izq")
                ##
                elif entrada[letra] == ")":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei parentesis der")
                ##
                elif entrada[letra] == "<":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei bracket izq")
                ##
                elif entrada[letra] == ">":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei bracket der")
                ##
                elif entrada[letra] == "{":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei parentesis izq")
                ##
                elif entrada[letra] == "}":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei parentesis der")
                ##
                elif entrada[letra] == "[":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei corchete izq")
                ##
                elif entrada[letra] == "]":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei corchete der")

                # GUIONES
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un guión")
                ##
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un guion bajo")
                ##

                # OPERADORES
                elif entrada[letra] == "+":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo más")
                ##
                elif entrada[letra] == "=":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo igual")
                ##

                # SIGNOS DE INTERROGACION/EXCLAMACIÓN
                elif entrada[letra] == "!":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo exlamación")
                ##
                elif entrada[letra] == "¡":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo exclamación")
                ##
                elif entrada[letra] == "¿":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo interrogación")
                ##
                elif entrada[letra] == "?":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo interrogación")
                ##

                # SIMBOLOS
                elif entrada[letra] == "@":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un arroba")
                ##
                elif entrada[letra] == "$":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo de dolar")
                ##
                elif entrada[letra] == "^":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo de potencia")
                ##
                elif entrada[letra] == "%":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo de porcentaje")
                ##
                elif entrada[letra] == "&":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un signo aspersand")
                ##
                elif entrada[letra] == "\n":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.fila += 1
                    self.columna = 1
                    #print("Lei un salto de linea")
                ##
                elif entrada[letra] == "\t":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.fila += 4
                    #print("Lei una tabulación")
                ##
                elif entrada[letra] == "|":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un pipe")
                ##
                elif entrada[letra] == "°":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei una orden")
                ##
                elif entrada[letra] == "¬":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un simbolo raro")
                ##
                elif entrada[letra] == "'":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei una comilla simple")
                ##
                elif entrada[letra] == "*":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un asterisco")
                    self.bitacora += "q2 -> q1 \n"
                    estado = 1
            ##
            elif estado == 3:
                self.bitacora += "Estado q3, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                # ESTADO DE ACEPTACIÓN
                token_ = Tokencss(Tokencss.COMENTARIO)
                self.listaTokens.append([token_.ObtenerTipoTokenCSS(), cadena])
                self.bitacora += "   Token de tipo comentario aceptado\n"

                if self.VerificarRuta(cadena, 'PATHW:'):
                    # reemplazar la cadena
                    cadena.replace("PATHW:", "")
                #########
                self.bitacora += "q3 -> q0 \n"
                self.salida += entrada[letra]
                cadena = ""
                estado = 0
            ##
            elif estado == 4:
                self.bitacora += "Estado q4, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                # ESTADO DE ACEPTACIÓN
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei una letra")
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un numero")
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    #print("Lei un guion")
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "#":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ";":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "/":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "*":
                    #cadena += entrada[letra]
                    #self.salida += entrada[letra]
                    self.columna += 1

                # ERRORES LEXICOS
                elif entrada[letra] == "$":
                    # print("Error lexico $", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "@":
                    # print("Error lexico @", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "%":
                    # print("Error lexico %", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "¬":
                    # print("Error lexico ¬", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "|":
                    # print("Error lexico |", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "°":
                   # print("Error lexico °", "fila:",
                   #       self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == ">":
                    # print("Error lexico >", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "<":
                    # print("Error lexico <", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "+":
                    # print("Error lexico +", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "=":
                    # print("Error lexico =", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "~":
                    # print("Error lexico ~", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "/":
                    # print("Error lexico /", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "?":
                    # print("Error lexico ?", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                elif entrada[letra] == "¿":
                    # print("Error lexico ¿", "fila:",
                    #      self.fila, "col: ", self.columna)
                    self.listaErroresLex.append(
                        [self.fila, self.columna, entrada[letra]])
                    self.columna += 1
                    estado = 0
                else:  # aceptar el ID o detectar el error lexico
                    # print(cadena)
                    self.AgregarToken(cadena)
                    self.bitacora += "q4 -> q0 \n"
                    #cadena = ""
                    #estado = 0

                    if entrada[letra] == "{":
                        self.salida += entrada[letra]
                    elif entrada[letra] == ":":
                        self.salida += entrada[letra]
                    elif entrada[letra] == "(" or entrada[letra] == ")":
                        self.salida += entrada[letra]
                    elif entrada[letra] == "\n":
                        self.salida += entrada[letra]
                        self.fila += 1
                    cadena = ""
                    estado = 0
            ##
            elif estado == 5:
                # declarar prefijo (es la cadena que se esta leyendo) y sufijo
                sufijo = ""
                self.bitacora += "Estado q5, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "%":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "\n":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna = 1
                    self.fila += 1
                elif entrada[letra] == ";":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "}":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ")":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "/":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ",":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1

                else:
                    self.partirLexNumero(cadena)
                    range(len(entrada) - 1)
                    self.bitacora += "q5 -> q0 \n"
                    estado = 0

                    if entrada[letra] == " ":
                        #cadena += entrada[letra]
                        self.salida += entrada[letra]
                        self.columna += 1
            ##
            elif estado == 6:
                self.bitacora += "Estado q6, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "\\":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "\"" or entrada[letra] == "'":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                    self.bitacora += "q6 -> q7 \n"
                    estado = 7
            ##
            elif estado == 7:
                self.bitacora += "Estado q7, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                token_ = Tokencss(Tokencss.CADENA)
                self.listaTokens.append([token_.ObtenerTipoTokenCSS(), cadena])
                self.bitacora += "   Token cadena de texto reconocida\n"
                self.bitacora += "q7 -> q8 \n"
                self.salida += entrada[letra]
                cadena = ""
                estado = 0
            ##
            elif estado == 8:
                self.bitacora += "Estado q8, caracter: "
                self.bitacora += entrada[letra]
                self.bitacora += "\n"
                
                
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1

                elif entrada[letra] == "{" or entrada[letra] == "}":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ";":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ":":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ",":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == ".":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna += 1
                elif entrada[letra] == "\n":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.columna = 1
                    self.fila += 1
                elif entrada[letra] == " ":
                    self.columna += 1
                    token_ = Tokencss(Tokencss.SELECTOR)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenCSS(), cadena])
                    self.bitacora += "  Token identificador reconocido \n"
                    cadena = ""
                    self.bitacora += "q8 -> q0 \n"
                    estado = 0

                    """if entrada[letra] == "{":
                        self.salida += entrada[letra]
                    elif entrada[letra] == ":":
                        self.salida += entrada[letra]
                    cadena = ""
                    estado = 0"""

    ####################

    def AgregarToken(self, token):

        # SELECTORES HTML
        if token == "h1":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "h2":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "h3":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "h4":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "h5":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "p":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "div":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "ul":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "li":
            token_ = Tokencss(Tokencss.SELECTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "a":
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
        elif token == "margin-bottom":
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
        elif token == "height":
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
        elif token == "border-top":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "background":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "solid":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "rgba":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "absolute":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "content":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "url":
            token_ = Tokencss(Tokencss.URL_)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "margin":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "display":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "overflow":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "border-radius":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "transition":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "box-shadow":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "cursor":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "clear":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "type":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "focus":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "clear":
            token_ = Tokencss(Tokencss.PROPIEDAD)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])

        ######## COLORES ########
        elif token == "white":
            token_ = Tokencss(Tokencss.COLOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "red":
            token_ = Tokencss(Tokencss.COLOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "blue":
            token_ = Tokencss(Tokencss.COLOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "black":
            token_ = Tokencss(Tokencss.COLOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "gray":
            token_ = Tokencss(Tokencss.COLOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "green":
            token_ = Tokencss(Tokencss.COLOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "yellow":
            token_ = Tokencss(Tokencss.COLOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "orange":
            token_ = Tokencss(Tokencss.COLOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])
        elif token == "aqua":
            token_ = Tokencss(Tokencss.COLOR)
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
            token_ = Tokencss(Tokencss.IDENTIFICADOR)
            self.listaTokens.append([token_.ObtenerTipoTokenCSS(), token])

    ####################

    def AgregarError(self, caracter, fila, col):
        # validar los caracteres que sean erroes y agregarlos a la lista de errores
        if caracter == "@":
            print("Error lexico @", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "#":
            print("Error lexico #", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "|":
            print("Error lexico |", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "¿":
            print("error lexico ¿", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "´":
            print("error lexico ´", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "~":
            print("error lexico ~", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "^":
            print("error lexico ^", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "_":
            print("error lexico _", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "?":
            print("error lexico ?", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "$":
            print("error lexico $", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "%":
            print("error lexico %", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "¬":
            print("error lexico ¬", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "°":
            print("error lexico °", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "/":
            print("error lexico /", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])

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
        bitacora = self.bitacora
        # print(bitacora)
        return bitacora
        # imprimir lista de errores

    ####################

    def VerificarRuta(self, p1, p2):
        aux = p1.replace(p2, "")
        ruta = ""
        ruta = aux.replace(" ", "")
        ruta = ruta.replace("\\\\", "")

        try:
            if ruta[0] == "c" or ruta[0] == "C" and ruta[1] == ":":
                
                directorio = ""
                directorio = ruta
                #directorio = ruta.replace("\\", "")
                directorio = os.path.join(directorio)
                print(directorio)
                
                if not os.path.exists(directorio):
                    print("creado")
                    os.mkdir(directorio)

                self.dir_salida = directorio
                #archivo = open(ruta, "w+")
                #archivo.write("prueba jeje")
                #archivo.close()
        except IndexError:
            pass

        return (' ' + p2 + ' ') in (' ' + p1 + ' ')

    ####################

    def CantidadLineas(self):
        return self.fila

    ####################

    def GenerarReporte(self):
        contador = 1  # contador del numero de errores
        reporte = open("Reportes/ErroresCSS.html", "w", encoding="utf-8")

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

            # print(contador)
            contenido2 = "<tr>"\
                "<td>"\
                + str(contador) +\
                "</td>"\
                "<td>"\
                + str(error[0]) +\
                "</td>"\
                "<td>"\
                + str(error[1]) +\
                "</td>"\
                "<td>"\
                + str(error[2]) +\
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

        os.startfile(
            "C:\\Users\\jsola\\Desktop\\Proyecto1_Compiladores\\Reportes\\ErroresCSS.html")

    ####################

    def GenerarArchivoSalida(self):

        archivo = "salida.css"
        rutafinal = ""
        rutafinal += self.dir_salida
        rutafinal += archivo
        
        salida = open(rutafinal, "w+")
        salida.write(self.salida)
        salida.close()
