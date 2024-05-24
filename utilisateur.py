class Utilisateur:
    def __init__(self, idUser, prenom, nom, email, role):
        self.idUser = idUser
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.role = role

    def afficherUtilisateur(self):
        return f"id : {self.idUser}, nom : {self.nom}, prenom : {self.prenom}, email : {self.email}, role : {self.role.value}"
