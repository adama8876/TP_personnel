# Importation des modules nécessaires
from role import Role
import getpass
from enseignant import Enseignant
from apprenant import Apprenant
from admin import Admin
from groupe import Groupe

# Initialisation des listes d'apprenants, d'enseignants et d'administrateurs
liste_apprenants = [
    Apprenant(1, "Adama", "Konate", "adama@gmail.com","123456", 1),
    Apprenant(2, "Sikou", "Diouarra", "sikou@gmail.com","654378",1 )
]

liste_enseignants = [
    Enseignant(1, "Fatoumata", "Kaloga", "fatoumata@example.com", 1234567, "Enseignant"),
    Enseignant(2, "Kaou", "Diallo", "diallo@example.com", 34527371, "Enseignant")
]

liste_admins = [
    Admin(1,"Adama","Konate","adama@gmail.com", "adama"),
    Admin(3, "issa","coulibaly","issa@gmail.com","1111")
]
liste_groupes =[
    Groupe(1, "Groupe 1"),
    Groupe(2, "Groupe 2")
]


def verifier_presence_admin():
    print("\n ***Connexion*** \n")
    prenom_admin = input("veillez saisir votre nom: ")
    # mdp_admin = input("veillez saisir votre mot de passe: ")
    admin_operant = next((a for a in liste_admins if a.prenom == prenom_admin ), None)
    if admin_operant:
        print("\n ***Bienvenu(e) Administrateur ", admin_operant.prenom, "!*** \n")
        main(admin_operant)
    else:
        print("Le nom ou le mot de passe incorrect, veuillez vous rassurer que vous avez bien saisi les caracteres.")
        print("\n***Options***\n:")
        print("1. Réessayer")
        print("Autre. Quitter")
        choix = input("Entrez votre choix: ")
        if choix == '1':
            verifier_presence_admin()




def verifier_presence_enseignant():
    print("\n ***Connexion*** \n")
    prenom_enseignant = input("veillez saisir votre prenom: ")
    # mdp_admin = input("veillez saisir votre mot de passe: ")
    enseignant_operant = next((a for a in liste_enseignants if a.prenom == prenom_enseignant ), None)
    if enseignant_operant:
        print("\n ***Bienvenu(e) Enseignant(e) ", enseignant_operant.prenom, "!*** \n")
        main(enseignant_operant)
    else:
        print("Le prenom ou le mot de passe incorrect, veuillez vous rassurer que vous avez bien saisi les caracteres.")
        print("\n***Options***\n:")
        print("1. Réessayer")
        print("Autre. Quitter")
        choix = input("Entrez votre choix: ")
        if choix == '1':
            verifier_presence_enseignant()

# Fonction principale (tableau de bord de l'admin)
def main(admin: Admin):
    global liste_enseignants, liste_admins, liste_apprenants
    
    # admin1 = Admin(1, "Mamadou", "Diarra", "diarra@gmail.com","123654")
    
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
            role = "Enseignant"
            idUser = len(liste_enseignants) + 1
            print(admin.Ajouter_enseignant(idUser, nom, prenom, email, mot_de_passe, role, liste_enseignants))
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
                    idUser = int(input("Entrez l'ID de l'enseignant à modifier : "))
                    enseignant = next((ens for ens in liste_enseignants if ens.idUser == idUser), None)
                    if enseignant:
                        nom = input("Entrez le nouveau nom de l'enseignant : ")
                        prenom = input("Entrez le nouveau prénom de l'enseignant : ")
                        email = input("Entrez le nouvel email de l'enseignant : ")
                        mot_de_passe = input("Entrez le nouveau mot de passe de l'enseignant : ")
                        print(admin.modifier_enseignant_par_id(idUser, nom, prenom, email, mot_de_passe, liste_enseignants))
                        break  # Sort de la boucle si la modification est effectuée avec succès
                    else:
                        print(f"L'enseignant avec l'ID {idUser} n'existe pas dans notre base de données. Veuillez saisir un autre ID valide.")
                elif sub_choix == '2':
                    while True:
                        idUser = int(input("Entrez l'ID de l'enseignant à supprimer : "))
                        enseignant = next((ens for ens in liste_enseignants if ens.idUser == idUser), None)
                        if enseignant:
                            print(admin.supprimer_enseignant_par_id(idUser, liste_enseignants))
                            break  # Sort de la boucle après la suppression
                        else:
                            print(f"L'enseignant avec l'ID {idUser} n'existe pas dans notre base de données. Veuillez saisir un autre ID valide.")
                    break  # Sort de la boucle après la modification/suppression
                else:
                    print("Option invalide, veuillez réessayer.")
        elif choix == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")
            #####################################################################################################################

            # Fonction principale (tableau de bord de l'admin)
def main(enseignant: Enseignant):
    global liste_enseignants, liste_admins, liste_apprenants
    
    # admin1 = Admin(1, "Mamadou", "Diarra", "diarra@gmail.com","123654")
    
    while True:
        print("*** Bienvenue dans le tableau de bord de l'enseignant ***")
        print("1. Ajouter un apprenant")
        print("2. Voir liste des apprenants")
        print("3. Modifier ou supprimer un apprenant")
        print("4. Créer un groupe")
        print("5. Afficher listes groupes")

        choix = input("Choisissez une option : ")

        if choix == '1':
            nom = input("Entrez le nom de l'apprenant : ")
            prenom = input("Entrez le prénom de l'apprenant : ")
            email = input("Entrez l'email de l'apprenant : ")
            mot_de_passe = input("Entrez le mot de passe de l'apprenant : ")
            # role= "Apprenant" 
            idUser = len(liste_apprenants) + 1
            print(enseignant.Ajouter_apprenant(idUser, nom, prenom, email, mot_de_passe, liste_apprenants))

        elif choix == '2':
            print("Liste des apprenants supervisés par l'enseignant:")
            for apprenant in liste_apprenants:
                print(f"ID : {apprenant.idUser}, Nom : {apprenant.nom}, Prénom : {apprenant.prenom}, Email : {apprenant.email}, Rôle :{apprenant.role}, Ens_id : {apprenant.id_ens}")
                ################################################################################
        elif choix == '3':
            while True:
                print("1. Modifier un apprennat")
                print("2. Supprimer un apprenant")
                sub_choix = input("Choisissez une option : ")
                if sub_choix == '1':
                    idUser = int(input("Entrez l'ID de l'apprenant à modifier : "))
                    apprenant = next((ens for ens in liste_apprenants if ens.idUser == idUser), None)
                    if apprenant:
                        nom = input("Entrez le nouveau nom de l'enseignant : ")
                        prenom = input("Entrez le nouveau prénom de l'enseignant : ")
                        email = input("Entrez le nouvel email de l'enseignant : ")
                        mot_de_passe = input("Entrez le nouveau mot de passe de l'enseignant : ")
                        print(enseignant.modifier_apprenant(idUser, nom, prenom, email, mot_de_passe, liste_apprenants))
                        break  # Sort de la boucle si la modification est effectuée avec succès
                    else:
                        print(f"L'enseignant avec l'ID {idUser} n'existe pas dans notre base de données. Veuillez saisir un autre ID valide.")
                elif sub_choix == '2':
                    while True:
                        idUser = int(input("Entrez l'ID de l'enseignant à supprimer : "))
                        apprenant = next((ens for ens in liste_apprenants if ens.idUser == idUser), None)
                        if apprenant:
                            print(enseignant.supprimer_apprenant(idUser, liste_apprenants))
                            break  # Sort de la boucle après la suppression
                        else:
                            print(f"L'apprenant avec l'ID {idUser} n'existe pas dans notre base de données. Veuillez saisir un autre ID valide.")
                    break  # Sort de la boucle après la modification/suppression
                else:
                    print("Option invalide, veuillez réessayer.")
        elif choix == '4':
                        idgroupe = len(liste_groupes) + 1
                        nom = input("Entrez le nom du groupe : ")                        
                        print(enseignant.creer_groupe(idgroupe, nom, liste_groupes))
        elif choix == '5':
            print("Liste des groupes créés:")
            for groupe in liste_groupes:
                print(f"ID : {groupe.idgroupe}, Nom : {groupe.nom}")

# Exécute la fonction main si ce fichier est exécuté directement
if __name__ == "__main__":
    print('***Bienvenue dans notre système de gestion de groupe***')
    role = input("Veuillez indiquer votre rôle (admin/enseignant/apprenant): ").lower()
    if role == 'admin':
        # main()
        verifier_presence_admin()
    elif role == 'enseignant':
        verifier_presence_enseignant()
else:
    print("Rôle invalide")