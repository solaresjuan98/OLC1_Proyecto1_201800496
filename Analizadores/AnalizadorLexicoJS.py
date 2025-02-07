
from enum import Enum
from io import open
import os


class TokenJavascript(Enum):

    COMENTARIO = "Comentario"
    PR_VAR = "Pr_Var"
    IDENTIFICADOR = "Identificador"

    # valores booleanas
    PR_TRUE = "Pr_True"
    PR_FALSE = "Pr_False"

    # condicionales
    PR_IF = "Pr_if"
    PR_ELSE = "Pr_else"

    # bucles
    PR_FOR = "Pr_for"
    PR_WHILE = "Pr_while"
    PR_DO = "Pr_do"
    PR_BREAK = "Pr_break"

    # POO
    PR_CONSTRUCTOR = "Pr_constructor"
    PR_THIS = "Pr_this"
    PR_CLASS = "Pr_class"

    # otras
    PR_RETURN = "Pr_return"
    PR_FUNCTION = "Pr_function"

    ### EXPRESIONES ###
    # aritmeticas
    S_SUMA = "Simbolo_suma"
    S_RESTA = "Simbolo_resta"
    S_MULT = "Simbolo_multiplicacion"
    S_DIVISION = "Simbolo_division"
    PR_POW = "Pr_pow"
    PR_MATH = "Pr_math"

    # valores numericos
    NUMERO = "Numero"

    CADENA = "Cadena de texto"

    # relacionales
    EXPR_IGUAL = "Expresion_igual"
    S_MAYOR = "Simbolo mayor que"
    S_MENOR = "Simbolo menor que"
    S_MAYOR_IGUAL = "Simbolo mayor o igual que"
    S_MENOR_IGUAL = "Simbolo menor o igual que"
    DISTINTO = "Distinto"
    INCREMENTO = "Incremento"
    DECREMENTO = "Decremento"

    # logicos
    CONJUNCION = "Conjuncion"
    DISTUNCION = "Disyuncion"
    NEGACION = "Negacion"

    # parentesis
    PARENTESIS_IZQ = "Parentesis_izq"
    PARENTESIS_DER = "Parentesis_der"

    # llaves
    LLAVE_IZQ = "Llave_izq"
    LLAVE_DER = "Llave_der"

    # corchetes
    CORCHETE_IZQ = "Corchete_izq"
    CORCHETE_DER = "Corchete_der"

    # punto y coma
    PUNTO_Y_COMA = "Punto y coma"
    COMA = "Coma"
    PUNTO = "Punto"
    DOS_PUNTOS = "Dos_puntos"

    # ERROR LEXICO
    ERROR = "Error Léxico"

    def __init__(self, token):
        super().__init__()

        self.Token = token

    def ObtenerTipoTokenJS(self):
        return self.Token

################################


class AnalizadorLexicoJS():

    def __init__(self):
        super().__init__()

        self.listaTokens = []
        self.listaErroresLex = []
        self.salida = ""
        self.estado = 0
        self.fila = 1
        self.col = 1
        # cadena donde se limpia el archivo
        self.archivo_salida = ""
        # directorio donde se almacenará la salida 
        self.dir_salida = ""
        # bandera archivos
        self.bandArchivo = False

    ####################

    def Escanear(self, entrada):
        # recorrer texto de entrada
        estado = self.estado
        #self.salida = entrada
        cadena = ""
        # bandera que indica si el grafo de automata fue generado
        banderaID = False
        banderaNum = False
        banderaComentario = False
        banderaCadena = False

        for letra in range(len(entrada)):
            """
                Estados de acepación de tokens JS
                estado = 2 (comentario de una linea)
                estado = 5 (comentario multilinea)
                estado = 6 (Identificador)
                estado = 7 y 8 (Numeros enteros / con punto decimal)
                estado = 9 (expresiones relacionales)
                estado = 13 (cadenas de texto)
            """
            # ESTADOS DE ANALIZADOR LEXICO
            if estado == 0:
                #cadena = ""
                #print("Estoy en estado 0 ", entrada[letra])
                range(len(entrada)-1)
                cadena = ""
                if entrada[letra] == "/":
                    self.salida += entrada[letra]
                    # cadena += entrada[letra]
                    self.col += 1
                    estado = 1
                elif entrada[letra].isalpha():
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 6
                elif entrada[letra].isdigit():
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 7

                elif entrada[letra] == " ":
                    self.salida += entrada[letra]
                    self.col += 1
                    #cadena = ""
                # RECONOCIENDO CADENAS
                elif entrada[letra] == "\"" or entrada[letra] == "'":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 11

                elif entrada[letra] == "\n":
                    self.salida += entrada[letra]
                    self.fila += 1
                    self.col = 1
                    #estado = 0
                    # cadena = ""
                elif entrada[letra] == "\t":
                    self.salida += entrada[letra]
                    #estado = 0
                    self.col += 4
                elif entrada[letra] == ",":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.COMA)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == ".":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PUNTO)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    self.col += 1
                    # estado = 0
                    cadena = ""
                elif entrada[letra] == ":":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.DOS_PUNTOS)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == ";":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PUNTO_Y_COMA)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                    #estado = 0
                elif entrada[letra] == "(":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PARENTESIS_IZQ)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == ")":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PARENTESIS_DER)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "[":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.CORCHETE_IZQ)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""

                elif entrada[letra] == "]":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.CORCHETE_DER)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""

                elif entrada[letra] == "{":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.LLAVE_IZQ)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "}":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.LLAVE_DER)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""

                # OPERADORES ARITMETICOS
                elif entrada[letra] == ">":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    estado = 9
                elif entrada[letra] == "<":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    estado = 9
                elif entrada[letra] == "!":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    estado = 9
                elif entrada[letra] == "*":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.S_MULT)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "-":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    estado = 9
                elif entrada[letra] == "+":
                    self.salida += entrada[letra]
                    self.col += 1
                    cadena += entrada[letra]
                    estado = 9
                elif entrada[letra] == "=":
                    self.salida += entrada[letra]
                    self.col += 1
                    entrada += entrada[letra]
                    estado = 9
                elif entrada[letra] == "!":
                    self.salida += entrada[letra]
                    self.col += 1
                    entrada += entrada[letra]
                    estado = 9
                # ATRAPAR ERRORES
                else:
                    cadena += entrada[letra]
                    # self.EliminarError(cadena)
                    self.AgregarError(cadena, self.fila, self.col)
                    self.col += 1
                    cadena == ""
            ##
            elif estado == 1:
                #print("Estoy en estado 1 ", cadena)
                if entrada[letra] == "/":
                    # cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 2
                elif entrada[letra] == "*":
                    self.col += 1
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    estado = 3
                else:
                    self.AgregarError(cadena, self.fila, self.col)
                    self.col += 1
                    estado = 0
                    cadena = ""

                """elif entrada[letra] == "\n":
                    # cadena += entrada[letra]
                    self.col += 1
                    self.fila += 1"""
            ##
            elif estado == 2:
                #print("Estoy en estado 2 ", cadena)
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ":":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PUNTO)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    self.col += 1
                elif entrada[letra] == "\\":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\n":
                    self.fila += 1
                    self.col = 1
                    self.salida += entrada[letra]
                    token_ = TokenJavascript(TokenJavascript.COMENTARIO)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenJS(), cadena])

                    if self.VerificarRuta(cadena, 'PATHW:') and self.bandArchivo == False:
                        # reemplazar la cadena
                        cadena.replace("PATHW:", "")
                        self.bandArchivo = True
                    #########
                    cadena = ""
                    estado = 0
            ##
            elif estado == 3:
                #print("Estoy en estado 3 ", cadena)
                if entrada[letra] == "*":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra].isdigit() or entrada[letra].isalpha():
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    estado = 4
                    self.col += 1
                elif entrada[letra] == "\n":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.fila += 1
                    self.col = 1
                elif entrada[letra] == "/":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    estado = 5
                    self.col += 1
            ##
            elif estado == 4:
                #print("Estoy en estado 4 ", cadena)
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "@":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "^":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "$":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "%":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "'":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "~":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "+":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "-":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "=":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "<":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ">":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ":":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "[":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "]":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "(":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ")":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ".":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PUNTO)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\\":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "/":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\n":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col = 1
                    self.fila += 1
                elif entrada[letra] == "*":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 3
            ##
            elif estado == 5:
                #print("Estoy en estado 5 ", cadena)
                self.fila += 1
                token_ = TokenJavascript(TokenJavascript.COMENTARIO)
                self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
                cadena = ""
                estado = 0
            ##
            elif estado == 6:
                #print("Estoy en estado 6 ", cadena)
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == " ":
                    self.AgregarToken(cadena)
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 0
                elif entrada[letra] == "(":
                    self.AgregarToken(cadena)
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 0
                elif entrada[letra] == ")":
                    self.AgregarToken(cadena)
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 0
                elif entrada[letra] == "." or entrada[letra] == "," or entrada[letra] == ":" or entrada[letra] == ";":
                    self.AgregarToken(cadena)
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 0
                # ERRORES LEXICOS
                elif entrada[letra] == "@":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "|":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "&":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "^":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "%":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "~":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "|":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "´":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "°":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0
                elif entrada[letra] == "#":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    cadena = ""
                    estado = 0

                else:
                    # clasificar y agregar token aceptado a la lista
                    self.AgregarToken(cadena)
                    if banderaID == False:
                        self.GenerarGrafoID(cadena)
                        banderaID = True
                    estado = 0
                # PARENTESIS, etc (causa que se estanquee)
                """elif entrada[letra] == "(" or entrada[letra] == ":":
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 14"""
            ##
            elif estado == 7:
                #print("Estoy en estado 7 ", cadena)
                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 7
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 8
                else:
                    # estado = 8
                    tk_num = TokenJavascript(TokenJavascript.NUMERO)
                    self.listaTokens.append(
                        [tk_num.ObtenerTipoTokenJS(), cadena])
                    # range(len(entrada) - 1)
                    self.AgregarError(entrada[letra], self.fila, self.col)

                    # generando grafo
                    if banderaNum == False:
                        self.GenerarGrafoNum(cadena)
                        banderaNum = True

                    elif entrada[letra] == "(":
                        self.AgregarToken(cadena)
                        self.salida += entrada[letra]
                        self.col += 1
                        estado = 0
                    elif entrada[letra] == ")":
                        self.AgregarToken(cadena)
                        self.salida += entrada[letra]
                        self.col += 1
                        estado = 0
                    elif entrada[letra] == "." or entrada[letra] == "," or entrada[letra] == ":":
                        self.AgregarToken(cadena)
                        self.salida += entrada[letra]
                        self.col += 1
                        estado = 0

                    cadena = ""
                    estado = 0
            ##
            elif estado == 8:
                #print("Estoy en estado 8 ", cadena)
                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                else:
                    tk_num = TokenJavascript(TokenJavascript.NUMERO)
                    self.listaTokens.append(
                        [tk_num.ObtenerTipoTokenJS(), cadena])
                    # range(len(entrada) - 1)
                    if banderaNum == False:
                        self.GenerarGrafoNum(cadena)
                        banderaNum = True

                    cadena = ""
                    estado = 0
            ##
            elif estado == 9:
                #print("Estoy en estado 9 ", cadena)
                if entrada[letra] == "=":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 10
                    # range(len(entrada) - 1)
                else:
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    cadena = ""
                    estado = 0

                    if entrada[letra] == ">":
                        self.salida += entrada[letra]
                        #cadena += entrada[letra]
                        self.col += 1
                        estado = 0
            ##
            elif estado == 10:
                self.ClasificarExpr(cadena)
                # print(cadena)
                cadena = ""
                estado = 0
            ##
            elif estado == 11:
                #print("Estoy en estado 11 ", cadena)
                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.col += 1
                    self.salida += entrada[letra]
                    estado = 12
                elif entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.col += 1
                    self.salida += entrada[letra]
                    estado = 12
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    self.col += 1
                    self.salida += entrada[letra]
                    estado = 12
                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 12
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 12
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 12
                elif entrada[letra] == ",":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 12
                elif entrada[letra] == ":":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 12
            ##
            elif estado == 12:

                if entrada[letra].isdigit():
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra].isalpha():
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "/":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "_":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "-":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == " ":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ".":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ">":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "[":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "]":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "_":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ":":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\"" or entrada[letra] == "'":
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 13
            ##
            elif estado == 13:

                token_ = TokenJavascript(TokenJavascript.CADENA)
                self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

                if banderaCadena == False:
                    self.GenerarGrafoCadenaTexto(cadena)
                    banderaCadena = True

                if entrada[letra] == ")" or entrada[letra] == "(":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ".":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ",":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "+":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ";":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ":":
                    self.salida += entrada[letra]
                    self.col += 1

                cadena = ""
                estado = 0
            ##
            elif estado == 14:

                if entrada[letra] == "(":
                    self.col += 1
                    #cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PARENTESIS_IZQ)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena == ""
                    estado = 0
                elif entrada[letra] == ":":
                    self.col += 1
                    #cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.DOS_PUNTOS)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena == ""
                    estado = 0

    ####################

    def ImprimirListaTokens(self):
        contenido = ""
        lista = self.listaTokens
        for token in lista:
            contenido += "Tipo: "\
                + str(token[0]) +\
                " VALOR: "\
                + str(token[1]) +\
                "\n"\

        return contenido

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

    ####################

    def EliminarError(self, caracter):
        print(caracter)

        print("borrado")

    ####################

    def ClasificarExpr(self, token):

        if token == "!=":
            t = TokenJavascript(TokenJavascript.DISTINTO)
            self.listaTokens.append([t.ObtenerTipoTokenJS(), token])
        elif token == ">=":
            t = TokenJavascript(TokenJavascript.S_MAYOR_IGUAL)
            self.listaTokens.append([t.ObtenerTipoTokenJS(), token])
        elif token == "<=":
            t = TokenJavascript(TokenJavascript.S_MENOR_IGUAL)
            self.listaTokens.append([t.ObtenerTipoTokenJS(), token])
        elif token == "==":
            t = TokenJavascript(TokenJavascript.EXPR_IGUAL)
            self.listaTokens.append([t.ObtenerTipoTokenJS(), token])
        elif token == "+=":
            t = TokenJavascript(TokenJavascript.INCREMENTO)
            self.listaTokens.append([t.ObtenerTipoTokenJS(), token])
        elif token == "-=":
            t = TokenJavascript(TokenJavascript.DECREMENTO)
            self.listaTokens.append([t.ObtenerTipoTokenJS(), token])

    ####################

    def AgregarToken(self, cadena):

        # condicionales
        if cadena == "if":
            token_ = TokenJavascript(TokenJavascript.PR_IF)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        elif cadena == "else":
            token_ = TokenJavascript(TokenJavascript.PR_ELSE)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

        # variables booleanas
        elif cadena == "true":
            token_ = TokenJavascript(TokenJavascript.PR_TRUE)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        elif cadena == "false":
            token_ = TokenJavascript(TokenJavascript.PR_FALSE)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

        # var
        elif cadena == "var":
            token_ = TokenJavascript(TokenJavascript.PR_VAR)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

        # bucles
        elif cadena == "for":
            token_ = TokenJavascript(TokenJavascript.PR_FOR)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        elif cadena == "while":
            token_ = TokenJavascript(TokenJavascript.PR_WHILE)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        elif cadena == "do":
            token_ = TokenJavascript(TokenJavascript.PR_DO)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

        # sentencias de escape
        elif cadena == "continue":
            pass
            # token_ = TokenJavascript(TokenJavascript.pr_con)
        elif cadena == "break":
            token_ = TokenJavascript(TokenJavascript.PR_BREAK)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        elif cadena == "return":
            token_ = TokenJavascript(TokenJavascript.PR_RETURN)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

        # metodos y funciones
        elif cadena == "function":
            token_ = TokenJavascript(TokenJavascript.PR_FUNCTION)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

        # clases
        elif cadena == "class":
            token_ = TokenJavascript(TokenJavascript.PR_CLASS)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        elif cadena == "constructor":
            token_ = TokenJavascript(TokenJavascript.PR_CONSTRUCTOR)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        elif cadena == "this":
            token_ = TokenJavascript(TokenJavascript.PR_THIS)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

        # potencias
        elif cadena == "Math":
            token_ = TokenJavascript(TokenJavascript.PR_MATH)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        elif cadena == "pow":
            token_ = TokenJavascript(TokenJavascript.PR_POW)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
        else:
            token_ = TokenJavascript(TokenJavascript.IDENTIFICADOR)
            self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])

    ####################

    def VerificarRuta(self, p1, p2):
        aux = p1.replace(p2, "")
        #print("aux: ", aux)
        ruta = ""
        ruta = aux.replace(" ", "")
        #print("Ruta: ", ruta)
        ruta = ruta.replace("\\\\", "")
        print(ruta)
        try:
            if (ruta[0] == "c" or ruta[0] == "C") and ruta[1] == ":":
                #dir = ruta.replace("\\", "")
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

    def ObtenerRuta(self, cadena):
        pass

    ####################

    def GenerarSalida(self):
        
        archivo = "salida.js"
        rutafinal = ""
        rutafinal += self.dir_salida
        rutafinal += archivo

        output = open(rutafinal, "w+")

        output.write(self.salida.replace("@", "", -1).replace("|", "", -1))

        output.close()

    ####################

    def GenerarGrafoID(self, cadena):

        # GENERA EL AUTOMATA DE UN ID
        graph = open("grafo.txt", "w")
        graph.write("digraph G { \n")

        graph.write("q0 -> q1 [label= \"" + cadena[0] + "\" ] \n")
        # toma el resto de la cadena
        aux = cadena[1:]
        content = ""

        # estado de aceptación
        for letra in aux:
            graph.write("q1 -> q1 [label= \"" + letra + "\" ] \n")

        graph.write("q1[peripheries=2] \n")
        graph.write("{ rank = \"same\"; q0; q1; }\n")
        graph.write("}")
        graph.close()
        os.system('cmd /c "dot -Tjpg grafo.txt -o grafoID.jpg"')
        os.startfile("grafoID.jpg")
    ####################

    def ver_subcadena(self, s, w):
        return (' ' + w + ' ') in (' ' + s + ' ')

    ####################

    def GenerarGrafoNum(self, num):

        # GENERA EL AUTOMATA DE UN ID
        graph = open("grafo_numero.txt", "w")
        graph.write("digraph G { \n")

        # 1. Verifico si es un decimal o entero
        # 2. Si es numero entero solo lo hago con dos estados
        # 3. Si tiene punto decimal hacerlo con tres estados

        if self.ver_subcadena(num, '.'):
            # hacerlo con tres estados
            # partir numero en dos
            num_aux = num.split(".")
            print(num_aux[0])
            print(num_aux[1])

        else:
            # hacerlo solo con dos estados
            # si solo es un numero entero
            graph.write("q0 -> q1 [label= \"" + num[0] + "\" ] \n")
            # toma el resto de la cadena
            aux = num[1:]
            content = ""
            # estado de aceptación (si es un numero entero)
            for numero in aux:
                graph.write("q1 -> q1 [label= \"" + numero + "\" ] \n")

                #####
            graph.write("q1[peripheries=2] \n")
            graph.write("{ rank = \"same\"; q0; q1; }\n")

        graph.write("}")
        graph.close()
        os.system('cmd /c "dot -Tjpg grafo_numero.txt -o grafo_numero.jpg"')
        os.startfile("grafo_numero.jpg")
    ####################

    def GenerarGrafoCadenaTexto(self, cadena):
        # GENERA EL AUTOMATA DE UNA CADENA DET
        graph = open("grafo_cadena.txt", "w")
        graph.write("digraph G { \n")

        aux1 = cadena[0]
        aux2 = cadena[1:-1]
        aux3 = cadena[-1]

        graph.write("q0 -> q1 [label= \"" + "Comilla simple/doble" + "\" ]; \n")

        for letra in aux2:
            
            graph.write("q1 -> q1 [label = \""+letra + "\"]; \n")

        graph.write("q1 -> q2 [label= \"" + "Comilla simple/doble" + "\" ]; \n")
        graph.write("q2[peripheries=2] \n")
        graph.write("}")
        graph.close()
        os.system('cmd /c "dot -Tjpg grafo_cadena.txt -o grafoCadena.jpg"')
        os.startfile("grafoCadena.jpg")
    ####################

    def GenerarReporte(self):
        # Generar reporte de errores y crea el archivo de acuerdo al directorio dado al inicio del archivo JS
        contador = 1  # contador del numero de errores
        reporte = open("Reportes/Erroresjs.html", "w")

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
                    "<h2>PROYECTO COMPILADORES 1</h2>"\
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
                    "<th>Fila</th>"\
                    "<th>Columna</th>"\
                    "<th>Descripcion</th>"\
                    "</tr>"\

        reporte.write(contenido)

        for error in self.listaErroresLex:
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
            "C:\\Users\\jsola\\Desktop\\Proyecto1_Compiladores\\Reportes\\Erroresjs.html")

        pass

    ####################

    def GuardarError(self, error):
        print(error)
        pass
