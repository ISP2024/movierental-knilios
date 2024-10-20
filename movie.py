from dataclasses import dataclass

@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: list[str]
    
    def get_title(self):
        return self.title
    
    def is_genre(self, genre):
        return genre in self.genre
    
    def __str__(self):
        return f"{self.title} ({str(self.year)})"
    
