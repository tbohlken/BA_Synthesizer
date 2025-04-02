from PIL import Image, ImageDraw, ImageFont
from utils import Utils
from coordinate_tracker import CoordinateTracker
from defs import Defs
import random, string

class Cross:
    def __init__(self, tracker: CoordinateTracker, width=150, height=150, line_width=5, font_size=30):
        """
        Creates a cross with optional text in each of the four quadrants:
        texts = (top_left, top_right, bottom_left, bottom_right)
        """
        self.scale = round(random.uniform(Defs.min_cross_scale_factor, Defs.max_cross_scale_factor), 2)
        self.width = int(width * self.scale)
        self.height = int(height * self.scale)
        self.line_width = line_width
        self.font_size = int(font_size * self.scale)

        self.image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)

        self._draw_cross()
        self._draw_texts()

        self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.width, self.height)

        while True:
            if tracker.is_overlapping(self.randX, self.randY, self.width, self.height):
                self.randX, self.randY = Utils.generate_rand_allowed_xyPos(self.width, self.height)
            else:
                break

        self.randomPosition = (self.randX, self.randY)

        self.relativeWidth = self.width / Defs.width
        self.relativeHeight = self.height / Defs.height

        self.xFraction = (self.randX + 0.5 * self.width) / Defs.width  # Center x fraction
        self.yFraction = (self.randY + 0.5 * self.height) / Defs.height  # Center y fraction

    def _draw_cross(self):
        cx = self.width // 2
        cy = self.height // 2
        # Vertical line
        self.draw.line([(cx, 0), (cx, self.height)], fill="black", width=self.line_width)
        # Horizontal line
        self.draw.line([(0, cy), (self.width, cy)], fill="black", width=self.line_width)

    def _draw_texts(self):
        font = ImageFont.truetype("Arial.ttf", self.font_size)
        cx = self.width // 2
        cy = self.height // 2

        positions = [
            (cx // 2, cy // 2),                  # top left
            (cx + cx // 2, cy // 2),             # top right
            (cx // 2, cy + cy // 2),             # bottom left
            (cx + cx // 2, cy + cy // 2)         # bottom right
        ]

        if random.random() < 0.5:
            tl = str(random.randint(1000,9999))
        else:
            tl = str(random.randint(1000, 9999)) + "\n" + str(random.randint(1000, 9999))

        tr = random.choice(string.ascii_uppercase)
        br = str(round(random.uniform(1.0, 9.9), 1))
        texts = (tl, tr, "△", br)

        for text, (x, y) in zip(texts, positions):
            bbox = self.draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            self.draw.text((x - text_width // 2, y - text_height // 2), text, font=font, fill="black")

    def get_image(self):
        return self.image