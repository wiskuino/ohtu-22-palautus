class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score = ""
        self.temp_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        
        if self.player1_score == self.player2_score:
            self.score = self.deuce_case()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            self.score = self.winning_case()  
        
        else:
            self.score = self.playing_case()
        
        return self.score

    def playing_case(self):
        for i in range(1, 3):
            if i == 1:
                self.temp_score = self.player1_score
            else:
                self.score = self.score + "-"
                self.temp_score = self.player2_score
            if self.temp_score == 0:
                self.score = self.score + "Love"
            elif self.temp_score == 1:
                self.score = self.score + "Fifteen"
            elif self.temp_score == 2:
                self.score = self.score + "Thirty"
            elif self.temp_score == 3:
                self.score = self.score + "Forty"
        return self.score

    def winning_case(self):
        minus_result = self.player1_score - self. player2_score
        if minus_result == 1:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"
        return self.score

    def deuce_case(self):
        if self.player1_score > 3:
            return "Deuce"
        else:
            scores = {0:"Love-All",1:"Fifteen-All",2:"Thirty-All",3:"Forty-All"}
            return scores[self.player1_score]

