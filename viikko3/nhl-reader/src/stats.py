#from reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.lukija = reader
        #self.response=response
        self.players = []
        self.players2 = []
        

    def top_scorers_by_nationality(self, nation: str):
        
        self.players2=self.lukija.get_players()
        for player_dict in self.players2:
            player = Player(
                player_dict['name'],player_dict['team'],player_dict['goals'],player_dict['assists']
            )
            if player_dict['nationality'] == nation:
                self.players.append(player)

        self.players.sort(key=lambda x: (x.goals+x.assists),reverse=True)
        return filter(lambda player : (player.goals+player.assists) >= 0,self.players)










