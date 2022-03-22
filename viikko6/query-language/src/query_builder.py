from matchers import All, And, Or, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def plays_in(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def one_of(self, query1, query2):
        return QueryBuilder(Or(query1, query2))