# Gabriel Vallieres, 1536504
import re

class Personne(object):
    # Méthode d'access
    def getnom(self):
        return self.__nom
    def setnom(self, value):
        if re.match(r'^[A-Z]{1})\d{6,20}$', value):
            self.__nom = value
        else:
            raise ValueError("Doit commencer par une lettre majuscule et d'une longueur de 6 à 20 lettres alphabétiques")

    def getprenom(self):
        return self.__prenom
    def setprenom(self, value):
        if re.match(r'^[A-Z]{1})\d{6,20}$', value):
            self.__prenom = value
        else:
            raise ValueError("Doit commencer par une lettre majuscule et d'une longueur de 6 à 20 lettres alphabétiques")

    # Constructeur
    def __init__(self, nom: str = "", prenom: str = ""):
        self.setnom(nom)
        self.setnom(prenom)
