from matchers import And, Or, All, PlaysIn, HasAtLeast, HasFewerThan


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

    def oneOf(self,query1,query2):
        self.query1 = query1
        self.query2= query2
        return QueryBuilder(Or(self.query1,self.query2))

            
