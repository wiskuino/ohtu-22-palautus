class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player_1 = player1_name
        self.player_2 = player2_name
        self.player_1_score = 0
        self.player_2_score = 0
        

    def won_point(self, player_name):
        if player_name == self.player_1:
            self.player_1_score = self.player_1_score + 1
        else:
            self.player_2_score = self.player_2_score + 1

    def get_score(self):
        
        if self.player_1_score == self.player_2_score:
            return self.deuce_case()

        elif self.player_1_score >= 4 and self.player_1_score > self.player_2_score:
            return self.player_1_advantage()  # player_1 johtaa
        
        elif self.player_2_score >= 4 and self.player_2_score > self.player_1_score:
            return self.player_2_advantage()   # player_2 johtaa
        
        else:
            return self.playing()
    

    def playing(self):
        scores = {0:"Love",1:"Fifteen",2:"Thirty",3:"Forty"}  # sanakirjaa tarvitaan vain metodissa
        return f"{scores[self.player_1_score]}-{scores[self.player_2_score]}" # tulos sen mukaan kuin kummallkin on pisteitä

    def player_1_advantage(self): # etu player_1 pelaajalla ja myös voitto jos näin käy
        scores = {1:"Advantage "+self.player_1,2:"Win for "+self.player_1,3:"Win for "+self.player_1, 4:"Win for "+self.player_1} # sanakirjaa tarvitaan vain metodissa
        return scores[self.player_1_score - self. player_2_score]  
        

    def player_2_advantage(self): # etu player_2 pelaajalla ja myös voitto jos näin käy
        scores = {1:"Advantage "+self.player_2,2:"Win for "+self.player_2,3:"Win for "+self.player_2,4:"Win for "+self.player_2} # sanakirjaa tarvitaan vain metodissa
        return scores[self.player_2_score - self. player_1_score]
        
    def deuce_case(self):  # tänne tullaan tasapisteissä
        if self.player_1_score > 3:
            return "Deuce"  #  näin tavataan sanoa
        else:
            scores = {0:"Love-All",1:"Fifteen-All",2:"Thirty-All",3:"Forty-All"} # sanakirjaa tarvitaan vain metodissa
            return scores[self.player_1_score] # vaikka tässä on player_1, pitää muistaa että ollaan tasurissa

