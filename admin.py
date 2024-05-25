from utilisateur import Utilisateur
from role import Role
from enseignant import Enseignant
class Admin(Utilisateur):
    def __init__(self, idUser, prenom, nom, email, role=Role.ADMIN):
          super().__init__(idUser, prenom, nom, email, role)

    def Ajouter_enseignant(self, idEnseignant, nom, prenom,email, mot_de_passe, role, liste_enseignants):
        enseignant = Enseignant(idEnseignant, prenom, nom, email, mot_de_passe, role)
        liste_enseignants.append(enseignant)
        for enseignant in liste_enseignants:
            print(enseignant)
        return f"Utilisateur avec idUser {idEnseignant} a été ajouté avec success."