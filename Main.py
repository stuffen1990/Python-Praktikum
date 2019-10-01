import DataManagement as DM
import Tournament as TM
import Official as O

class Main:

    data = DM.DataManagement()
    data.addTournament(123)
    print(data.tournaments)
    tournament = TM.Tournament()
    official = O.Official("Max Mustermann")
    print(type(official.team))