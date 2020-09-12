
# importar clase Token
from Analizadores.Lexrmt import Token


class AnalizadorSintactico():

    def __init__(self):
        super().__init__()

        self.ErrorSintactico = False
        self.tokenActual = Token
        self.posicion = 0
        self.listaTokens = []

    # recibe como parametro la lista de tokens
    def Parsear(self, listaTokens):
        posicion = self.posicion
        self.listaTokens = listaTokens
        self.tokenActual = listaTokens[posicion][1]

        print("inicial -> ", self.tokenActual)

        # La lista de tokens está de la forma [Tipo, simbolo]  [0][1]
        self.__Inicio()

    def __Inicio(self):

        # Inicio -> Lista
        self.__Lista()
        

    def __Lista(self):

        # Lista -> Expresion ListaP
        self.__Expresion()
        self.__ListaP()
        """if self.tokenActual == "(":
            # print(True)
            self.__Expresion()
            self.__ListaP()
        """
        pass

    def __Expresion(self):

        # Expresion -> E
        print("EXPRESION")
        self.__E()

    def __ListaP(self):
        print("LISTAP")
        # ListaP -> Expresion ListaP
        #           | Epsilon
        self.__Expresion()
        self.__ListaP()

    def __E(self):
        print("E")
        # E -> T EP
        self.__T()
        self.__EP()

    def __T(self):
        print("T")
        # T -> F TP
        self.__F()
        self.__TP()

    def __EP(self):
        print("EP")
        # EP -> + T EP
        #     | - T EP
        #     | EPSILON
        # meter los if
        if self.tokenActual == "+":
            print("Signo +")
            self.Parea(self.tokenActual)
            self.__T()
            self.__EP()
        elif self.tokenActual == "-":
            print("Signo -")
            self.Parea(self.tokenActual)
            self.__T()
            self.__EP()
        else:
            # EPSILON
            pass

    def __F(self):

        if self.tokenActual.isdigit():

            self.Parea(self.tokenActual)
            
        
        elif self.tokenActual == "(":

            self.Parea(self.tokenActual)
            self.__E()
            self.Parea(self.tokenActual)
        else:

            self.Parea(self.tokenActual)
            pass

    def __TP(self):
        
        if self.tokenActual == "*":
            print("Signo *")
            self.Parea(self.tokenActual)
            self.__F
            self.__TP()
        elif self.tokenActual == "/":
            print("Signo /")
            self.Parea(self.tokenActual)
            self.__F()
            self.__TP()
        else:
            # EPSILON
            pass

    # o salto de linea
    def __SaltodeLinea(self):
        
        if self.tokenActual == "\n":
            self.Parea(self.tokenActual)

        else:
            print("error :V")

    def Parea(self, tipoToken):

        # Cuando es un error sintactico
        if self.ErrorSintactico:
            print("error sintactico")
            if self.posicion < len(self.listaTokens) - 1:
                self.posicion += 1
                self.tokenActual = self.listaTokens[self.posicion][1]

                if self.tokenActual == "\n":
                    self.ErrorSintactico = False

            else:
                print(":v")

        # Cuando no lo es
        else:

            if self.tokenActual == tipoToken:

                if self.posicion < len(self.listaTokens) - 1:
                    self.posicion += 1
                    self.tokenActual = self.listaTokens[self.posicion][1]
                else:
                    self.ErrorSintactico = True
