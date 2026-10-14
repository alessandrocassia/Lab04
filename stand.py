"""File di definizione della classe Stand, ma anche le sue classi figlie StandPremium e StandConPrese"""

class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo

        self.__espositore_associato = None #ovvero è libero

    def __str__(self):
        return f"Codice stand: {self.__codice}, Superficie: {self.__superficie}, Padiglione: {self.__padiglione}, Prezzo(€): {self.__prezzo: .2f}"

    def __lt__(self, other): #funzione per l'ordinamento degli stand in base al loro prezzo
        return self.__prezzo < other.__prezzo


    #accesso agli attributi privati per modifica e lettura
    @property
    def prezzo(self):           #utili per modificare il prezzo in modo leggibile nelle classi figlie
        return self.__prezzo
    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo

    @property
    def espositore_associato(self):
        return self.__espositore_associato
    @espositore_associato.setter
    def espositore_associato(self, espositore_associato):
        self.__espositore_associato = espositore_associato

    @property
    def codice(self):
        return self.__codice


#definizione delle classi figlie
class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__posizione = posizione
        self.prezzo = prezzo * 1.3 #sovrapprezzo

    def __str__(self):
        return f"Stand di tipo Premium | {super().__str__()}, Posizione: {self.__posizione}"


class StandConPrese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, numero_prese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__numero_prese = numero_prese
        self.prezzo = self.prezzo * (1 + 0.07 * numero_prese) #sovrapprezzo

    def __str__(self):
        return f"Stand dotato di prese | {super().__str__()}, Numero Prese: {self.__numero_prese}"


