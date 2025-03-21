from random import randint

from PIL import Image, ImageDraw
from coordinate_tracker import CoordinateTracker
from utils import Utils
from defs import Defs
import math


class Arrow:
    def __init__(self, tracker: CoordinateTracker):
        self.length = randint(Defs.min_arrow_length, Defs.max_arrow_length)


        self.orientation = randint(0,1)

        if self.orientation == 0:

            self.width = self.length
            self.height = 30
            self.angle = math.radians(0)  # Convert degrees to radians
        else:
            self.width = 30
            self.height = self.length
            self.angle = math.radians(90)  # Convert degrees to radians



        #Generate random x and y position coordinates
        self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.width, self.height)
        while True:
            if tracker.is_overlapping(self.randX, self.randY, self.width, self.height):
                self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.width, self.height)
            else:
                break

        self.randomPosition = (self.randX, self.randY)


        self.image_size = (self.width, self.length)
        self.image = Image.new("RGBA", self.image_size, (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)

        self.draw_arrow()

    def draw_arrow(self):
        center = (self.image_size[0] // 2, self.image_size[1] // 2)
        half_length = self.length // 2

        # Calculate arrow line endpoints
        x1 = center[0] - half_length * math.cos(self.angle)
        y1 = center[1] - half_length * math.sin(self.angle)
        x2 = center[0] + half_length * math.cos(self.angle)
        y2 = center[1] + half_length * math.sin(self.angle)

        # Draw the main line
        self.draw.line([(x1, y1), (x2, y2)], fill="black", width=2)

        # Draw arrowheads (triangles)
        self._draw_arrowhead((x1, y1), self.angle + math.pi)  # Left arrowhead
        self._draw_arrowhead((x2, y2), self.angle)  # Right arrowhead

    def _draw_arrowhead(self, tip, angle):
        size = 10  # Fixed size of arrowhead

        # Calculate triangle points
        x1 = tip[0] + size * math.cos(angle + math.radians(150))
        y1 = tip[1] + size * math.sin(angle + math.radians(150))
        x2 = tip[0] + size * math.cos(angle - math.radians(150))
        y2 = tip[1] + size * math.sin(angle - math.radians(150))

        self.draw.polygon([tip, (x1, y1), (x2, y2)], fill="black")

    def get_image(self):
        """Returns the generated small image."""
        return self.image
