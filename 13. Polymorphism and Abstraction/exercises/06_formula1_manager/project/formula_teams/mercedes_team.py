from project.formula_teams.formula_team import FormulaTeam

class MercedesTeam(FormulaTeam):
    @property
    def team_data(self):
        sponsors = {"Petronas": {1: 1000000, 3: 500000}, "TeamViewer": {5: 100000, 7: 50000}}
        expenses = 200000
        return sponsors, expenses