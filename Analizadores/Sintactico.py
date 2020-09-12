
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

            