"""Object oriented programming practice."""
from __future__ import annotations


class Point:
    """Create class."""
    x: float
    y: float

    # constructor
    def __init__(self, x_init: float, y_init: float):
        """Create new point object."""
        self.x = x_init
        self.y = y_init

    # mutating method
    def scale_by(self, factor: int) -> None:
        """Update x and y by multiplying it by factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    # mutating method
    def scale(self, factor: int) -> Point:
        """Update x and y by multiplying it by factor."""
        x = self.x * factor
        y = self.y * factor
        return Point(x, y)