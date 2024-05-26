from utilisateur import Utilisateur
from role import Role
from enseignant import Enseignant



class Admin(Utilisateur):
    def __init__(self, idUser, prenom, nom, email, role=Role.ADMIN):
        super().__init__(idUser, prenom, nom, email, role)

    def Ajouter_enseignant(self, idEnseignant, nom, prenom, email, mot_de_passe, role, liste_enseignants):
        enseignant = Enseignant(idEnseignant, prenom, nom, email, mot_de_passe, role)
        liste_enseignants.append(enseignant)
        return f"Enseignant avec l'ID {idEnseignant} a été ajouté avec succès."

# Fonction pour modifier un enseignant par son ID
    def modifier_enseignant_par_id(idEnseignant, nom, prenom, email, mot_de_passe, liste_enseignants):
        for enseignant in liste_enseignants:
            if enseignant.idEnseignant == idEnseignant:
                enseignant.nom = nom
                enseignant.prenom = prenom
                enseignant.email = email
                enseignant.mot_de_passe = mot_de_passe
                return f"L'enseignant avec l'ID {idEnseignant} a été modifié avec succès."
        return f"L'enseignant avec l'ID {idEnseignant} n'existe pas dans notre base de données."




    def afficher_liste_enseignants(self, liste_enseignants):
        print("*** Liste des enseignants ***")
        for enseignant in liste_enseignants:
            print(enseignant)
    # def __str__(self):
    #     return f"Enseignant(ID: {self.idEnseignant}, Nom: {self.nom}, Prénom: {self.prenom}, Email: {self.email})"
    