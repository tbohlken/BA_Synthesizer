import random
import os
from random import randint
from coordinate_tracker import CoordinateTracker
from defs import Defs
from PIL import Image
from utils import Utils

class Rivet:
    def __init__(self, image: Image.Image, x_offset: int, y_offset: int, group_origin: tuple):
        self.image = image

        self.width = image.width
        self.height = image.height

        self.relativeWidth = self.width / Defs.width
        self.relativeHeight = self.height / Defs.height

        self.local_x = x_offset
        self.local_y = y_offset

        self.global_x = group_origin[0] + x_offset
        self.global_y = group_origin[1] + y_offset

        self.xFraction = (self.global_x + 0.5 * self.width) / Defs.width  # Center x fraction
        self.yFraction = (self.global_y + 0.5 * self.height) / Defs.height


class RivetGroup:
    def __init__(self, tracker: CoordinateTracker, symbol_folder="resources/rivet_symbols", spacing=10):
        self.symbol_folder = symbol_folder
        self.rows = randint(Defs.min_rg_rows, Defs.max_rg_rows)
        self.cols = randint(Defs.min_rg_columns, Defs.max_rg_columns)

        self.scale = round(random.uniform(Defs.min_rg_scale, Defs.max_rg_scale), 2)

        # Get all PNG files
        symbol_paths = [os.path.join(self.symbol_folder, f) for f in os.listdir(self.symbol_folder) if
                        f.lower().endswith(".png")]
        if not symbol_paths:
            raise ValueError("No rivet symbols found in the specified folder.")

        # Get size from one symbol
        sample_symbol = Image.open(symbol_paths[0]).convert("RGBA")
        original_width, original_height = sample_symbol.size
        symbol_width = int(original_width * self.scale)
        symbol_height = int(original_height * self.scale)

        # Set default spacing based on scaled size if not provided
        self.spacing = spacing if spacing is not None else int(min(symbol_width, symbol_height) * 0.5)

        # Create the final image canvas
        canvas_width = self.cols * symbol_width + (self.cols - 1) * self.spacing
        canvas_height = self.rows * symbol_height + (self.rows - 1) * self.spacing
        self.image = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

        self.rivets = []

        self.randX, self.randY = Utils.generate_rand_allowed_xyPos(canvas_width, canvas_height)

        while True:
            if tracker.is_overlapping(self.randX, self.randY, canvas_width, canvas_height):
                self.randX, self.randY = Utils.generate_rand_allowed_xyPos(canvas_width, canvas_height)
            else:
                break

        self.randomPosition = (self.randX, self.randY)

        # Paste scaled symbols into grid
        for row in range(self.rows):
            for col in range(self.cols):
                symbol_path = random.choice(symbol_paths)
                symbol = Image.open(symbol_path).convert("RGBA")
                symbol = symbol.resize((symbol_width, symbol_height), Image.Resampling.LANCZOS)
                x = col * (symbol_width + self.spacing)
                y = row * (symbol_height + self.spacing)
                self.image.paste(symbol, (x, y), symbol)
                rivet = Rivet(symbol, x, y, (self.randX, self.randY))
                self.rivets.append(rivet)


    def get_image(self):
        """Returns the generated rivet grid image."""
        return self.image
