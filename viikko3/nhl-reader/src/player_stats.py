from datetime import datetime

class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()

        print(f'Players from {nationality} {datetime.now()}')

        players_by_nationality = [player for player in players if player.nationality == nationality]

        return sorted(players_by_nationality, key=lambda player: player.assists + player.goals, reverse=True)
            

