class TournamentPhase:

    def __init__(self, tournament, pairingType, numberOfRounds = 1):
        self.tournament = tournament
        self.pairingType = pairingType
        self.numberOfRounds = int(numberOfRounds)