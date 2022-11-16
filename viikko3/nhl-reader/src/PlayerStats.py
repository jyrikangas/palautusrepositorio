
class PlayerStats:
    def __init__(self, reader) -> None:
        self.reader = reader
        
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered = []
        for p in players:
            if p.nationality == nationality:
                filtered.append(p)
        
        filtered.sort(key = lambda x : x.points)
        return filtered