
from enum import Enum
from io import open
import os


class TokenHTML(Enum):

    # etiquetas de apertura
    ETIQUETA_HTML = "etiqueta html"
    ETIQUETA_BODY = "etiqueta body"
    ETIQUETA_HEAD = "etiqueta head"
    ETIQUETA_TITLE = "etiqueta title"

    # titulos y subtitulos
    ETIQUETA_H1 = "etiqueta h1"
    ETIQUETA_H2 = "etiqueta h2"
    ETIQUETA_H3 = "etiqueta h3"
    ETIQUETA_P = "p"

    # imagen
    ETIQUETA_IMG = "etiqueta img"

    # Listas e indices
    ETIQUETA_UL = "etiqueta ul"
    ETIQUETA_LI = "etiqueta li"
    ETIQUETA_OL = "etiqueta ol"

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
                estado 4 -> etiquetas html
                estado 5 -> texto que esta entra las etiquetas de apertura y de cierre

            """
            # ESTADOS DE ANALIZADOR LEXICO
            if estado == 0:
                #print("Estoy en estado 0 ", entrada[letra])
                cadena = ""
                range(len(entrada) - 1)
                if entrada[letra] == "<":
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 1
                elif entrada[letra].isdigit() or entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 5
                elif entrada[letra] == "\n":
                    self.fila += 1
                    self.col = 1
                elif entrada[letra] == "\t":
                    self.col += 4
            ##
            elif estado == 1:
                #print("Estoy en estado 1", entrada[letra])
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 3
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 2
            ##
            elif estado == 2:
                #print("Estoy en estado 2", entrada[letra])
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 3
            ##
            elif estado == 3:
                #print("Estoy en estado 3", entrada[letra])
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\"":
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 6
                elif entrada[letra] == "\n":
                    cadena += entrada[letra]
                    self.fila += 1
                elif entrada[letra] == ">":
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 4
            ##
            elif estado == 4:
                #print("Estoy en estado 4")
                # Estado de aceptación de cualquier etiqueta html
                self.AgregarToken(cadena)
                range(len(entrada) - 1)
                cadena = ""
                estado = 0
            ##
            elif estado == 5:

                if entrada[letra].isalpha() or entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 5
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.col += 1
                    #estado = 5
                elif entrada[letra] == "<":
                    ## agregar lo que se llevaba antes a la lista
                    self.listaTokens.append(["Texto / contenido", cadena])
                    self.col += 1
                    ## borro la cadena
                    cadena = ""
                    ## concateno la nueva cadena y la mando al estado 1 para reconocer una etiqueta
                    cadena += entrada[letra]
                    estado = 1

                # detectar tambien simbolos
                else:
                    self.listaTokens.append(["Texto / contenido", cadena])
                    cadena = ""
                    estado = 0
            ##
            elif estado == 6:

                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "=":
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ":":
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\"":
                    cadena += entrada[letra]
                    self.col += 1
                    estado = 3

    #####################

    def AgregarToken(self, cadena):
        ## print(cadena)
        # clasificar las etiquetas para agregarlas a la lista
        if cadena == "<html>" or cadena == "</html>":
            token = TokenHTML(TokenHTML.ETIQUETA_HTML)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "<head>" or cadena == "</head>":
            token = TokenHTML(TokenHTML.ETIQUETA_HEAD)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "<title>" or cadena == "</title>":
            token = TokenHTML(TokenHTML.ETIQUETA_TITLE)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "<body>" or cadena == "</body>":
            token = TokenHTML(TokenHTML.ETIQUETA_BODY)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "<p>" or cadena == "</p>":
            token = TokenHTML(TokenHTML.ETIQUETA_P)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        # SUBTITULOS
        elif cadena == "<h1>" or cadena == "</h1>":
            token = TokenHTML(TokenHTML.ETIQUETA_H1)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "<h2>" or cadena == "</h2>":
            token = TokenHTML(TokenHTML.ETIQUETA_H2)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "<h3>" or cadena == "</h3>":
            token = TokenHTML(TokenHTML.ETIQUETA_H3)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##

        # LISTAS
        elif cadena == "<li>" or cadena == "</li>":
            token = TokenHTML(TokenHTML.ETIQUETA_LI)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<ul>" or cadena == "</ul>":
            token = TokenHTML(TokenHTML.ETIQUETA_UL)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])

        # TABLAS
        elif cadena == "<table>" or cadena == "</table>":
            token = TokenHTML(TokenHTML.ETIQUETA_TABLE)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<th>" or cadena == "</th>":
            token = TokenHTML(TokenHTML.ETIQUETA_TH)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<td>" or cadena == "</td>":
            token = TokenHTML(TokenHTML.ETIQUETA_TD)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<tr>" or cadena == "</tr>":
            token = TokenHTML(TokenHTML.ETIQUETA_TR)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])   
        elif cadena == "<caption>" or cadena == "</caption>":
            token = TokenHTML(TokenHTML.ETIQUETA_CAPTION)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<colgroup>" or cadena == "</colgroup>":
            token = TokenHTML(TokenHTML.ETIQUETA_COLGROUP)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<col>" or cadena == "</col>":
            token = TokenHTML(TokenHTML.ETIQUETA_COL)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<thead>" or cadena == "</thead>":
            token = TokenHTML(TokenHTML.ETIQUETA_THEAD)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<tbody>" or cadena == "</tbody>":
            token = TokenHTML(TokenHTML.ETIQUETA_TBODY)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif cadena == "<tfoot>" or cadena == "</tfoot>":
            token = TokenHTML(TokenHTML.ETIQUETA_TFOOT)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif "img" in cadena:
            token = TokenHTML(TokenHTML.ETIQUETA_IMG)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
    
    #####################

    def imprimirListaTokens(self):
        contenido = ""

        for token in self.listaTokens:
            contenido += "Tipo: "\
                + str(token[0]) +\
                " VALOR: "\
                + str(token[1]) +\
                "\n"\

        return contenido


    def GenerarReporteErrores(self):
        pass

