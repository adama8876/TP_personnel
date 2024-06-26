from utilisateur import Utilisateur
from role import Role
from apprenant import Apprenant

# enseignant.py
class Enseignant:
    def __init__(self, idEnseignant, nom, prenom, email, mot_de_passe, role):
        self.idEnseignant = idEnseignant
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.role = role

    def __str__(self):
        return f"ID: {self.idEnseignant}, Nom: {self.nom}, Prénom: {self.prenom}, Email: {self.email}, Role: {self.role}"



    def recupe_apprenant_par_id(self, id, liste_apprenants) -> Apprenant|None:
        for i in range(len(liste_apprenants)):
            if(liste_apprenants[i].idUser== id):
                return liste_apprenants[i]
        return None
        

    def creer_apprenant(self, idApprenant, prenom, nom, email, liste_apprenants):
        apprenant = Apprenant(idApprenant, prenom, nom, email, self.idUser)
        liste_apprenants.append(apprenant)
        return apprenant

    def modifier_apprenant(self, apprenant_id, new_prenom, new_nom, new_email, liste_apprenants):
        for apprenant in liste_apprenants:
            if apprenant.idUser == apprenant_id:
                apprenant.prenom = new_prenom
                apprenant.nom = new_nom
                apprenant.email = new_email
                return True  # Modification réussie
        return False  # L'apprenant n'a pas été trouvé

    def supprimer_apprenant(self, apprenant_id, liste_apprenants):
        for apprenant in liste_apprenants:
            if apprenant.idUser == apprenant_id:
                liste_apprenants.remove(apprenant)
                return True  # Suppression réussie
        return False  # L'apprenant n'a pas été trouvé


    def afficher_liste_apprenants(self, liste_apprenants):
        if not liste_apprenants:
            print("Aucun apprenant dans la liste.")
        else:
            print("Liste des apprenants supervisés par l'enseignant:")
            for apprenant in liste_apprenants:
                print(f"ID : {apprenant.idUser}, Nom : {apprenant.nom}, Prénom : {apprenant.prenom}, Email : {apprenant.email} Ens_id : {apprenant.id_ens}")
