class Utilisateur:
    def __init__(self, idUser, prenom, nom, email,mot_de_passe,role):
        self.idUser = idUser
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.role = role
        self.mot_de_passe= mot_de_passe

    def afficherUtilisateur(self):
        return f"id : {self.idUser}, nom : {self.nom}, prenom : {self.prenom}, email : {self.email}, role : {self.role.value}"
