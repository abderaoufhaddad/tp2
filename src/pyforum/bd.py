from pyforum.utilisateur import Utilisateur

class BD:
    def __init__(self):
        self.utilisateurs: list[Utilisateur] = []
        self.forums = []
        self.publications = []
        self.commentaires = []
        self.utilisateurs_forums = {}
        print("Base de données initialisée.")

    def creer_utilisateur(self, username: str, email: str, mot_de_passe: str) -> Utilisateur:
        # Vérifier si l'utilisateur existe déjà
        if username in [u.username for u in self.utilisateurs]:
            print(f"[Simulé] L'utilisateur {username} existe déjà.")
            return

        # Créer un nouvel identifiant pour l'utilisateur
        new_id = max([u.id for u in self.utilisateurs], default=0) + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(new_id, username, email, mot_de_passe)
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde de l'utilisateur: {u}")

        # Retourner l'utilisateur créé
        return u

    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u

    def creer_forum(self, nom: str, description: str, utilisateur: Utilisateur):
        # Créer un nouvel identifiant pour le forum
        new_id = len(self.forums) + 1

        # Créer le forum
        forum = {
            "id": new_id,
            "nom": nom,
            "description": description,
            "utilisateur": utilisateur
        }

        # Ajouter le forum à la liste des forums
        self.forums.append(forum)

        # Ajouter le forum à la liste des forums de l'utilisateur
        utilisateur.forums.append(forum)

        print(f"[Simulé] Forum '{nom}' créé par {utilisateur.username}.")
        return forum

    def creer_publication(self, titre: str, contenu: str, utilisateur: Utilisateur, forum_id: int):
        # Créer un nouvel identifiant pour la publication
        new_id = len(self.publications) + 1

        # Créer la publication
        publication = {
            "id": new_id,
            "titre": titre,
            "contenu": contenu,
            "utilisateur": utilisateur,
            "forum_id": forum_id
        }

        # Ajouter la publication à la liste des publications
        self.publications.append(publication)

        print(f"[Simulé] Publication '{titre}' créée par {utilisateur.username} dans le forum {forum_id}.")
        return publication

    def creer_commentaire(self, contenu: str, utilisateur: Utilisateur, publication_id: int):
        # Créer un nouvel identifiant pour le commentaire
        new_id = len(self.commentaires) + 1

        # Créer le commentaire
        commentaire = {
            "id": new_id,
            "contenu": contenu,
            "utilisateur": utilisateur,
            "publication_id": publication_id
        }

        # Ajouter le commentaire à la liste des commentaires
        self.commentaires.append(commentaire)

        print(f"[Simulé] Commentaire créé par {utilisateur.username} sur la publication {publication_id}.")
        return commentaire

    def obtenir_forum_par_nom(self, nom_forum: str):
        for forum in self.forums:
            if forum["nom"] == nom_forum:
                return forum

    def obtenir_publication_par_titre(self, titre_publication: str):
        for publication in self.publications:
            if publication["titre"] == titre_publication:
                return publication

    def mettre_a_jour_forum(self, forum_id: int, nouveau_nom: str, nouvelle_description: str):
        # Chercher le forum à mettre à jour
        forum = next((f for f in self.forums if f["id"] == forum_id), None)

        if forum:
            forum["nom"] = nouveau_nom
            forum["description"] = nouvelle_description
            print(f"[Simulé] Forum {forum_id} mis à jour avec le nouveau nom: {nouveau_nom}.")
            return forum
        else:
            print(f"[Erreur] Forum {forum_id} non trouvé.")
            return None
