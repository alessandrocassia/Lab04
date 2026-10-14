"""File di definizione della classe Stand, ma anche le sue classi figlie StandPremium e StandConPrese"""

class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo,posizione):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__posizione = posizione


class StandConPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__numero_prese = numero_prese
