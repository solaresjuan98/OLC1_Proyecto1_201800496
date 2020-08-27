
from enum import Enum
from io import open


class TokenJavascript(Enum):

    COMENTARIO = "Comentario"
    PR_VAR = "Pr_Var"

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
            """

            if estado == 0:
                cadena = ""

                range(len(entrada)-1)

                if entrada[letra] == "/":
                    cadena += entrada[letra]
                    estado = 1
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

    ####################

    def ImprimirListaTokens(self):
        lista = self.listaTokens
        for token in lista:
            print(token)

    ####################

    def AgregarToken(self, token):
        pass

    ####################

    def GenerarReporte(self, ruta):
        # Generar reporte de errores y crea el archivo de acuerdo al directorio dado al inicio del archivo JS
        pass

    ####################
