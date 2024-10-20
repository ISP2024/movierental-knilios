import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie
from movie_catalog import MovieCatalog
from pricing import NEW_RELEASE, REGULAR, CHILDREN, PriceStrategy


class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    	
    def setUp(self):
        """Test fixture contains:
        
        c = a customer
        movies = list of some movies
        """
        self.catalog = MovieCatalog()
        
    def test_pricing_children_movie(self):
        children1 = self.catalog.get_movie("Cinderella")
        self.assertEqual(Rental.get_price_for_movie(children1), CHILDREN)
        
    def test_pricing_new_movie(self):
        new_release1 = self.catalog.get_movie("Bitconned")
        self.assertEqual(Rental.get_price_for_movie(new_release1), NEW_RELEASE)

    def test_pricing_regular_movie(self):
        regular1 = self.catalog.get_movie("Django/Zorro")
        self.assertEqual(Rental.get_price_for_movie(regular1), REGULAR)
	
