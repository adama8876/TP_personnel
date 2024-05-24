from role import Role
from utilisateur import Utilisateur

class Apprenant(Utilisateur):
    def __init__(self, idUser, prenom, nom, email):
        super().__init__(idUser, prenom, nom, email, Role.APPRENANT)

    def afficherApprenant(self):
        return self.afficherUtilisateur()  # Reuse the method from Utilisateur
    
    