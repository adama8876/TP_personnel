# Importation des modules nécessaires
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
    Enseignant(1, "Fatoumata", "Kaloga", "fatoumata@example.com", 1234567, Role.ENSEIGNANT),
    Enseignant(2, "Kaou", "Diallo", "diallo@example.com", 34527371, Role.ENSEIGNANT)
]

liste_admins = []

# Fonction pour ajouter un enseignant
def ajouter_enseignant(idEnseignant, nom, prenom, email, mot_de_passe, role, liste_enseignants):
    enseignant = Enseignant(idEnseignant, nom, prenom, email, mot_de_passe, role)
    liste_enseignants.append(enseignant)
    return f"L'enseignant avec l'ID {idEnseignant} a été ajouté avec succès."

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

# Fonction pour supprimer un enseignant par son ID
def supprimer_enseignant_par_id(idEnseignant, liste_enseignants):
    for enseignant in liste_enseignants:
        if enseignant.idEnseignant == idEnseignant:
            liste_enseignants.remove(enseignant)
            return f"L'enseignant avec l'ID {idEnseignant} a été supprimé avec succès."
    return f"L'enseignant avec l'ID {idEnseignant} n'existe pas dans notre base de données."

# Fonction principale (tableau de bord de l'admin)
def main():
    global liste_enseignants, liste_admins, liste_apprenants
    
    admin1 = Admin(1, "Mamadou", "Diarra", "diarra@gmail.com")
    
    while True:
        print("*** Bienvenue dans le tableau de bord de l'administrateur ***")
        print("1. Ajouter un enseignant")
        print("2. Afficher la liste des enseignants")
        print("3. Modifier ou supprimer un enseignant")
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
            print("*** Liste des enseignants ***")
            for enseignant in liste_enseignants:
                print(enseignant)
        elif choix == '3':
            while True:
                print("1. Modifier un enseignant")
                print("2. Supprimer un enseignant")
                sub_choix = input("Choisissez une option : ")
                if sub_choix == '1':
                    idEnseignant = int(input("Entrez l'ID de l'enseignant à modifier : "))
                    enseignant = next((ens for ens in liste_enseignants if ens.idEnseignant == idEnseignant), None)
                    if enseignant:
                        nom = input("Entrez le nouveau nom de l'enseignant : ")
                        prenom = input("Entrez le nouveau prénom de l'enseignant : ")
                        email = input("Entrez le nouvel email de l'enseignant : ")
                        mot_de_passe = input("Entrez le nouveau mot de passe de l'enseignant : ")
                        print(modifier_enseignant_par_id(idEnseignant, nom, prenom, email, mot_de_passe, liste_enseignants))
                        break  # Sort de la boucle si la modification est effectuée avec succès
                    else:
                        print(f"L'enseignant avec l'ID {idEnseignant} n'existe pas dans notre base de données. Veuillez saisir un autre ID valide.")
                elif sub_choix == '2':
                    while True:
                        idEnseignant = int(input("Entrez l'ID de l'enseignant à supprimer : "))
                        enseignant = next((ens for ens in liste_enseignants if ens.idEnseignant == idEnseignant), None)
                        if enseignant:
                            print(supprimer_enseignant_par_id(idEnseignant, liste_enseignants))
                            break  # Sort de la boucle après la suppression
                        else:
                            print(f"L'enseignant avec l'ID {idEnseignant} n'existe pas dans notre base de données. Veuillez saisir un autre ID valide.")
                    break  # Sort de la boucle après la modification/suppression
                else:
                    print("Option invalide, veuillez réessayer.")
        elif choix == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Exécute la fonction main si ce fichier est exécuté directement
if __name__ == "__main__":
    main()
