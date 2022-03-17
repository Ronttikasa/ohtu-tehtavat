class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score_to_silly_name(self, score):
        score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_names[score]

    def score_difference(self):
        return abs(self.player1_score - self.player2_score)

    def four_points_reached(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            return True
        return False

    def leader(self):
        if self.player1_score > self.player2_score:
            return self.player1_name
        return self.player2_name

    def get_score(self):
        score_diff = self.score_difference()

        if score_diff == 0:
            if self.player1_score < 3:
                score = "{}-All".format(self.score_to_silly_name(self.player1_score))
            else:
                score = "Deuce"
        elif self.four_points_reached():
            leader = self.leader()
            if score_diff == 1:
                score = "Advantage {}".format(leader)
            elif score_diff >= 2:
                score = "Win for {}".format(leader)
        else:
            score = "{}-{}".format(self.score_to_silly_name(self.player1_score), self.score_to_silly_name(self.player2_score))

        return score
