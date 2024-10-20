import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie
from movie_catalog import MovieCatalog

class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
		
	def setUp(self):
		"""Test fixture contains:
				
		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.catalog = MovieCatalog()
		self.new_movie = self.catalog.get_movie("Dune: Part Two")
		self.regular_movie = self.catalog.get_movie("Arrival")
		self.childrens_movie = self.catalog.get_movie("Weathering With You")
	
	def test_billing(self):
		# no convenient way to test billing since its buried in the statement() method.
		customer = Customer("Movie Monster")
		customer.add_rental(Rental(self.new_movie, 1))
		self.assertEqual(customer.get_total_amount(), 3)
		customer.add_rental(Rental(self.childrens_movie, 2))
		self.assertEqual(customer.get_total_amount(), 4.5)
		customer.add_rental(Rental(self.regular_movie, 5))
		self.assertEqual(customer.get_total_amount(), 9.0)
  		
	def test_statement(self):
		stmt = self.c.statement()
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
  
	def test_get_rental_points(self):
		customer = Customer("Movie Monster")
		customer.add_rental(Rental(self.new_movie, 3))
		self.assertEqual(customer.get_rental_points(), 3)
		customer.add_rental(Rental(self.childrens_movie, 2))
		self.assertEqual(customer.get_rental_points(), 4)
		customer.add_rental(Rental(self.regular_movie, 5))
		self.assertEqual(customer.get_rental_points(), 5)
