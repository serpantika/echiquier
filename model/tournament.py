from tinydb import TinyDB
import os
class Tournament:
    def __init__(self, name, localisation, date, nbturn, rounds, players, timecontrol, description):
        self.name = name
        self.localisation = localisation
        self.date = date
        self.nbturn = nbturn
        self.rounds = rounds
        self.players = players
        self.timecontrol = timecontrol
        self.description = description

    def create_tournament(name, localisation, date,nbturn, rounds, players, timecontrol, description):
        global tournament
        tournament = Tournament(name=name, localisation=localisation, date=date, nbturn=nbturn
                                , rounds=rounds, players=players, timecontrol=timecontrol, description=description)

    def read_tournament():
        global tournament

    def save_tournament(name):
        if not os.path.exists("save" + str(name)):
            os.makedirs("save" + str(name))

        pass

    def load_players(name):
        pass