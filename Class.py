# Gabriel Vallieres, 1536504
import re

class Personne(object):
    # Méthode d'access
    def getnom(self):
        return self.__nom
    def setnom(self, value):
        if re.match(r'^[A-Z][a-zA-Z]{6,20}$', value):
            self.__nom = value
        else:
            raise ValueError("Doit commencer par une lettre majuscule et d'une longueur de 6 à 20 lettres alphabétiques")

    def getprenom(self):
        return self.__prenom
    def setprenom(self, value):
        if re.match(r'^[A-Z][a-zA-Z]{6,20}$', value):
            self.__prenom = value
        else:
            raise ValueError("Doit commencer par une lettre majuscule et d'une longueur de 6 à 20 lettres alphabétiques")

    # Constructeur
    def __init__(self, nom: str = "", prenom: str = ""):
        self.setnom(nom)
        self.setprenom(prenom)

    # Méthode d'affichage
    def __str__(self)-> str:
        return f"Nom: {self.getnom()}\nPrénom: {self.getprenom()}\n"

class Employe(Personne):
    # Méthode d'access
    def gettelephone(self):
        return self.__telephone
    def settelephone(self, value):
        self.__telephone = value

    def getcourriel(self):
        return self.__courriel
    def setcourriel(self, value):
        self.__courriel = value

    # Constructeur
    def __init__(self, nom, prenom, telephone: str = "", courriel: str = ""):
        super().__init__(nom, prenom)
        self.settelephone(telephone)
        self.setcourriel(courriel)
    # Méthode d'affichage
        return f"{super().__str__()}, Telephone: {self.__gettelephone()}\nCourriel: {self.getcourriel()}\n"

test1 = Personne("Gsdghsghfgh", "Gsfghfgdhfxg")
print(test1)
test2 = Employe(test1, "okk", "ok")
