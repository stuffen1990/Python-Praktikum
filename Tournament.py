class Tournament:

    def __init__(self, identifier, numberOfLocations = 1, officialPositions = []):
        self.identifier = identifier
        self.numberOfLocations = numberOfLocations
        self.officialPositions = officialPositions
        self.teams = []
        self.officials = []
        self.phases = []