class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_games_won = 0
        self.player2_games_won = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_games_won = self.player1_games_won + 1
        else:
            self.player2_games_won = self.player2_games_won + 1

    def score_for_players_tied_in_games(self):
        score = ""
        if self.player1_games_won == 0:
            score = "Love-All"
        elif self.player1_games_won == 1:
            score = "Fifteen-All"
        elif self.player1_games_won == 2:
            score = "Thirty-All"
        elif self.player1_games_won == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        return score
    def score_for_one_player_leading_by_four_or_more(self):
        score = ""
        minus_result = self.player1_games_won - self. player2_games_won
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    
    def score_for_players_close_but_not_tied_in_games(self):
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_games_won
            else:
                score = score + "-"
                temp_score = self.player2_games_won
            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score
    
    def get_score(self):

        if self.player1_games_won == self.player2_games_won:
            score = self.score_for_players_tied_in_games()
        elif self.player1_games_won >= 4 or self.player2_games_won >= 4:
            score = self.score_for_one_player_leading_by_four_or_more()
        else:
            score = self.score_for_players_close_but_not_tied_in_games()
        return score
