from matchers import All, PlaysIn


class QueryBuilder:
    def __init__(self, matcher = None):
        self.matcher = matcher or All()
    
    def build(self):
        return self.matcher
    
    def playsIn(self, team):
        return QueryBuilder(self.matcher and PlaysIn(team))
            
