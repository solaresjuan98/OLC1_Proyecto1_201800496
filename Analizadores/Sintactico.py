from io import open
import os

class Sintactico():

    def __init__(self):
        super().__init__()

        self.listaTokens = []
        self.pila = []
        self.ErrorSintactico = True
        self.listaReporte = []

    def pilaVacia(self):
        return self.pila == []

    def apilar(self, t):
        self.pila.insert(0, t)

    def desapilar(self):
        self.pila.pop(0)

    def Parse(self, lista):
        #elemento = lista[1]
        try:
            for expresion in lista:
                print(" >> Expresion a evaluar", expresion)
                for caracter in range(len(expresion)):
                    
                    if (expresion[caracter] == "+" or expresion[caracter] == "-" or expresion[caracter] == "/" or expresion[caracter] == "*") and (expresion[caracter+1] == "+" or expresion[caracter+1] == "-" or expresion[caracter+1] == "*" or expresion[caracter+1] == "/"):
                        print("error")
                        ## mandarlo como error
                        self.listaReporte.append([expresion, "INCORRECTO"])
                        self.pila = []
                        break
                    elif expresion[caracter] == "(":
                        print("apilando")
                        self.apilar("-")
                    elif expresion[caracter] == ")":
                        print("desapilando")
                        self.desapilar()
                    elif (expresion[caracter] == "(") and (expresion[caracter+1] == "+" or expresion[caracter+1] == "-" or expresion[caracter+1] == "*" or expresion[caracter+1] == "/"): 
                        self.listaReporte.append([expresion, "INCORRECTO"])
                        self.pila = []
                        break
                    elif expresion[caracter] == "\n":
                        ## en esta parte validar parentesis
                
                        if self.pilaVacia:
                            self.listaReporte.append([expresion, "CORRECTO"])
                            self.pila = []
                        else:
                            self.listaReporte.append([expresion, "INCORRECTO"])
                            self.pila = []

                        print("Salto de linea")
        except:
            pass

    def mostrarReporte(self):
        result = ""
        for resultado in self.listaReporte:
            
            result += resultado[0]
            result += resultado[1]

        return result

    def GenerarReporteErrores(self):
        # Generar reporte de errores y crea el archivo de acuerdo al directorio dado al inicio del archivo JS
        contador = 1  # contador del numero de errores
        reporte = open("Reportes/ReporteRMT.html", "w")

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
                    "<h2>Analizador .rmt</h2>"\
                    "</div>"\
                    "<div class=\"clearfix\"></div>"\
                    "</div>"\
                    "</header>"\
                    "<section id=\"content\">"\
                    "<h2 class=\"subtitle\">Resultados</h2>"\
                    "<div id=\"tasks\">"\
                    "<br><br>"\
                    "<table class=\"card\">"\
                    "<tr>"\
                    "<th>No</th>"\
                    "<th>Expresion</th>"\
                    "<th>Resultado</th>"\
                    "<th></th>"\
                    "</tr>"\

        reporte.write(contenido)

        for resultado in self.listaReporte:
            contenido2 = "<tr>"\
                "<td>"\
                + str(contador) +\
                "</td>"\
                "<td>"\
                + resultado[0] +\
                "</td>"\
                "<td>"\
                + resultado[1] +\
                "</td>"\
                "<td>"\
                ""\
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
            "C:\\Users\\jsola\\Desktop\\Proyecto1_Compiladores\\Reportes\\ReporteRMT.html")

        
            