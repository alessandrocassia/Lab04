from csv import reader

from stand import Stand, StandPremium, StandConPrese
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

    def __str__(self):
        return f"Nome: {self.nome}"

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
                s = Stand(record[0], int(record[1]), record[2], float(record[3])) #creo un oggetto espositore
                self.lista_stand.append(s)

            elif len(record) == 5: #è uno stand premium oppure uno stand dotato di prese

                if record[4].isdigit(): #ho uno stand dotato di prese
                    scp = StandConPrese(record[0], int(record[1]), record[2], float(record[3]), int(record[4])) #creo un oggetto stand con prese
                    self.lista_stand.append(scp)

                else: #ho uno stand premium
                    sp = StandPremium(record[0], int(record[1]), record[2], float(record[3]), record[4]) #creo un oggetto stand premium
                    self.lista_stand.append(sp)


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        #in base al tipo di problema che riscontro, lancio un'eccezione diversa

        #verifica di esistenza dello stand
        stand_trovato  = None
        for stand in self.lista_stand:
            if stand.codice == codice_stand:
                stand_trovato = stand

        if stand_trovato is None:
            raise Exception("Il codice stand inserito non è presente nei nostri registri")


        #verifica di esistenza dell'espositore
        espositore_trovato = None
        for espositore in self.lista_espositori:
            if espositore.codice == codice_espositore:
                espositore_trovato = espositore

        if espositore_trovato is None:
            raise Exception("Il codice espositore inserito non è presente nei nostri registri")


        #verifica che lo stand sia libero
        if stand_trovato.espositore_associato is not None:
            raise Exception("Lo stand indicato è già stato occupato da un espositore")
        else:
            stand_trovato.espositore_associato = espositore_trovato


        #verifica che l'espositore sia libero
        if espositore_trovato.stand_associato is not None:
            raise Exception("L'espositore indicato è già stato associato ad uno stand")
        else: espositore_trovato.stand_associato = stand_trovato

        # TODO ALE
        #perché non provi a creare delle funzioni che vengono chiamate nella funzione grande? per maggiore pulizia del codice

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
