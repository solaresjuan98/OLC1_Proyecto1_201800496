
from enum import Enum
from io import open
import os


class TokenHTML(Enum):

    # etiquetas de apertura
    ETIQUETA_HTML = "etiqueta html"
    ETIQUETA_BODY = "etiqueta body"

    # titulos y subtitulos
    ETIQUETA_H1 = "etiqueta h1"
    ETIQUETA_H2 = "etiqueta h2"
    ETIQUETA_p = "p"

    # imagen
    ETIQUETA_IMF = "etiqueta img"

    # Listas e indices
    ETIQUETA_UL = "ul"
    ETIQUETA_LI = "li"

    # Tablas
    ETIQUETA_TABLE = "table"
    ETIQUETA_TH = "etiqueta th"
    ETIQUETA_TR = "etiqueta tr"
    ETIQUETA_TD = "etiqueta td"
    ETIQUETA_CAPTION = "etiqueta caption"
    ETIQUETA_COLGROUP = "etiqueta coldgroup"
    ETIQUETA_COL = "etiqueta col"
    ETIQUETA_THEAD = "etiqueta th"
    ETIQUETA_TBODY = "etiqueta tbody"
    ETIQUETA_TFOOT = "etiqueta tfoot"

    # Hipervinculos
    ETIQUETA_A = "etiqueta hipervinculo"

    def __init__(self, token):
        super().__init__()

        self.Token = token

    def ObtenerTipoTokenHTML(self):
        return self.Token

###############################


class AnalizadorLexicohtml():

    def __init__(self):
        super().__init__()

        self.listaTokens = []
        self.listaErroresLex = []
        self.salida = []
        self.estado = 0
        self.fila = 1
        self.col = 1

    #####################

    def Escanear(self, entrada):
        # recorrer texto entrada
        estado = self.estado
        cadena = ""

        for letra in range(len(entrada)):
            """
                Estados de aceptación de tokens HTML

            """

            # ESTADOS DE ANALIZADOR LEXICO
            if estado == 0:

                if entrada[letra] == "<":
                    cadena += entrada[letra]
            ##
            elif estado == 1:

                if entrada[letra].isdigit():
                    cadena += entrada[letra]
                elif entrada[letra] == ">":
                    cadena += entrada[letra]
            ##
            elif estado == 2:

                # ESTADO DE ACEPTACIÓN ETIQUETA
                # Clasificar el Token
                pass

    #####################

    def AgregarToken(self, cadena):

        # clasificar las etiquetas para agregarlas a la lista
        if cadena == "<p>":
            token = TokenHTML(TokenHTML.ETIQUETA_p)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "h1":
            token = TokenHTML(TokenHTML.ETIQUETA_H1)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ## 
        elif cadena == "h2":
            token = TokenHTML(TokenHTML.ETIQUETA_H2)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "h3":
            token = TokenHTML(TokenHTML.ETIQUETA_H1)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
                