from movie import Movie
import logging
from pricing import NEW_RELEASE, REGULAR, CHILDREN, PriceStrategy

class Rental:
   """
   A rental of a movie by customer.
   From Fowler's refactoring example.

   A realistic Rental would have fields for the dates
   that the movie was rented and returned, from which the
   rental period is calculated.
   For simplicity of this application only days_rented is recorded.
   """
   
   # The types of movies (price_code). 
   REGULAR = REGULAR
   NEW_RELEASE = NEW_RELEASE
   CHILDRENS = CHILDREN
    
   def __init__(self, movie, days_rented, price_code): 
      """Initialize a new movie rental object for
         a movie with known rental period (daysRented).
      """
      self.movie = movie
      self.days_rented = days_rented
      self.price_code = price_code
      
   def get_price_code(self) -> PriceStrategy:
      # get the price code
      return self.price_code

   def get_movie(self) -> Movie:
      return self.movie

   def get_days_rented(self) -> int:
      return self.days_rented
  
   def get_price(self) -> float:
      return self.get_price_code().get_price(self.get_days_rented())
     
   def rental_point(self):
      return self.get_price_code().get_rental_points(self.get_days_rented())
        
