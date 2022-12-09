from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan


class QueryBuilder:
    def __init__(self, matcher = None):
        self.matcher = matcher or All()
    
    def build(self):
        return self.matcher
    
    def playsIn(self,team):
        self.team =team
        return QueryBuilder(And(self.matcher, PlaysIn(self.team)))

    def hasAtLeast(self, value, attr):
        self.value = value
        self.attr = attr
        return QueryBuilder(And(self.matcher, HasAtLeast(self.value,self.attr)))
    
    def hasFewerThan(self,value,attr):
        self.value = value
        self.attr = attr
        return (QueryBuilder(And(self.matcher, HasFewerThan(self.value,self.attr))))


            
