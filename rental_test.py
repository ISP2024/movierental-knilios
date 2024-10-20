import unittest
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.new_movie = Movie("Dune: Part Two")
		self.regular_movie = Movie("Air")
		self.childrens_movie = Movie("Frozen")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air")
		self.assertEqual("Air", m.get_title())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.childrens_movie, 2, Rental.CHILDRENS)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5.0, Rental.CHILDRENS)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.regular_movie, 2, Rental.REGULAR)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 5, Rental.REGULAR)
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
		self.assertEqual(rental.rental_point(), 1.0)
		rental = Rental(self.new_movie, 5,  Rental.NEW_RELEASE)
		self.assertEqual(rental.rental_point(), 5.0)
		rental = Rental(self.childrens_movie, 2, Rental.CHILDRENS)
		self.assertEqual(rental.rental_point(), 1.0)
		rental = Rental(self.childrens_movie, 5.0, Rental.CHILDRENS)
		self.assertEqual(rental.rental_point(), 1.0)
		rental = Rental(self.regular_movie, 2, Rental.REGULAR)
		self.assertEqual(rental.rental_point(), 1.0)
		rental = Rental(self.regular_movie, 5, Rental.REGULAR)
		self.assertEqual(rental.rental_point(), 1.0)
