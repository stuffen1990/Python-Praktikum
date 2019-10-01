class Match:

    def __init__(self, teamOne, teamTwo, priority = 0):
        self.teamOne = teamOne
        self.teamTwo = teamTwo
        self.priority = priority

    def setLocationTime(self, location, time):
        self.locTime = (location, time)

    def setResult(self, scoreTeamOne, scoreTeamTwo):
        self.scoreTeamOne = scoreTeamOne
        self.scoreTeamTwo = scoreTeamTwo

