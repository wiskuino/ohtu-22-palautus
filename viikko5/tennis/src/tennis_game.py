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

        elif self.player1_score >= 4 and self.player1_score > self.player2_score:
            self.score = self.winning_player_1()  # player1 johtaa
        
        elif self.player2_score >= 4 and self.player2_score > self.player1_score:
            self.score = self.winning_player_2()   # player2 johtaa
        
        else:
            self.score = self.playing_case()
        
        return self.score

    def playing_case(self):
        scores = {0:"Love",1:"Fifteen",2:"Thirty",3:"Forty"}
        return f"{scores[self.player1_score]}-{scores[self.player2_score]}"
        
        
        
        #for i in range(1, 3):
            #if i == 1:
            #    self.temp_score = self.player1_score
            #else:
            #    self.score = self.score + "-"
            #    self.temp_score = self.player2_score
            #if self.temp_score == 0:
            #    self.score = self.score + "Love"
            #elif self.temp_score == 1:
            #    self.score = self.score + "Fifteen"
            #elif self.temp_score == 2:
            #    self.score = self.score + "Thirty"
            #elif self.temp_score == 3:
            #    self.score = self.score + "Forty"
        #return self.score

    def winning_player_1(self):
        scores = {1:"Advantage player1",2:"Win for player1",3:"Win for player1", 4:"Win for player1"}
        return scores[self.player1_score - self. player2_score]  
        

    def winning_player_2(self):
        scores = {1:"Advantage player2",2:"Win for player2",3:"Win for player2",4:"Win for player2"}
        return scores[self.player2_score - self. player1_score]
        
    def deuce_case(self):
        if self.player1_score > 3:
            return "Deuce"
        else:
            scores = {0:"Love-All",1:"Fifteen-All",2:"Thirty-All",3:"Forty-All"}
            return scores[self.player1_score]

