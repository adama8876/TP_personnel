from utilisateur import Utilisateur
from role import Role
from apprenant import Apprenant
from groupe import Groupe
from tp import Tp
from datetime import datetime

# enseignant.py
class Enseignant(Utilisateur):
    def __init__(self, idUser, prenom, nom, email,mot_de_passe, role=Role.ENSEIGNANT):
        super().__init__(idUser, prenom, nom, email,mot_de_passe, role)

    def __str__(self):
        return f"ID: {self.idUser}, Nom: {self.nom}, Prénom: {self.prenom}, Email: {self.email}, Role: {self.role}"



    def recupe_apprenant_par_id(self, id, liste_apprenants) -> Apprenant|None:
        for i in range(len(liste_apprenants)):
            if(liste_apprenants[i].idUser== id):
                return liste_apprenants[i]
        return None
    ########################################################################################################    

    def Ajouter_apprenant(self, idUser, prenom, nom, email,mot_de_passe, liste_apprenants):
        apprenant = Apprenant(idUser, prenom, nom, email, mot_de_passe, self.idUser)
        liste_apprenants.append(apprenant)
        return f"Apprenant {nom} {prenom} avec l'ID {idUser} a été ajouté avec succès."
    #######################################################################################################
    def modifier_apprenant(self,idUser, nom, prenom, email, mot_de_passe, liste_apprenants):
        for apprenant in liste_apprenants:
            if apprenant.idUser == idUser:
                apprenant.nom = nom
                apprenant.prenom = prenom
                apprenant.email = email
                apprenant.mot_de_passe = mot_de_passe
                return f"L'apprenant {prenom} avec l'ID {idUser} a été modifié avec succès."
        return f"L'apprenant avec l'ID {idUser} n'existe pas dans notre base de données."


    ##############################################################################################
    def supprimer_apprenant(self, idUser, liste_apprenants):
        for apprenant in liste_apprenants:
            if apprenant.idUser == idUser:
                liste_apprenants.remove(apprenant)
                return f"L'apprenant avec l'ID {idUser} a été supprimé avec succès."
        return f"L'apprenant avec l'ID {idUser} n'existe pas dans notre base de données."

    # def supprimer_apprenant(self, apprenant_id, liste_apprenants):
    #     for apprenant in liste_apprenants:
    #         if apprenant.idUser == apprenant_id:
    #             liste_apprenants.remove(apprenant)
    #             return True  # Suppression réussie
    #     return False  # L'apprenant n'a pas été trouvé


    def afficher_liste_apprenants(self, liste_apprenants):
        if not liste_apprenants:
            print("Aucun apprenant dans la liste.")
        else:
            print("Liste des apprenants supervisés par l'enseignant:")
            for apprenant in liste_apprenants:
                print(f"ID : {apprenant.idUser}, Nom : {apprenant.nom}, Prénom : {apprenant.prenom}, Email : {apprenant.email} Ens_id : {apprenant.id_ens}")
######################################################################################################################

    def creer_groupe(self, idgroupe, nom,liste_groupes):
        groupe= Groupe(idgroupe, nom)
        liste_groupes.append(groupe)
        return f" {nom} avec l'ID {idgroupe} a été créé avec succès"
    
    def supprimer_groupe(self, idgroupe, liste_groupes):
        for groupe in liste_groupes:
            if groupe.idgroupe == idgroupe:
                liste_groupes.remove(groupe)
                return f"Le goupe avec l'ID {idgroupe} a été supprimé avec succès."
        return f"Le groupe avec l'ID {idgroupe} n'existe pas dans notre base de données."
    
    def modifier_groupe(self,idgroupe, nom, liste_groupes):
        for groupe in liste_groupes:
            if groupe.idgroupe == idgroupe:
                groupe.nom = nom
                return f"Le {nom} avec l'ID {idgroupe} a été modifié avec succès."
        return f"Le groupe avec l'ID {idgroupe} n'existe pas dans notre base de données."


    def afficher_listes_groupes(self, listes_groupes):
        if not listes_groupes:
            print("Aucun groupe dans la liste")
        else:
            print("Listes des groupes:")
            for groupe in listes_groupes:
                print(f"ID: {groupe.idgroupe}, nom : {groupe.nom}")
##############################################################################################################

    def creer_tp(self,idTp,libelle_tp,date_de_restitution,descriptionTp,liste_TP):
        tp= Tp(idTp,libelle_tp,datetime.now(),date_de_restitution,descriptionTp)
        liste_TP.append(tp)
        return f" Le TP sur le thème: {libelle_tp} avec l'ID {idTp} a été créé avec succès" 
    

    def afficher_liste_TP(self, liste_TP):
        if not liste_TP:
            print("Aucun TP dans la liste")
        else:
            print("Listes des TP:")
            for tp in liste_TP:
                print(f"ID: {tp.idTP}, nom : {tp.libelle_tp}, créé à la date du: {tp.date_de_creation}")