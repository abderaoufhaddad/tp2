# Importation des classes nécessaires
from time import sleep
from pyforum.bd import BD


def afficher_menu():
    """Affiche les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")


def main():

    # Initialisation de la base de données
    db = BD()

    while True:
        afficher_menu()

        # Demander à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1-6): ")

        if choix == '1':
            # Créer un utilisateur
            print("\nCréation d'un utilisateur...")

            # informations nécessaires pour créer un utilisateur
            username = input("Entrez le nom d'utilisateur: ")
            email = input("Entrez l'adresse courriel: ")
            password = input("Entrez le mot de passe: ")

            # Créer l'utilisateur 
            utilisateur = db.creer_utilisateur(username, email, password)
            print(f"Utilisateur {username} créé avec succès!")

        elif choix == '2':
            # Créer un forum
            print("\nCréation d'un forum...")

            # créer un forum
            nom_forum = input("Entrez le nom du forum: ")
            description_forum = input("Entrez la description du forum : ")
            if not description_forum:
                description_forum = None 

            # Appeler la méthode  
            forum = db.creer_forum(nom_forum, description_forum)

            # Message de confirmation
            print(f"Forum '{nom_forum}' créé avec succès!")

        elif choix == '3':
            # Créer une publication
            print("\nCréation d'une publication...")

            #informations nécessaires pour créer une publication
            titre_publication = input("Entrez le titre de la publication: ")
            contenu_publication = input("Entrez le contenu de la publication: ")

            # Demander l'identifiant de l'auteur et du forum
            auteur_id = input("Entrez l'identifiant de l'auteur (utilisateur): ")
            forum_id = input("Entrez l'identifiant du forum auquel la publication appartient: ")

            # Appeler la méthode pour créer la publication 
            publication = db.creer_publication(titre_publication, contenu_publication, auteur_id, forum_id)
            print(f"Publication '{titre_publication}' créée avec succès!")

        elif choix == '4':
            # Ajouter un commentaire
            print("\nAjouter un commentaire...")

            # Demander le contenu 
            contenu_commentaire = input("Entrez le contenu du commentaire: ")

            # Demander l'identifiant de l'auteur et de la publication
            auteur_id = input("Entrez l'identifiant de l'auteur (utilisateur): ")
            publication_id = input("Entrez l'identifiant de la publication à commenter: ")

            # Appeler la méthode pour créer le commentaire 
            commentaire = db.creer_commentaire(contenu_commentaire, auteur_id, publication_id)
            print(f"Commentaire ajouté avec succès à la publication {publication_id}!")

        elif choix == '5':
            # Joindre un forum
            print("\nJoindre un forum...")

            # Demander l'identifiant de l'utilisateur et du forum
            utilisateur_id = input("Entrez l'identifiant de l'utilisateur: ")
            forum_id = input("Entrez l'identifiant du forum à rejoindre: ")

            # Vérifier si l'utilisateur et le forum existent 
            utilisateur = db.obtenir_utilisateur_par_id(utilisateur_id)  # Récupérer l'utilisateur par ID
            forum = db.obtenir_forum_par_id(forum_id)  # Récupérer le forum par ID

            if utilisateur and forum:
                # Appeler la méthode
                db.ajouter_utilisateur_au_forum(utilisateur_id, forum_id)
                print(f"L'utilisateur {utilisateur.username} a rejoint le forum {forum_id}.")
            else:
                print("L'utilisateur ou le forum n'existe pas.")

        elif choix == '6':
            # Quitter le programme
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break

        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(1)  # Pause de 1 secondes pour rendre l'interface plus agréable
