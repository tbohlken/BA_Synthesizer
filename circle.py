from random import randint
from defs import Defs
from utils import Utils
from coordinate_tracker import CoordinateTracker
from PIL import Image, ImageDraw, ImageFont


class Circle:

    def __init__(self, tracker: CoordinateTracker):

        """Initialize a small 500x500 image with a diamond shape and centered text."""
        self.circle_diameter = randint(Defs.min_circle_diameter, Defs.max_circle_diameter)
        self.circle_radius = self.circle_diameter/2

        self.relativeWidth = self.circle_diameter / Defs.width
        self.relativeHeight = self.circle_diameter / Defs.height

        self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.circle_diameter, self.circle_diameter)

        while True:
            if tracker.is_overlapping(self.randX, self.randY, self.circle_diameter, self.circle_diameter):
                self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.circle_diameter, self.circle_diameter)
            else:
                break

        self.randomXFraction = (self.randX + 0.5 * self.circle_diameter) / Defs.width  # Center x fraction
        self.randomYFraction = (self.randY + 0.5 * self.circle_diameter) / Defs.height  # Center y fraction

        self.randomPosition = (self.randX, self.randY)

        self.image = Image.new("RGBA", (self.circle_diameter, self.circle_diameter), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)
        self._draw_circle()
        self._draw_text()

    def _draw_circle(self):
        """Draws a diamond shape in the center of the small image."""
        self.draw.ellipse((0, 0, self.circle_diameter, self.circle_diameter), fill="white", outline="black", width=5)

    def _draw_text(self):
        font = ImageFont.truetype("Arial.ttf", Defs.circle_number_font_size)

        #Generate random number
        number = str(randint(10, 50))
        bbox = self.draw.textbbox((0, 0), number, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        text_x = (self.circle_diameter - text_width) // 2
        text_y = (self.circle_diameter - text_height) // 2 - 5

        self.draw.text((text_x, text_y), number, font=font, fill=(0, 0, 0))

    def get_image(self):
        """Returns the generated small image."""
        return self.image
