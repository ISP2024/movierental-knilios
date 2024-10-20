from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass
    
    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days
    
    def get_price(self, days):
        return 3*days
        

class RegularPrice(PriceStrategy):
    """Pricing"""
    
    def get_rental_points(self, days=None):
        """New release rentals earn 1 point for each day rented."""
        return 1
    
    def get_price(self, days):
        if days > 2:
            return 1.5*(days-2)
        return 2.0
    
class ChildrenPrice(PriceStrategy):
    """Pricing"""
    
    def get_rental_points(self, days=None):
        """New release rentals earn 1 point for each day rented."""
        return 1
    
    def get_price(self, days):
        if days > 3:
            return 1.5*(days-3)
        return 1.5

# Define instances of the strategies as named constants
NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrenPrice()