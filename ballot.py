class Ballot(dict):

    def __eq__(self, other):
        return self['Receipt'] == other['Receipt']

    def __hash__(self):
        return int(self['Receipt'], 36)
