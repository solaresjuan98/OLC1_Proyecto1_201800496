
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
    ETIQUETA_H4 = "etiqueta h4"
    ETIQUETA_H5 = "etiqueta h5"
    ETIQUETA_H6 = "etiqueta h6"

    ETIQUETA_P = "etiqueta p"
    ETIQUETA_BR = "etiqueta br"

    # imagen
    ETIQUETA_IMG = "etiqueta img"

    ETIQUETA_STYLE = "etiqueta style"

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

    # Otros
    COMENTARIO = "Comentario"

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
        self.salida = ""
        self.estado = 0
        self.fila = 1
        self.col = 1
        # bandera de archivo
        self.bandera = False
        # ruta donde se almacenara la salida
        self.rutaSalida = ""

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
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 1
                elif entrada[letra].isdigit() or entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 5
                elif entrada[letra] == "\n":
                    self.salida += entrada[letra]
                    self.fila += 1
                    self.col = 1
                elif entrada[letra] == "\t":
                    self.salida += entrada[letra]
                    self.col += 4
                ## AGREGANDO SIMBOLOS (QUE VIENEN FUERA DE LAS ETIQUETAS)
                # QUE DENTRO DE LA ETIQUETA SERÍA ERROR LEXICO

                elif entrada[letra] == "@":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "#":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "$":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "¿":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "?":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "!":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "¡":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "/":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "&":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "%":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "=":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "-":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "+":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "*":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "~":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\\":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "¬":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "°":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\"":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "'":
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "|":
                    self.salida += entrada[letra]
                    self.col += 1    
            ##
            elif estado == 1:
                #print("Estoy en estado 1", entrada[letra])
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 3
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 2
                elif entrada[letra] == "!":
                    self.salida += entrada[letra]
                    #cadena += entrada[letra]
                    self.col += 1
                    estado = 7
            ##
            elif estado == 2:
                #print("Estoy en estado 2", entrada[letra])
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 3
            ##
            elif estado == 3:
                #print("Estoy en estado 3", entrada[letra])
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
                elif entrada[letra] == "=":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                # Si se reconoce una comilla doble
                elif entrada[letra] == "\"":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 6
                elif entrada[letra] == "\n":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.fila += 1
                elif entrada[letra] == ">":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 4

                # Reconociendo Errores lexicos en HTML
                # - Reconocer el token hasta el momento?
                else:
                    error = ""
                    error += entrada[letra]
                    self.AgregarError(error, self.fila, self.col)
                    error = ""
                    #cadena = ""
                    #estado = 0
                """
                elif entrada[letra] == "@":
                    
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    estado = 0
                    cadena = ""
                elif entrada[letra] == "#":
                    self.AgregarError(entrada[letra], self,fila, self.col)
                    self.col += 1
                    cadena = ""
                elif entrada[letra] == "%":
                    self.AgregarError(entrada[letra], self.fila, self.col)
                    self.col += 1
                    estado = 0
                    cadena = """
            ##
            elif estado == 4:
                #print("Estoy en estado 4")
                if entrada[letra].isalpha():
                    self.AgregarToken(cadena)
                    cadena = ""
                    self.salida += entrada[letra]
                    cadena += entrada[letra]
                    estado = 5
                else:
                # Estado de aceptación de cualquier etiqueta html
                    self.AgregarToken(cadena)
                    range(len(entrada) - 1)
                    cadena = ""
                    estado = 0

                    if entrada[letra].isalpha():
                        self.salida += entrada[letra]
                        cadena += entrada[letra]
                        estado = 5

                    elif entrada[letra] == "<":
                        cadena += entrada[letra]
                        self.salida += entrada[letra]
                    
                    elif entrada[letra] == ">":
                        cadena += entrada[letra]
                        self.salida += entrada[letra]
            ##
            elif estado == 5:
                #print("Estoy en estado 5")
                #print("Estoy en estado 5 ", entrada[letra])
                if entrada[letra].isalpha() or entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 5
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    #estado = 5
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "@":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "#":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "$":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "¿":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "?":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "!":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "¡":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "&":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "%":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "=":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "+":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "*":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "~":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\\":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "¬":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "°":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\"":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "'":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "|":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1   

                elif entrada[letra] == "<":
                    
                    # agregar lo que se llevaba antes a la lista
                    self.listaTokens.append(["Texto / contenido", cadena])
                    self.col += 1
                    # borro la cadena
                    cadena = ""
                    # concateno la nueva cadena y la mando al estado 1 para reconocer una etiqueta
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    estado = 1

                # detectar tambien simbolos
                else:
                    self.listaTokens.append(["Texto / contenido", cadena])
                    cadena = ""
                    estado = 0
            ##
            elif estado == 6:
                #print("Estoy en estado 6")
                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "=":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ":":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "-":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ";":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\"":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 3
                elif entrada[letra] == "\n":
                    #cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.fila += 1
                    estado = 3
            ##
            elif estado == 7:

                if entrada[letra] == "-":
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 8
            ##
            elif estado == 8:

                if entrada[letra] == "-":
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 9
            ##
            elif estado == 9:

                if entrada[letra].isalpha():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra].isdigit():
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ":":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == " ":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "/":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "\\":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ".":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == ";":
                    cadena += entrada[letra]
                    self.salida += entrada[letra]
                    self.col += 1
                elif entrada[letra] == "-":
                    self.salida += entrada[letra]
                    estado = 10
            ##
            elif estado == 10:
                if entrada[letra] == "-":
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 11
            ##
            elif estado == 11:
                if entrada[letra] == ">":
                    self.salida += entrada[letra]
                    self.col += 1
                    estado = 12
            ##
            elif estado == 12:

                # Aceptando el comentario que contiene la ruta
                token = TokenHTML(TokenHTML.COMENTARIO)
                self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
                aux = cadena.replace("<", "")
                if self.VerificarRuta(aux, 'PATHW:'):

                    cadena.replace("PATHW:", "")
                    self.bandera = True
                cadena = ""
                estado = 0


    #####################

    def AgregarToken(self, cadena):
        # print(cadena)
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
        elif cadena == "<h4>" or cadena == "</h4>":
            token = TokenHTML(TokenHTML.ETIQUETA_H4)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "<h5>" or cadena == "</h5>":
            token = TokenHTML(TokenHTML.ETIQUETA_H5)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        ##
        elif cadena == "<h6>" or cadena == "</h6>":
            token = TokenHTML(TokenHTML.ETIQUETA_H6)
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
        elif "style" in cadena:
            token = TokenHTML(TokenHTML.ETIQUETA_STYLE)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])
        elif "a href" in cadena:
            token = TokenHTML(TokenHTML.ETIQUETA_A)
            self.listaTokens.append([token.ObtenerTipoTokenHTML(), cadena])

    #####################

    def AgregarError(self, caracter, fila, col):
        # validar los errores
        if caracter == "@":
            #print("Error lexico @", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "#":
            # print("Error lexico #", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "|":
            #print("Error lexico |", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "¿":
            #print("error lexico ¿", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "´":
            #print("error lexico ´", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "~":
            #print("error lexico ~", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "^":
            #print("error lexico ^", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "_":
            #print("error lexico _", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "?":
            #print("error lexico ?", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "$":
            #print("error lexico $", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])
        elif caracter == "%":
            #print("error lexico %", "fila:", fila, "col: ", col)
            self.listaErroresLex.append([fila, col, caracter])

    #####################

    def VerificarRuta(self, p1, p2):
        aux = p1.replace(p2, "")
        ruta = ""
        ruta = aux.replace(" ", "")
        ruta = ruta.replace("\\\\", "")
        directorio = ""
        print(ruta)
        #directorio = ruta
        #directorio = os.path.join(directorio)
        
        try:
            if ruta[0] == "c" or ruta[0] == "C" and ruta[1] == ":":
                
                directorio = ""
                directorio = ruta
                directorio = os.path.join(directorio)

                if not os.path.exists(directorio):
                    print("creado")
                    os.mkdir(directorio)

                self.rutaSalida = directorio
                # self.rutaSalida = ruta
                """archivo = open(ruta, "w+")
                archivo.write("prueba jeje")
                archivo.close()"""
        except IndexError:
            pass

        return (' ' + p2 + ' ') in (' ' + p1 + ' ')

    ####################

    def GenerarSalida(self):
        
        archivo = "salida.html"
        rutafinal = ""
        rutafinal += self.rutaSalida
        rutafinal += archivo

        output = open(rutafinal, "w")

        output.write(self.salida)

        output.close()
        
    ####################

    def imprimirListaTokens(self):
        contenido = ""

        for token in self.listaTokens:
            contenido += "Tipo: "\
                + str(token[0]) +\
                " VALOR: "\
                + str(token[1]) +\
                "\n"\

        return contenido

    #####################

    def GenerarReporteErrores(self):

        # Generar reporte de errores y crea el archivo de acuerdo al directorio dado al inicio del archivo JS
        contador = 1  # contador del numero de errores
        reporte = open("Reportes/ErroresHTML.html", "w")

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
                    "<h2>Analizador html</h2>"\
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
            "C:\\Users\\jsola\\Desktop\\Proyecto1_Compiladores\\Reportes\\ErroresHTML.html")

        pass
