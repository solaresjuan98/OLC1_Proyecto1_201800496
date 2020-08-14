import enum
class Tokencss(enum.Enum):
    # selectores
    """ palabras reservadas de html como p, h1, *(universal), ID, clases, pseudoclases div etc...
        reglas con <DIV>...
    """
    # reglas (palabras reservadas), puede tener o no el ';' al final
    # comentarios
    # propiedades
    # delimitadores
    # valores
        # - unidades de medida
        # - ID y numeros
        # - porcentajes
        # - numeros hexadecimales de colores
        # - URL
        # - cadenas
    
    SELECTOR = "Selector"

    def __init__(self, Token, Valor):
        super().__init__()

        self.Token = ""
        self.Valor = ""

    def ObtenerTipoTokenCSS(self):
        return self.Token

    def ObtenerValor(self):
        return self.Valor
