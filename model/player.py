class Player:
    def __init__(self, lastname, firstname, birthday, sexe, rank):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.sexe = sexe
        self.rank = rank
    players = list()

    def create_player(self):
    global players
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))
    else:
        players.append({'name': name, 'price': price, 'quantity': quantity})


    def read_player(lastname):
        global players
        my_players = Query()
        if players.search(my_players.nom == lastname):
            return players.search(my_players.nom == lastname)
        else:
            raise PlayerNotRegistered


    def read_players_alphabetic():
        global players
        return [player for player in players]

    def update_player(lastname, firstname, birthday, sexe, rank):
        global players
        my_players = Query()
        if players.search(my_players.nom == lastname):
            players.update_multiple([({'prénom': firstname}, my_players.nom == lastname),
                                     ({'date de naissance': birthday}, my_players.nom == lastname),
                                     ({'sexe': sexe}, my_players.nom == lastname),
                                     ({'classement' : rank}, my_players.nom == lastname)])
        else:
            raise PlayerNotRegistered

    def delete_player(lastname):
        global players
        my_players = Query()
        if players.search(my_players.nom == lastname):
            players.remove(my_players.nom == lastname)
        else:
            raise PlayerNotRegistered


class PlayerAlreadyRegistered(Exception):
    pass

class PlayerNotRegistered(Exception):
    pass