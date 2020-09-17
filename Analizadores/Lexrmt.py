from enum import Enum


class Token(Enum):

    ID = "Identificador"
    NUM_ENTERO = "Numero entero"
    OP_MULT = "Operador multiplicacion"
    OP_SUMA = "Operador suma"
    OP_RESTA = "Operador resta"
    OP_DIVISION = "Operador division"
    PAR_IZQ = "Parentesis izq"
    PAR_DER = "Parentesis der"
    SALTO_LINEA = "Salto de linea"

    def __init__(self, token):
        super().__init__()

        self.Token = token

    def ObtenerTipoTokenHTML(self):
        return self.Token

    ###


# Analizador lexico de las expresiones
class Lexrmt():

    def __init__(self):
        super().__init__()

        self.estado = 0
        self.fila = 1
        self.columna = 1
        self.ListaTokens = []
        self.ListaErroresLex = []
        self.salida = ""
        self.listaExpr = []

    def Escanear(self, entrada):
        estado = self.estado
        expresion = ""
        # ESTADOS DE RECONOCIMIENTO DE TOKENS POR EL QUE PASARA EL ANALIZADOR LEXICO

        for letra in range(len(entrada)):
            #expresion = ""
            if entrada[letra].isdigit():
                expresion += entrada[letra]
            
            ##
            elif entrada[letra].isalpha():
                expresion += entrada[letra]
            
            ##
            elif entrada[letra] == "+" or entrada[letra] == "-" or entrada[letra] == "/"  or entrada[letra] == "*":
                expresion += entrada[letra]
            
            ##
            elif entrada[letra] == "(" or entrada[letra] == ")":
                expresion += entrada[letra]
            
            ##
            elif entrada[letra] == "_":
                expresion += entrada[letra]
            
            ##
            elif entrada[letra] == ".":
                expresion += entrada[letra]
            
            ##
            elif entrada[letra] == "\n":
                expresion += entrada[letra]
                print(expresion)
                self.listaExpr.append(expresion)
                expresion = ""
            """
            if estado == 0:
                # print(entrada[letra])

                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                    estado = 1
                elif entrada[letra].isalpha():
                    cadena += entrada[letra]
                    estado = 2
                elif entrada[letra] == "(":
                    cadena += entrada[letra]
                    t = Token(Token.PAR_IZQ)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    cadena = ""
                elif entrada[letra] == ")":
                    cadena += entrada[letra]
                    t = Token(Token.PAR_DER)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    cadena = ""
                elif entrada[letra] == "+":
                    cadena += entrada[letra]
                    t = Token(Token.OP_SUMA)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    cadena = ""
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    t = Token(Token.OP_RESTA)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    cadena = ""
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    t = Token(Token.OP_MULT)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    cadena = ""
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    t = Token(Token.OP_DIVISION)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    cadena = ""
                elif entrada[letra] == "\n":
                    cadena += entrada[letra]
                    t = Token(Token.SALTO_LINEA)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    cadena = ""
            ##
            elif estado == 1:

                # print(entrada[letra])
                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                else:
                    t = Token(Token.NUM_ENTERO)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    estado = 0
                    cadena = ""
                    if entrada[letra] == "(":
                        cadena += entrada[letra]
                        t = Token(Token.PAR_IZQ)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == ")":
                        cadena += entrada[letra]
                        t = Token(Token.PAR_DER)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "+":
                        cadena += entrada[letra]
                        t = Token(Token.OP_SUMA)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "-":
                        cadena += entrada[letra]
                        t = Token(Token.OP_RESTA)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "*":
                        cadena += entrada[letra]
                        t = Token(Token.OP_MULT)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "/":
                        cadena += entrada[letra]
                        t = Token(Token.OP_DIVISION)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "\n":
                        cadena += entrada[letra]
                        t = Token(Token.SALTO_LINEA)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
            ##
            elif estado == 2:

                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                else:
                    t = Token(Token.ID)
                    self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                    estado = 0
                    cadena = ""
                    if entrada[letra] == "(":
                        cadena += entrada[letra]
                        t = Token(Token.PAR_IZQ)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == ")":
                        cadena += entrada[letra]
                        t = Token(Token.PAR_DER)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "+":
                        cadena += entrada[letra]
                        t = Token(Token.OP_SUMA)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "-":
                        cadena += entrada[letra]
                        t = Token(Token.OP_RESTA)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "*":
                        cadena += entrada[letra]
                        t = Token(Token.OP_MULT)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "/":
                        cadena += entrada[letra]
                        t = Token(Token.OP_DIVISION)
                        self.ListaTokens.append(
                            [t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "\n":
                        cadena += entrada[letra]
                        t = Token(Token.SALTO_LINEA)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
            """
    
    def imprimirListaTokens(self):
        for token in self.ListaTokens:
            print(token)

    def imprimirExpresiones(self):
        for exp in self.listaExpr:
            print(exp)