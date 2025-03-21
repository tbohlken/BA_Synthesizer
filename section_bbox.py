from random import randint
from defs import Defs
from utils import Utils
from coordinate_tracker import CoordinateTracker
from PIL import Image, ImageDraw, ImageFont

class Section_Bbox:
    def __init__(self, tracker: CoordinateTracker):
        """Initialize a small 500x500 image with a diamond shape and centered text."""
        self.width = 400
        self.height = 100

        self.relativeWidth = self.width / Defs.width
        self.relativeHeight = self.height / Defs.height

        self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.width, self.height)

        while True:
            if tracker.is_overlapping(self.randX, self.randY, self.width, self.height):
                self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.width, self.height)
            else:
                break


        self.randomXFraction = (self.randX + 0.5*self.width) / Defs.width #Center x fraction
        self.randomYFraction = (self.randY + 0.5*self.height) / Defs.height #Center y fraction

        self.randomPosition = (self.randX, self.randY)

        self.image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

        self._draw_text()






    def _draw_text(self):
        font = ImageFont.truetype("Arial.ttf", 50)

        #Generate random number
        number = str(randint(10, 50))
        bbox = self.draw.textbbox((0, 0), number, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        text_x = 0
        text_y = (self.height-text_height) // 2


        self.draw.text((text_x, text_y), "SECTION X3-A7", font=font, fill=(0, 0, 0))

    def get_image(self):
        """Returns the generated small image."""
        return self.image