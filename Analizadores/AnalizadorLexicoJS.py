
from enum import Enum
from io import open


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

    # relacionales
    EXPR_IGUAL = "Expresion_igual"
    S_MAYOR = "Simbolo_mayor"
    S_MENOR = "Simbolo_menor"
    S_MAYOR_IGUAL = "Simbolo_mayor"
    S_MENOR_IGUAL = "Simbolo_menor"

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
    PUNTO_Y_COMA = "Punto_y_coma"

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

    ####################

    def Escanear(self, entrada):
        # recorrer texto de entrada
        estado = self.estado
        cadena = ""

        for letra in range(len(entrada)):
            """
                Estados de acepación de tokens JS
                estado = 2 (comentario de una linea)
                estado = 5 (comentario multilinea)
                estado = 6 (Identificador)
                estado = 7 y 8 (Numeros enteros / con punto decimal)
            """

            if estado == 0:
                cadena = ""

                range(len(entrada)-1)

                if entrada[letra] == "/":
                    cadena += entrada[letra]
                    estado = 1
                elif entrada[letra].isalpha():
                    cadena += entrada[letra]
                    estado = 6
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    estado = 7
                elif entrada[letra] == "\n":
                    cadena = ""
                elif entrada[letra] == "\t":
                    cadena = ""
                elif entrada[letra] == ";":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PUNTO_Y_COMA)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "(":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PARENTESIS_IZQ)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == ")":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.PARENTESIS_DER)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "[":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.CORCHETE_IZQ)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "]":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.CORCHETE_DER)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "{":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.LLAVE_IZQ)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "}":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.LLAVE_DER)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == ">":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.S_MAYOR)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "<":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.S_MENOR)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    s = TokenJavascript(TokenJavascript.S_MULT)
                    self.listaTokens.append([s.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                
                # ATRAPAR ERRORES  


            ##
            elif estado == 1:

                if entrada[letra] == "/":
                    cadena += entrada[letra]
                    estado = 2
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    estado = 3
            ##
            elif estado == 2:

                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                elif entrada[letra] == "\n":
                    token_ = TokenJavascript(TokenJavascript.COMENTARIO)
                    self.listaTokens.append(
                        [token_.ObtenerTipoTokenJS(), cadena])
                    cadena = ""
                    estado = 0
            ##
            elif estado == 3:

                if entrada[letra] == "*":
                    cadena += entrada[letra]
                elif entrada[letra].isdigit() or entrada[letra].isalpha():
                    cadena += entrada[letra]
                    estado = 4
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    estado = 5
            ##
            elif estado == 4:

                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                elif entrada[letra] == "\n":
                    cadena += entrada[letra]
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    estado = 3
            ##
            elif estado == 5:
                token_ = TokenJavascript(TokenJavascript.COMENTARIO)
                self.listaTokens.append([token_.ObtenerTipoTokenJS(), cadena])
                cadena = ""
                estado = 0
            ##
            elif estado == 6:
                if entrada[letra].isalpha():
                    cadena += entrada[letra]

                elif entrada[letra].isdigit():
                    cadena += entrada[letra]

                elif entrada[letra] == "_":
                    cadena += entrada[letra]
                elif entrada[letra] == "@":
                    print("error")
                    cadena = ""
                    estado = 0
                else:
                    # clasificar y agregar token aceptado a la lista
                    self.AgregarToken(cadena)
                    cadena = ""
                    estado = 0
            ##
            elif estado == 7:

                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                    estado = 7
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    estado = 8
                else:
                    estado = 8
            ##
            elif estado == 8:
                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                else:
                    tk_num = TokenJavascript(TokenJavascript.NUMERO)
                    self.listaTokens.append(
                        [tk_num.ObtenerTipoTokenJS(), cadena])
                    range(len(entrada) - 1)
                    estado = 0

    ####################

    def ImprimirListaTokens(self):
        lista = self.listaTokens
        for token in lista:
            print(token)

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
            #token_ = TokenJavascript(TokenJavascript.pr_con)
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

    def GenerarReporte(self, ruta):
        # Generar reporte de errores y crea el archivo de acuerdo al directorio dado al inicio del archivo JS
        pass

    ####################
