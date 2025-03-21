from defs import Defs
class CoordinateTracker:
    def __init__(self, delta=25):
        """Initialize the tracker with a fixed delta range."""
        self.delta = delta

        self.used_spaces = []  # List to store boxes (each box is a tuple: (x_min, x_max, y_min, y_max))


    def is_overlapping(self, x, y, obj_width, obj_height):
        """Checks if the new box overlaps with any existing boxes."""

        x_min, x_max, y_min, y_max = x, x + obj_width, y, y + obj_height

        for box in self.used_spaces:
            bx_min, bx_max, by_min, by_max = box
            if not (x_max < bx_min or x_min > bx_max or y_max < by_min or y_min > by_max):
                return True  # Overlapping detected
        self.used_spaces.append((x_min, x_max, y_min, y_max))
        return False  # No overlap, therefore add new box to used spaces


