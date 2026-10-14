"""File di definizione della classe Espositore"""

class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

        self.__stand_associato = None

    def __str__(self):
        return f"Codice espositore: {self.__codice}, Nome: {self.__nome}, Cognome: {self.__cognome}"

    @property
    def codice(self):
        return self.__codice

    @property
    def stand_associato(self):
        return self.__stand_associato
    @stand_associato.setter
    def stand_associato(self, stand_associato):
        self.__stand_associato = stand_associato
