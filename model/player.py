class Player:

    def __init__(self, name, birthday, gender, rank, point):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.point = point

    def create_players():
        global players
        global serialized_players
        players = list()
        serialized_players = list()

    def create_player(name, birthday, gender, rank, point):
        global players
        global serialized_players
        player = Player(name=name, birthday=birthday, gender=gender, rank=rank, point=point)
        players.append(player)
        serialized_player = {'name': player.name, 'birthday': player.birthday, 'gender': player.gender,
                             'rank': player.rank, 'point' : player.point}
        serialized_players.append(serialized_player)

    def read_players_alphabetic():
        global players
        myplayers = (sorted(players, key=lambda player: player.name ))
        return [player for player in myplayers]

    def read_player_rank():
        global players
        myplayers = (sorted(players, key=lambda player: player.rank ))
        return [player for player in myplayers]

    def read_player():
        global players
        return [player for player in players]

    def save_player(name):
        pass
    def load_players(name):
        pass

    def modify_player(choice, name, birthday, gender, rank, point):
        global players
        copyplayer = players[int(choice)-1]
        copyname = copyplayer.name
        copybirthday = copyplayer.birthday
        copygender = copyplayer.gender
        copyrank = copyplayer.rank
        copypoint = copyplayer.point
        if not name:
            name = copyname
        elif not birthday:
            birthday = copybirthday
        elif not gender:
            gender = copygender
        elif not rank:
            rank = copyrank
        elif not point:
            point = copypoint
        players[int(choice)-1] = Player(name=name, birthday=birthday, gender=gender, rank=rank, point=point)


