# Gabriel Vallieres, 1536504
import re
import json
import jsonpickle

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

class Voiture(object):
    # Méthodes d'access
    def getnumeroplaque(self):
        return self.__numeroplaque
    def setnumeroplaque(self, value):
        self.__numeroplaque = value

    def getmarque(self):
        return self.__marque
    def setmarque(self, value):
        self.__marque = value

    def getmodele(self):
        return self.__modele
    def setmodele(self, value):
        self.__modele = value

    def getcouleur(self):
        return self.__couleur
    def setcouleur(self, value):
        self.__couleur = value

    def getannee(self):
        return self.__annee
    def setannee(self, value):
        self.__annee = value

    def getproprietaire(self):
        return self.__proprietaire
    def setproprietaire(self, value):
        self.__proprietaire = value

    def getreparations(self):
        return self.__reparations
    def setreparations(self, value):
        self.__reparations = value

    # Constructeur
    def __init__(self, numeroplaque: str = "", marque: str = "", modele: str = "", couleur: str = "", annee: int = 0, proprietaire:Client = None, reparations: list[Reparation] = None):
        self.setnumeroplaque(numeroplaque)
        self.setmarque(marque)
        self.setmodele(modele)
        self.setcouleur(couleur)
        self.setannee(annee)
        self.setproprietaire(proprietaire)
        self.setreparations(reparations)

    # Méthodes utilitaires
    def ajouterreparation(self, element: Reparation)->None:
        liste = []
        liste.append(element)

class Garage(object):
    # Méthode d'access
    def getnom(self):
        return self.__nom
    def setnom(self, value):
        self.__nom = value

    def getadresse(self):
        return self.__adresse
    def setadresse(self, value):
        self.__adresse = value

    def gettelephone(self):
        return self.__telephone
    def settelephone(self, value):
        self.__telephone = value

    def getemployes(self):
        return self.__employes
    def setemployes(self, value):
        self.__employes = value

    def getvoitures(self):
        return self.__voitures
    def setvoitures(self, value):
        self.__voitures = value

    # Constructeur
    def __init__(self, nom: str = "", adresse: str = "", telephone: str = "", employes: list[Employe] = None, voitures: list[Voiture] = None):
        self.setnom(nom)
        self.setadresse(adresse)
        self.settelephone(telephone)
        self.setemployes(employes)
        self.setvoitures(voitures)
        listeEmployes = []
        listeVoiture = []

    # Méthodes utilitaire
    @classmethod
    def serialisergarage(cls, element: object, fichier: str)-> None:
    #ouvrir le fichier (creer le stream)
        path: Path = Path(fichier)
        if path.is_file():
            stream=path.open('w')
            #serialiser la valeur vers le fichier
            json.dump(element, stream, indent=4, separators= (',',':'))
            #fermer le stream
            stream.flush()
            stream.close()
        else:
            raise Exception('fichier incorrect')

    @classmethod
    def deserialisergarage(cls, fichier: str)-> object:
        #ouvrir le fichier (creer le stream)
        path: Path = Path(fichier)
        if path.exists():
            stream = path.open('r')
            #deserialiser le fichier vers un objet liste de compte
            liste:list = json.load(stream)
            #fermer le stream
            stream.close()
            #retourner le resultat
            return liste
        else:
            raise Exception('fichier inexistant')

    def ajoutervoiture(self, element:Voiture)-> None:
        self.__voitures.append(element)

    def getvoiture(self, plaquevoiture: str)-> Voiture:



test1 = Personne("Gsdghsghfgh", "Gsfghfgdhfxg")
print(test1)
#test2 = Employe("GAFafdsdfg", "Oksdfdg", "okk", "ok")
#print(test2)
test3 = Reparation(2, "ROUILLE", 10.54, "3 avril", 4)
print(test3)
