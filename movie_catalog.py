from movie import Movie
import csv
import logging
logger = logging.getLogger(__name__)

from abc import ABC

class MovieCatalog:
    """Abstract base class for rental pricing."""
    _instance = None
    reader: list[dict] = []
    
    def __new__(cls):
        if not cls._instance:
            with open('movies.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls._instance = super(MovieCatalog, cls).__new__(cls)
                for number, row in enumerate(reader):
                    try:
                        _dict = {'id':row['#id'], 'title':row['title'], 'year':int(row['year']), "genres":row["genres"].split("|")}
                        cls._instance.reader.append(_dict)
                    except Exception:
                        info = [i for i in row.values()]
                        logger.error(f"Line {number} Unrecognized format '{info}'")
        return cls._instance

    def get_movie(self, title:str, year:int|None = None) -> Movie|None:
        for movie in self.reader:
            if movie['title'] == title:
                if year is None:
                    return Movie(movie['title'], movie['year'], movie['genres'])
                if movie['year'] == year:
                    return Movie(movie['title'], movie['year'], movie['genres'])
        return None