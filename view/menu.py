class Menu():
    def __init__(self):
        self.start()

    def start(self):
        print('Bienvenue !!!')
        nn = 2
        while nn != 0:
            print('Que voulez vous faire ?\n1: Créer un nouveau tournoi \n2: Ajouter des joueurs'
                  '\n3: Afficher les joueurs du tournoi \n4: Afficher un joueur du tournoi '
                  '\n5: Supprimer un joueur du tournoi \n6: Modifier un joueur du tournoi \n0: Quitter le programme ')
            nn = input()
            nn = int(nn)
            if nn == 1:
                tournoi = input("Nom du tournoi: ")
                ModelBasic.create_players(tournoi)
                print('Tournoi créé')
            elif nn == 2:
                print("Veuillez rentrer les données du nouveau joueur")
                lastname = str(input("Nom: "))
                firstname = str(input("Prénom: "))
                birthday = str(input("Date de naissance: "))
                sexe = str(input("Sexe: "))
                rank = str(input('Rang: '))
                Controller.insert_player(lastname, firstname, birthday, sexe, rank)
                print(lastname, firstname, birthday, sexe, rank)
                print("Ajouter un autre joueur ?")
                rep = int(input("1-Oui     2-Non: "))
                while rep == 1:
                    print("Veuillez rentrer les données du nouveau joueur")
                    lastname = (input("Nom: "))
                    firstname = (input("Prénom: "))
                    birthday = (input("Date de naissance: "))
                    sexe = (input("Sexe: "))
                    rank = (input('Rang: '))
                    Controller.insert_player(lastname, firstname, birthday, sexe, rank)
                    print(lastname, firstname, birthday, sexe, rank)
                    print("Ajouter un autre joueur ?")
                    rep = int(input("1 - oui     2 - non: "))
                print('Ajout de joueur terminé')
            elif nn == 3:
                Controller.show_players()
            elif nn == 4:
                lastname = input('Nom du joueur recherché: ')
                Controller.show_player(lastname)
            elif nn == 5:
                lastname = input('Nom du joueur à supprimer: ')
                Controller.delete_player(lastname)
            elif nn == 6:
                print("Veuillez rentrer les données du joueur à modifier")
                lastname = (input("Nom: "))
                firstname = (input("Prénom: "))
                birthday = (input("Date de naissance: "))
                sexe = (input("Sexe: "))
                rank = (input('Rang: '))
                Controller.update_player(lastname, firstname, birthday, sexe, rank)
            elif nn != 0:
                print("Choix inconnus")