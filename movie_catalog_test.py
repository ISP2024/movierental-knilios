import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie
from movie_catalog import MovieCatalog


class MovieCatalogTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    	
    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.catalog = MovieCatalog()
        
    def test_find_movie_in_catalog(self):
        movie = self.catalog.get_movie("Mulan")
        self.assertEqual(movie.title, "Mulan")