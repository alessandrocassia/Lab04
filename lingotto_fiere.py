from csv import reader

from stand import Stand
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.lista_stand = []
        self.lista_espositori = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r") as csvfile:
                file = reader(csvfile)
                lista_record = []
                for line in file:
                    lista_record.append(line) #per questioni di ordine salvo tutto qui, in modo da lavorare fuori
                                              #dal blocco with e dal blocco try

        except FileNotFoundError:
            raise FileNotFoundError("Non è stato possibile leggere il file")

        #creazione degli oggetti stand ed espositore
        for record in lista_record:
            if len(record) == 3: #è un espositore
                e = Espositore(record[0], record[1], record[2] ) #creo oggetto espositore
                self.lista_espositori.append(e)

            elif len(record) == 4: #è uno stand (base)
                s = Stand(record[0], record[1], record[2], record[3]) #creo un oggetto espositore
                self.lista_stand.append(s)

            elif len(record) == 5: #è uno stand premium oppure uno stand dotato di prese
                if record.isstring(): #ho uno stand premium
                    pass
                elif record.isint(): #ho uno stand dotato di prese
                    pass





    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
