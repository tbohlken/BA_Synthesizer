from random import randint
from coordinate_tracker import CoordinateTracker
from utils import Utils
from defs import Defs
from PIL import Image, ImageDraw, ImageFont


class Rectangle:
    def __init__(self, tracker: CoordinateTracker):

        self.rectangle_width = randint(Defs.rect_min_width, Defs.rect_max_width)
        self.rectangle_height = randint(Defs.rect_min_height, Defs.rect_max_height)

        self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.rectangle_width, self.rectangle_height)
        """
        while True:
            print(f"Checking overlap for upper left: ({self.randX}, {self.randY}), bottom right: ({self.randX + self.rectangle_width}, {self.randY + self.rectangle_height})")  # Debugging print
            if tracker.is_overlapping(self.randX, self.randY, self.rectangle_width, self.rectangle_height):
                print("Overlap detected! Regenerating position...")
                self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.rectangle_width, self.rectangle_height)
            else:
                print("No overlap. Breaking loop.")
                break  # ✅ This exits immediately if there's no overlap

        """

        self.randomPosition = (self.randX, self.randY)

        # Create an image with RGBA mode (supports transparency)
        self.image = Image.new("RGBA", (self.rectangle_width, self.rectangle_height), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)

        self._draw_rectangle()



    def _draw_rectangle(self):




        origin_x = 0
        origin_y = 0
        diamond = [
            (origin_x, origin_y),  # Top
            (origin_x+self.rectangle_width, origin_y),  # Right
            (origin_x+self.rectangle_width, origin_y+self.rectangle_height),  # Bottom
            (origin_x, origin_y+self.rectangle_height)  # Left
        ]
        self.draw.polygon(diamond, outline="black", width=5, fill=None)

    def get_image(self):
        """Returns the generated small image."""
        return self.image

