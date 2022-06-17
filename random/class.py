class Eleve:
    def __init__(self,nom,age,ecole):
        self.nom = nom
        self.age = age
        self.ecole = ecole



    def appeler_eleve(self):
        return f'Bonjour {self.nom}'

    def presenter_eleve(self):
        return f"Je suis {self.nom}, j'ai {self.age} ans et je vais au {self.ecole}"


eleve1 = Eleve('peres',14,'lcb')
eleve2 = Eleve('mahouna',15,'jean mermoz')


# attributs
print(eleve1.nom)
print(eleve1.age)
print(eleve1.ecole)

#methodes
print(eleve1.appeler_eleve())
print(eleve1.presenter_eleve())
print(eleve2.presenter_eleve())