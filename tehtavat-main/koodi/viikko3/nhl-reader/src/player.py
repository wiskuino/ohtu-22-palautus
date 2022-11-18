class Player:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name']
        )

        players.append(player)

    print("Oliot:")

    for player in players:
        print(player)