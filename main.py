# Importation de l'énumération Role et de la classe Utilisateur
from role import Role
from utilisateur import Utilisateur
from apprenant import Apprenant
from enseignant import Enseignant
from groupe import Groupe
from admin import Admin

# # Création d'une instance de Utilisateur avec le rôle apprenant
# # apprenant1 = Utilisateur(1, "Adama", "Konate", "adama@gmail.com", Role.APPRENANT)

# # Affichage des informations de l'apprenant
# # print(apprenant1.afficherUtilisateur())

# # Création d'une instance de Enseignant
# enseignant1 = Enseignant(1, "Fatoumataa", "Kaloga", "kalogae@gmail.com",)

# # Création d'apprenants par l'enseignant
# apprenant1 = enseignant1.creer_apprenant(2, "Adama", "Konate", "adama@gmail.com")
# apprenant2 = enseignant1.creer_apprenant(3, "Fatou", "Diop", "fatou@gmail.com")

# # Affichage des informations de l'enseignant
# print(enseignant1.afficherUtilisateur())

# # Affichage des informations des apprenants créés par l'enseignant
# for apprenant in enseignant1.liste_apprenants:
#     print(apprenant.afficherApprenant())




liste_apprenants = [
    Apprenant(1, "Adama", "Konate","adama@gmail.com", 1)
    
    
]

liste_Enseignats = [

]
    # Création d'un enseignant
enseignant = Enseignant(1, "Fatoumata", "Kaloga", "fatoumata@example.com")
enseignant2 = Enseignant(2, "Kaou", "Diallo", "Diallo@example.com" )

# Création d'un apprenant
# apprenant1 = enseignant.creer_apprenant(1, "Kontere", "Tienou", "kontere@example.com", liste_apprenants)
# apprenant2 = enseignant.creer_apprenant(3, "Moussa", "Coulibaly", "Moussa@example.com", liste_apprenants)
# # apprenant3 = enseignant.creer_apprenant(1, "Kalifa", "Babi", "Khalifa@example.com", liste_apprenants)
# apprenant4 = enseignant2.creer_apprenant(2, "Kalifa", "Babi", "Khalifa@example.com", liste_apprenants)

admin1= Admin(55, "Mamadou", "Diarra","diarra@gmail.com",)
# Modification de l'apprenant
# enseignant.modifier_apprenant(3, "New Alice", "New Smith", "newalice@example.com", liste_apprenants)

# Suppression de l'apprenant
# enseignant.supprimer_apprenant(1)
enseignant.afficher_liste_apprenants(liste_apprenants)
# print(admin1)





