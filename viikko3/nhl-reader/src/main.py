import requests
from player import Player
from datetime import datetime


class PlayerStats:
    def __init__(self, response):
        self.response=response
        self.players = []

    def top_scorers_by_nationality(self, nation: str):
        for player_dict in self.response:
            player = Player(
                player_dict['name'],player_dict['team'],player_dict['goals'],player_dict['assists']
            )
            if player_dict['nationality'] == nation:
                self.players.append(player)

        self.players.sort(key=lambda x: (x.goals+x.assists),reverse=True)
        return filter(lambda player : (player.goals+player.assists) > 50,self.players)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)
    stats = PlayerStats(response)
    players = stats.top_scorers_by_nationality("FIN")
    
    #players = []

    #for player_dict in response:
    #    player = Player(
    #        player_dict['name'],player_dict['team'],player_dict['goals'],player_dict['assists']
    #    )
    #    if player_dict['nationality'] == "FIN":
    #        players.append(player)
#
#
    #players.sort(key=lambda x: (x.goals+x.assists),reverse=True)

    #print(f"Players from FIN {datetime.now()}")
    #print()

    #parhaat = filter(lambda player : (player.goals+player.assists) > 50,players)
    

    for player in players:
        print(player)

if __name__=="__main__":
    main()



 
 
 

 

 
 
 
 

 

 

 
 