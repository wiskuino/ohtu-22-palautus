class TennisGame:
    def __init__(self, name_1, name_2):
        self.player_1 = name_1
        self.player_2 = name_2
        self.player_1_points = 0
        self.player_2_points = 0
        self.scoring_call = {0:"Love",1:"Fifteen",2:"Thirty",3:"Forty"}

    def won_point(self, player):
        if player == self.player_1:
            self.player_1_points += 1
        else:
            self.player_2_points += 1

    def get_score(self):

        if (self.player_1_points >= 4 or self.player_2_points >= 4) and self.player_1_points != self.player_2_points:
            leader = self.player_1 if self.player_1_points > self.player_2_points else self.player_2
            return self.player_x_advantage(leader,abs(self.player_1_points - self. player_2_points)) 

        else:
            return self.continue_playing()

    def player_x_advantage(self,leader,leader_points): 
        cases = {1:"Advantage "+leader,2:"Win for "+leader,3:"Win for "+leader, 4:"Win for "+leader} 
        return cases[leader_points]

    def deuce(self):
        return "Deuce" if self.player_1_points > 3 else f"{self.scoring_call[self.player_1_points]}-All" 
    
    def continue_playing(self):
        return f"{self.scoring_call[self.player_1_points]}-{self.scoring_call[self.player_2_points]}" \
             if self.player_2_points != self.player_1_points else self.deuce()
            
            

    
    
    
    

