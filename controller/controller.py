from view import View
from model import Player
from model import Tournament

class Controller(object):

    def start_players():
        Player.create_players()

    def start_menu():
        choice = 0
        View.menu()
        choice = input()
        choice = int(choice)
        Controller.choice_menu(choice)

    def choice_menu(choice):
        if choice == 1:
            name = input("nom du tournoi: ")
            localisation = input("lieu: ")
            date = input("date: ")
            nbturn = input("nombre de rounds: ")
            rounds = 0
            players = 0
            timecontrol = input("bullet, blitz ou coup rapide: ")
            description = input("description: ")
            Tournament.create_tournament(name, localisation, date,nbturn, rounds, players, timecontrol, description)

        elif choice == 2:
            print("Veuillez rentrer les données du nouveau joueur")
            name = str(input("Nom: "))
            birthday = str(input("Date de naissance: "))
            gender = str(input("Genre: "))
            rank = str(input('Rang: '))
            point = 0
            Controller.insert_player(name, birthday, gender, rank, point)
            print(name, birthday, gender, rank)
            rep = int(input("1-Oui     2-Non: "))
            while rep == 1:
                print("Veuillez rentrer les données du nouveau joueur")
                name = str(input("Nom: "))
                birthday = str(input("Date de naissance: "))
                gender = str(input("Genre: "))
                rank = str(input('Rang: '))
                point = 0
                Controller.insert_player(name, birthday, gender, rank, point)
                print(name, birthday, gender, rank)
                rep = int(input("1-Oui     2-Non: "))
            print('Ajout de joueur terminé')

        elif choice == 3:
            Controller.show_players_alpha()

        elif choice == 4:
            Controller.show_players_rank()

        elif choice == 5:
            Controller.show_tournament()

        elif choice == 6:
            Controller.first_round()

        elif choice == 7:
            choice = input("1-Sauvegarder 2-Charger")
            if choice == 1:
                pass
            if choice == 2:
                pass
            else :
                print("commande erreur")
                pass

        elif choice == 8:
            Controller.modify_player()
        elif choice == 0:
            quit()

        elif choice != 0:
            print("commande inconnus")

        Controller.start_menu()

    def show_players_alpha():
        players = Player.read_players_alphabetic()
        View.show_number_alpha(players)

    def show_players_rank():
        players = Player.read_player_rank()
        View.show_number_rank(players)
    def show_tournament():
        tournament = Tournament.read_tournament()
        View.show_tournament(tournament)


    def insert_player(name, birthday, gender, rank, point):
        Player.create_player(name, birthday, gender, rank, point)

    def first_round():
        players = Player.read_player_rank()
        View.show_round_one(players)

    def modify_player():
        players = Player.read_player()
        View.show_number_alpha(players)
        choice = input("quel joueur voulait vous modifier (rentrer chiffre): ")
        name = input("Nom: ")
        birthday = input("Date de naissance: ")
        gender = input("Genre: ")
        rank = input("Classement: ")
        point = input("Point: ")
        Player.modify_player(choice, name, birthday, gender, rank, point)

