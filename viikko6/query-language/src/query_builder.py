from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.matcher = matcher
    
    def build(self):
        return self.matcher
    
    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))
    def playsIn(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attribute):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attribute)))
    
    def hasFewerThan(self, value, attribute):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attribute))) 