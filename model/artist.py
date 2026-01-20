from dataclasses import dataclass

@dataclass
class Artist:
    id : int
    name : str
    genre: set

    def add_genre(self,g):
        self.genre.add(g)

    def __str__(self):
        return f"{self.id}, {self.name}"

    def __hash__(self):
        return hash(self.id)