import logging
import enum
from pricing import NEW_RELEASE, REGULAR, CHILDREN, PriceStrategy
    

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = REGULAR
    NEW_RELEASE = NEW_RELEASE
    CHILDRENS = CHILDREN
    
    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> PriceStrategy:
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title
