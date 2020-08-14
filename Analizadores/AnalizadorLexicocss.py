
#from Tokencss import *
#from tkinter import messagebox as MessageBox

class AnalizadorLexicocss():

    def __init__(self):
        super().__init__()

        self.auxLex = ""
        self.listaTokens = []
        self.estado = 0

    def ClasificarToken(self):
        # Clasificar los tokens de la lista
        pass

    def AgregarToken(self, Tokencss):
        #
        #token = Tokencss("ENTRADA", "hola")
        # print(self.listaTokens[:])
        pass

    def Escanear(self, entrada):
        # Recorrer texto de entrada
        estado = self.estado
        char = ""

        for letra in range(len(entrada)):
            if estado == 0:
                char += entrada[letra]
                print("Estoy en estado 0")
                range(len(entrada) - 1)
                if entrada[letra] == "/":
                    estado = 1

            elif estado == 1:
                print("Estoy en estado 1")
                if entrada[letra] == "*":
                    print("lei un asterisco")
                elif entrada[letra] ==" ":
                    print("lei un espacio")
