from role import Role
from utilisateur import Utilisateur

class Apprenant(Utilisateur):
    def __init__(self, idUser, prenom, nom, email, id_ens,role = Role.APPRENANT):
        super().__init__(idUser, prenom, nom, email, role)
        self.id_ens = id_ens

    def afficherApprenant(self):
        return self.afficherUtilisateur()  # Reuse the method from Utilisateur
    
    