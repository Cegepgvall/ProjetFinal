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
    def getcode(self):
        return self.__code
    def setcode(self, value):
        self.__code = value

    def getfonction(self):
        return self.__fonction
    def setfonction(self, value):
        self.__fonction = value

    # Constructeur
    def __init__(self, setnom, setprenom, code: int = 0, fonction: str = ""):
        super().__init__(setnom)
        super().__init__(setprenom)
        self.setcode(code)
        self.setfonction(fonction)
    # Méthode d'affichage
        return f"{super().__str__(getnom)}\n{super().__str__(getprenom)}\nCode: {self.__getcode()}\nFonction: {self.getFonction()}\n"

class Client(Personne):
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
    def __init__(self, setnom, setprenom, telephone: str = "", courriel: str = ""):
        super().__init__(setnom)
        super().__init__(setprenom)
        self.settelephone(telephone)
        self.setcourriel(courriel)
    # Méthode d'affichage
        return f"{super().__str__(getnom)}\n{super().__str__(getprenom)}\nTelephone: {self.__gettelephone()}\nCourriel: {self.getcourriel()}\n"

class Reparation(object):
    # Méthodes d'access
    def getcode(self):
        return self.__code
    def setcode(self, value):
        self.__code = value

    def getdescription(self):
        return self.__description
    def setdescription(self, value):
        self.__description = value

    def getmontant(self):
        return self.__montant
    def setmontant(self, value):
        self.__montant = value

    def getdatereparation(self):
        return self.__datereparation
    def setdatereparation(self, value):
        self.__datereparation = value

    def getcodeemploye(self):
        return self.__codeemploye
    def setcodeemploye(self, value):
        self.__codeemploye = value

    # Constructeur
    def __init__(self, code: int = 0, description: str = "", montant: float = 0, datereparation: str = "", codeemploye: int = 0):
        self.setcode(code)
        self.setdescription(description)
        self.setmontant(montant)
        self.setdatereparation(datereparation)
        self.setcodeemploye(codeemploye)

    # Méthodes d'affichage
    def __str__(self)-> str:
        return f"Code: {self.getcode()}\nDescription: {self.getdescription()}\nMontant: {self.getmontant()}\nDate: {self.getdatereparation()}\nCode Employer: {self.getcodeemploye()}\n"



test1 = Personne("Gsdghsghfgh", "Gsfghfgdhfxg")
print(test1)
#test2 = Employe("GAFafdsdfg", "Oksdfdg", "okk", "ok")
#print(test2)
test3 = Reparation(2, "ROUILLE", 10.54, "3 avril", 4)
print(test3)
