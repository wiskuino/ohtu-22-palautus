import requests
from player import Player
from datetime import datetime

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],player_dict['team'],player_dict['goals'],player_dict['assists']
        )
        if player_dict['nationality'] == "FIN":
            players.append(player)
    
    print(f"Players from FIN {datetime.now()}")
    print()


    parhaat = filter(lambda player : (player.goals+player.assists) > 20,players)
    

    for player in parhaat:
        print(player)

if __name__=="__main__":
    main()

 

 
 

 

 
 
 
 

 

 

 
 