import unittest
from rental import Rental
from movie import Movie
from movie_catalog import MovieCatalog


class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.catalog = MovieCatalog()
		self.new_movie = self.catalog.get_movie("Dune: Part Two")
		self.regular_movie = self.catalog.get_movie("Arrival")
		self.childrens_movie = self.catalog.get_movie("Weathering With You")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		self.assertEqual(self.regular_movie.get_title(), "Arrival")

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.childrens_movie, 2)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5.0)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.rental_point(), 1.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.rental_point(), 5.0)
		rental = Rental(self.childrens_movie, 2)
		self.assertEqual(rental.rental_point(), 1.0)
		rental = Rental(self.childrens_movie, 5.0)
		self.assertEqual(rental.rental_point(), 1.0)
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.rental_point(), 1.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.rental_point(), 1.0)
