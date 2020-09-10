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

    def Escanear(self, entrada):
        estado = self.estado
        cadena = ""
        # ESTADOS DE RECONOCIMIENTO DE TOKENS POR EL QUE PASARA EL ANALIZADOR LEXICO

        for letra in range(len(entrada)):

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
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == ")":
                        cadena += entrada[letra]
                        t = Token(Token.PAR_DER)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "+":
                        cadena += entrada[letra]
                        t = Token(Token.OP_SUMA)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "-":
                        cadena += entrada[letra]
                        t = Token(Token.OP_RESTA)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "*":
                        cadena += entrada[letra]
                        t = Token(Token.OP_MULT)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "/":
                        cadena += entrada[letra]
                        t = Token(Token.OP_DIVISION)
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
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == ")":
                        cadena += entrada[letra]
                        t = Token(Token.PAR_DER)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "+":
                        cadena += entrada[letra]
                        t = Token(Token.OP_SUMA)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "-":
                        cadena += entrada[letra]
                        t = Token(Token.OP_RESTA)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "*":
                        cadena += entrada[letra]
                        t = Token(Token.OP_MULT)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0
                    elif entrada[letra] == "/":
                        cadena += entrada[letra]
                        t = Token(Token.OP_DIVISION)
                        self.ListaTokens.append([t.ObtenerTipoTokenHTML(), cadena])
                        cadena = ""
                        estado = 0

                    
    def imprimirListaTokens(self):
        for token in self.ListaTokens:
            print(token)
