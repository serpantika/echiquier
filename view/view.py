class View(object):

    @staticmethod
    def show_number_alpha(players):
        print('--- {} LISTE ---')
        for i, player in enumerate(players):
            print('{}. {}, {}, {}, {}, {}' .format(i+1, player.name,
                                               player.birthday, player.gender, player.rank, player.point))

    @staticmethod
    def show_number_rank(players):
        print('--- {} LISTE ---')
        for i, player in enumerate(players):
            print('{}. {}, {}, {}, {}, {}' .format(i+1, player.rank, player.name,
                                                   player.birthday, player.gender, player.point))

    @staticmethod
    def show_tournament(tournament):
        print('--- {} LISTE ---')


    @staticmethod
    def show_round_one(players):
        print('--- Tour 1 ---')
        print(len(players))
        print(players[0] + 'Contre' + players[4] +'/n' +
              players[1] + 'Contre' + players[5] +'/n' +
              players[2] + 'Contre' + players[6] +'/n' +
              players[3] + 'Contre' + players[7] +'/n' )


    @staticmethod
    def display_player_updated(player, o_firstname, o_birthday, o_sexe, o_rank,
                               n_firstname, n_birthday, n_sexe, n_rank):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} firstname: {} --> {}'
              .format(player, o_firstname, n_firstname))
        print('Change {} birthday: {} --> {}'
              .format(player, o_birthday, n_birthday))
        print('Change {} sexe: {} --> {}'
              .format(player, o_sexe, n_sexe))
        print('Change {} rank: {} --> {}'
              .format(player, o_rank, n_rank))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')


    @staticmethod
    def menu():
        print('Que voulez vous faire ?\n1: Créer un nouveau tournoi \n2: Ajouter des joueurs'
              '\n3: Afficher les joueurs du tournoi classé par nom \n4: Afficher les joueurs du tournoi classé par rang'
              '\n5: Afficher information tournoi \n6: Lancer tour 1'
              '\n0: Quitter le programme')