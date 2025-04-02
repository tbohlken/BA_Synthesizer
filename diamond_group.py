from diamond import Diamond
from PIL import Image
from utils import Utils
from defs import Defs
import random


class DiamondGroup:


    def __init__(self, tracker, num_diamonds, vertical_spacing_factor=0.48, arrangement_direction="left"):

        """
            Creates a group of diamonds arranged in a structured pattern.
            :param tracker: instance of CoordinateTracker to avoid overlaps
            :param num_diamonds: number of diamonds to place
            :param vertical_spacing_factor: how much to overlap vertically (e.g., 0.75 means 25% overlap)
            :param arrangement_direction: direction of arrangement ("left" or "right")
            """
        self.diamonds = []
        self.image = None
        self.scale = round(random.uniform(Defs.min_diamond_scale_factor, Defs.max_diamond_scale_factor), 2)
        # Create and store diamonds
        for i in range(num_diamonds):
            diamond = Diamond(self.scale)
            self.diamonds.append(diamond)

        # Determine max image size
        canvas_width = max(d.width for d in self.diamonds)
        canvas_height = sum(int(d.height * vertical_spacing_factor) for d in self.diamonds)

        self.randX, self.randY = Utils.generate_rand_allowed_xyPos(canvas_width*2, canvas_height*2)

        while True:
            if tracker.is_overlapping(self.randX, self.randY, canvas_width*2, canvas_height*2):
                self.randX, self.randY = Utils.generate_rand_allowed_xyPos(canvas_width*2, canvas_height*2)
            else:
                break

        self.randomPosition = (self.randX, self.randY)



        if arrangement_direction is None:
            arrangement_direction = random.choice(["left", "right"])
        self.arrangement_direction = arrangement_direction

        self.image = Image.new("RGBA", (int(canvas_width*2), int(canvas_height*2)), (255, 255, 255, 0))

        for i, diamond in enumerate(self.diamonds):
            if self.arrangement_direction == "right":
                x_offset = canvas_width // 2 if i % 2 == 1 else 0
            else:  # "left"
                x_offset = canvas_width // 2 if i % 2 == 0 else 0
            y_offset = int(i * diamond.height * vertical_spacing_factor)

            self.image.paste(diamond.image, (x_offset, y_offset), diamond.image)

            diamond.setPosition(self.randomPosition, x_offset, y_offset)



    def get_image(self):
        """Returns the generated small image."""
        return self.image