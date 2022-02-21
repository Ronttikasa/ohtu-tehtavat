import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['games'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties']
        )

        players.append(player)

    print(f'Players from FIN {datetime.now()}')

    finnish_players = [player for player in players if player.nationality == 'FIN']

    for player in sorted(finnish_players, key=lambda player: player.assists + player.goals, reverse=True):
        print(player)


if __name__ == "__main__":
    main()


