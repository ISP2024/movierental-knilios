from movie import Movie
import logging

class Rental:
   """
   A rental of a movie by customer.
   From Fowler's refactoring example.

   A realistic Rental would have fields for the dates
   that the movie was rented and returned, from which the
   rental period is calculated.
   For simplicity of this application only days_rented is recorded.
   """
    
   def __init__(self, movie, days_rented): 
      """Initialize a new movie rental object for
         a movie with known rental period (daysRented).
      """
      self.movie = movie
      self.days_rented = days_rented

   def get_movie(self) -> Movie:
      return self.movie

   def get_days_rented(self) -> int:
      return self.days_rented
  
   def get_price(self) -> float:
      return self.get_movie().get_price(self.get_days_rented())
     
   def rental_point(self, frequent_renter_points: float):
      return self.get_movie().get_rental_points(self.get_days_rented())
      if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
         # New release earns 1 point per day rented
         return frequent_renter_points + self.get_days_rented()
      else:
         # Other rentals get only 1 point
         return frequent_renter_points + 1
        
