# # Importation de l'énumération Role et de la classe Utilisateur
# # from role import Role
# # from utilisateur import Utilisateur
# # from apprenant import Apprenant
# # from enseignant import Enseignant
# # from groupe import Groupe
# # from admin import Admin
# from utilisateur import Utilisateur
# from role import Role
# from enseignant import Enseignant
# from apprenant import Apprenant
# from admin import Admin
# # # Création d'une instance de Utilisateur avec le rôle apprenant
# # # apprenant1 = Utilisateur(1, "Adama", "Konate", "adama@gmail.com", Role.APPRENANT)

# # # Affichage des informations de l'apprenant
# # # print(apprenant1.afficherUtilisateur())

# # # Création d'une instance de Enseignant
# # enseignant1 = Enseignant(1, "Fatoumataa", "Kaloga", "kalogae@gmail.com",)

# # # Création d'apprenants par l'enseignant
# # apprenant1 = enseignant1.creer_apprenant(2, "Adama", "Konate", "adama@gmail.com")
# # apprenant2 = enseignant1.creer_apprenant(3, "Fatou", "Diop", "fatou@gmail.com")

# # # Affichage des informations de l'enseignant
# # print(enseignant1.afficherUtilisateur())

# # # Affichage des informations des apprenants créés par l'enseignant
# # for apprenant in enseignant1.liste_apprenants:
# #     print(apprenant.afficherApprenant())



# liste_apprenants = [
#     Apprenant(1, "Adama", "Konate","adama@gmail.com", 1),
#     Apprenant(1, "Sikou", "Diouarra","adama@gmail.com", 1)

#         ]

# liste_admins =[

# ]

# liste_enseignants = [

# ]
#     # Création d'un enseignant
# # enseignant = Enseignant(1, "Fatoumata", "Kaloga", "fatoumata@example.com")
# # enseignant2 = Enseignant(2, "Kaou", "Diallo", "Diallo@example.com" )

# # Création d'un apprenant
# # apprenant1 = enseignant.creer_apprenant(1, "Kontere", "Tienou", "kontere@example.com", liste_apprenants)
# # apprenant2 = enseignant.creer_apprenant(3, "Moussa", "Coulibaly", "Moussa@example.com", liste_apprenants)
# def Ajouter_enseignant(self, idEnseignant, nom, prenom, email, mot_de_passe, role, liste_enseignants):
#     enseignant = Enseignant(idEnseignant, nom, prenom, email, mot_de_passe, role)  # Correction de l'ordre des arguments
#     liste_enseignants.append(enseignant)
#     for enseignant in liste_enseignants:
#         print(enseignant)
#     return f"Utilisateur avec idUser {idEnseignant} a été ajouté avec succès."
# # # apprenant3 = enseignant.creer_apprenant(1, "Kalifa", "Babi", "Khalifa@example.com", liste_apprenants)



# # apprenant4 = enseignant2.creer_apprenant(2, "Kalifa", "Babi", "Khalifa@example.com", liste_apprenants)

# admin1= Admin(55, "Mamadou", "Diarra","diarra@gmail.com",)
# # Modification de l'apprenant
# # enseignant.modifier_apprenant(3, "New Alice", "New Smith", "newalice@example.com", liste_apprenants)

# # Suppression de l'apprenant
# # enseignant.supprimer_apprenant(1)
# # enseignant.afficher_liste_apprenants(liste_apprenants)
# # print(admin1)




# # Fonction principale (tableau de bord de l'admin)
# def main():
#  # Affichez le tableau de bord de l'administrateur
#     while True:
#         print("*** Bienvenue dans le tableau de bord de l'administrateur ***")
#         print("1. Ajouter un enseignant")
#         print("2. Ajouter un administrateur")
#         print("3. Quitter")

#         choix = input("Choisissez une option : ")

#         if choix == '1':
#             nom = input("Entrez le nom de l'enseignant : ")
#             prenom = input("Entrez le prénom de l'enseignant : ")
#             email = input("Entrez l'email de l'enseignant : ")
#             mot_de_passe = input("Entrez le mot de passe de l'enseignant : ")
#             role = Role.ENSEIGNANT
#             idEnseignant = len(liste_enseignants) + 1
#             print(admin1.Ajouter_enseignant(idEnseignant, nom, prenom, email, mot_de_passe, role, liste_enseignants))
#         elif choix == '2':
#             nom = input("Entrez le nom de l'administrateur : ")
#             prenom = input("Entrez le prénom de l'administrateur : ")
#             email = input("Entrez l'email de l'administrateur : ")
#             mot_de_passe = input("Entrez le mot de passe de l'administrateur : ")
#             role = Role.ADMIN
#             idAdmin = len(liste_admins) + 1
#             print(admin1.Ajouter_admin(idAdmin, nom, prenom, email, mot_de_passe, role, liste_admins))
#         elif choix == '3':
#             print("Au revoir!")
#             break
#         elif choix == '3':
#             self.afficher_liste_enseignants(liste_enseignants)
#         else:
#             print("Option invalide, veuillez réessayer.")

# # Exécute la fonction main si ce fichier est exécuté directement
# if __name__ == "__main__":
#     main()









from role import Role
from enseignant import Enseignant
from apprenant import Apprenant
from admin import Admin

# Initialisation des listes d'apprenants, d'enseignants et d'administrateurs
liste_apprenants = [
    Apprenant(1, "Adama", "Konate", "adama@gmail.com", 1),
    Apprenant(2, "Sikou", "Diouarra", "sikou@gmail.com", 1)
]

liste_enseignants = [
    Enseignant(1, "Fatoumata", "Kaloga", "fatoumata@example.com",1234567),
    Enseignant(2, "Kaou", "Diallo", "diallo@example.com",34527371)
]

liste_admins = []

# Fonction pour ajouter un enseignant
def ajouter_enseignant(idEnseignant, nom, prenom, email, mot_de_passe, role, liste_enseignants):
    enseignant = Enseignant(idEnseignant, nom, prenom, email, mot_de_passe, role)
    liste_enseignants.append(enseignant)
    return f"L'enseignant avec l'ID {idEnseignant} a été ajouté avec succès."

# Fonction principale (tableau de bord de l'admin)
def main():
    global liste_enseignants, liste_admins
    
    admin1 = Admin(1, "Mamadou", "Diarra", "diarra@gmail.com")
    
    while True:
        print("*** Bienvenue dans le tableau de bord de l'administrateur ***")
        print("1. Ajouter un enseignant")
        print("2. Ajouter un administrateur")
        print("3. Afficher la liste des enseignants")
        print("4. Quitter")

        choix = input("Choisissez une option : ")

        if choix == '1':
            nom = input("Entrez le nom de l'enseignant : ")
            prenom = input("Entrez le prénom de l'enseignant : ")
            email = input("Entrez l'email de l'enseignant : ")
            mot_de_passe = input("Entrez le mot de passe de l'enseignant : ")
            role = Role.ENSEIGNANT
            idEnseignant = len(liste_enseignants) + 1
            print(ajouter_enseignant(idEnseignant, nom, prenom, email, mot_de_passe, role, liste_enseignants))
        elif choix == '2':
            nom = input("Entrez le nom de l'administrateur : ")
            prenom = input("Entrez le prénom de l'administrateur : ")
            email = input("Entrez l'email de l'administrateur : ")
            mot_de_passe = input("Entrez le mot de passe de l'administrateur : ")
            role = Role.ADMIN
            idAdmin = len(liste_admins) + 1
            # Ajouter la logique pour ajouter un administrateur
        elif choix == '3':
            print("*** Liste des enseignants ***")
            for enseignant in liste_enseignants:
                print(enseignant)
        elif choix == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Exécute la fonction main si ce fichier est exécuté directement
if __name__ == "__main__":
    main()
