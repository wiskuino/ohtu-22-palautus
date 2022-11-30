class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player_1 = player1_name
        self.player_2 = player2_name
        self.player1_score = 0
        self.player2_score = 0
        

    def won_point(self, player_name):
        if player_name == self.player_1:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        
        if self.player1_score == self.player2_score:
            return self.deuce_case()

        elif self.player1_score >= 4 and self.player1_score > self.player2_score:
            return self.winning_player_1()  # player_1 johtaa
        
        elif self.player2_score >= 4 and self.player2_score > self.player1_score:
            return self.winning_player_2()   # player_2 johtaa
        
        else:
            return self.playing_case()
    

    def playing_case(self):
        scores = {0:"Love",1:"Fifteen",2:"Thirty",3:"Forty"}  # sanakirjaa tarvitaan vain metodissa
        return f"{scores[self.player1_score]}-{scores[self.player2_score]}"

    def winning_player_1(self):
        scores = {1:"Advantage "+self.player_1,2:"Win for "+self.player_1,3:"Win for "+self.player_1, 4:"Win for "+self.player_1} # sanakirjaa tarvitaan vain metodissa
        return scores[self.player1_score - self. player2_score]  
        

    def winning_player_2(self):
        scores = {1:"Advantage "+self.player_2,2:"Win for "+self.player_2,3:"Win for "+self.player_2,4:"Win for "+self.player_2} # sanakirjaa tarvitaan vain metodissa
        return scores[self.player2_score - self. player1_score]
        
    def deuce_case(self):
        if self.player1_score > 3:
            return "Deuce"
        else:
            scores = {0:"Love-All",1:"Fifteen-All",2:"Thirty-All",3:"Forty-All"} # sanakirjaa tarvitaan vain metodissa
            return scores[self.player1_score]

