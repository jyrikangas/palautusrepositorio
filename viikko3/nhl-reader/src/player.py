class Player:
    def __init__(self, name, nationality, team, games, assists, goals, penalties):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.games = games
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20}  {self.team} + {str(self.goals)} + {str(self.assists)} =  {str(self.points)}"
    
