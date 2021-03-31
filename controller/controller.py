from view import View
from view import Menu
from model import Player
from model import PlayerNotRegistered
from model import PlayerAlreadyRegistered

class Controller(object):
    def start_menu():
        Menu.start

    def show_players():
        players = Player.read_players_alphabetic()
        View.show_number_point_list(players)

    def show_player(lastname):
        try:
            player = ModelBasic.read_player(lastname)
            View.show_player(player)
        except PlayerNotRegistered as e:
            View.display_missing_player_error(lastname,e)

    def insert_player(lastname, firstname, birthday, sexe, rank):
        ModelBasic.create_player(lastname, firstname, birthday, sexe, rank)
    def update_player(lastname,firstname,birthday,sexe,rank):
        try:
            ModelBasic.update_player(lastname,firstname,birthday,sexe,rank)
            View.display_player_updated(lastname)
        except PlayerNotRegistered as e:
            View.display_player_not_yet_stored_error(lastname,e)
    def delete_player(lastname):
        try:
            ModelBasic.delete_player(lastname)
            View.display_player_deletion(lastname)
        except PlayerNotRegistered as e:
            View.display_player_not_yet_stored_error(lastname,e)