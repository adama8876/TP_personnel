from utilisateur import Utilisateur
from role import Role
from enseignant import Enseignant



class Admin(Utilisateur):
    def __init__(self, idUser, prenom, nom, email,mot_de_passe, role=Role.ADMIN):
        super().__init__(idUser, prenom, nom,mot_de_passe, email, role)

    def Ajouter_enseignant(self, idUser, nom, prenom, email, mot_de_passe, role, liste_enseignants):
        enseignant = Enseignant(idUser, prenom, nom, email, mot_de_passe, role)
        liste_enseignants.append(enseignant)
        return f"Enseignant avec l'ID {idUser} a été ajouté avec succès."

# Fonction pour modifier un enseignant par son ID
    def modifier_enseignant_par_id(self,idUser, nom, prenom, email, mot_de_passe, liste_enseignants):
        for enseignant in liste_enseignants:
            if enseignant.idUser == idUser:
                enseignant.nom = nom
                enseignant.prenom = prenom
                enseignant.email = email
                enseignant.mot_de_passe = mot_de_passe
                return f"L'enseignant avec l'ID {idUser} a été modifié avec succès."
        return f"L'enseignant avec l'ID {idUser} n'existe pas dans notre base de données."
    

    # Fonction pour supprimer un enseignant par son ID
    def supprimer_enseignant_par_id(self, idUser, liste_enseignants):
        for enseignant in liste_enseignants:
            if enseignant.idUser == idUser:
                liste_enseignants.remove(enseignant)
                return f"L'enseignant avec l'ID {idUser} a été supprimé avec succès."
        return f"L'enseignant avec l'ID {idUser} n'existe pas dans notre base de données."




    def afficher_liste_enseignants(self, liste_enseignants):
        print("*** Liste des enseignants ***")
        for enseignant in liste_enseignants:
            print(enseignant)
    # def __str__(self):
    #     return f"Enseignant(ID: {self.idUser}, Nom: {self.nom}, Prénom: {self.prenom}, Email: {self.email})"
    