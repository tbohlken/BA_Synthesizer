from random import randint
from defs import Defs
from utils import Utils
from coordinate_tracker import CoordinateTracker
from PIL import Image, ImageDraw, ImageFont

class Diamond:
    def __init__(self):
        """Initialize a small 500x500 image with a diamond shape and centered text."""
        width = randint(Defs.min_diamond_width, Defs.max_diamond_width)
        width = 120
        height = int(width * 2 / 3)






        self.width = width
        self.height = height
        self.relativeWidth = self.width / Defs.width
        self.relativeHeight = self.height / Defs.height

        #Position vars
        self.randomPosition = (0, 0)
        self.randomXFraction = 0.0
        self.randomYFraction = 0.0

        '''
        = (self.randX + 0.5*self.width) / Defs.width #Center x fraction
        = (self.randY + 0.5*self.height) / Defs.height #Center y fraction

        self.randomPosition = (self.randX, self.randY)
        
        '''




        self.image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)
        self._draw_diamond()
        self._draw_text()





    def setPosition(self, arrangementPos, xOffset, yOffset):



        self.randomPosition = (arrangementPos[0] + xOffset, arrangementPos[1] + yOffset)
        self.randomXFraction = (self.randomPosition[0]+ 0.5*self.width) / Defs.width #Center x fraction
        self.randomYFraction = (self.randomPosition[1] + 0.5*self.height) / Defs.height


    def _draw_diamond(self):
        """Draws a diamond shape in the center of the small image."""
        diamond = [
            (self.width // 2, 0),  # Top
            (self.width, self.height // 2),  # Right
            (self.width // 2, self.height),  # Bottom
            (0, self.height // 2)  # Left
        ]


        self.draw.polygon(diamond, fill="white", outline="black", width=5)

    def _draw_text(self):
        font = ImageFont.truetype("Arial.ttf", Defs.diamond_number_font_size)

        #Generate random number
        number = str(randint(10, 50))
        bbox = self.draw.textbbox((0, 0), number, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        text_x = (self.width - text_width) // 2 - 8
        text_y = (self.height - text_height) // 2 - 5

        formatted = str(number).zfill(3)

        self.draw.text((text_x, text_y), formatted, font=font, fill=(0, 0, 0))

    def get_image(self):
        """Returns the generated small image."""
        return self.image