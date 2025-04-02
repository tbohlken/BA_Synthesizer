
import os
import random
from defs import Defs
from PIL import Image, ImageDraw



class CadView:
    def __init__(self, pos: int):
        scale = 2


        # Load and scale the random PNG first
        folder_path = os.path.join(os.getcwd(), "resources", "cad_views")
        png_path = self.get_random_path(folder_path)
        overlay = Image.open(png_path).convert("RGBA")

        if scale != 1.0:
            new_size = (int(overlay.width * scale), int(overlay.height * scale))
            overlay = overlay.resize(new_size, Image.Resampling.LANCZOS)

        # Create an image with RGBA mode (supports transparency)
        self.image = Image.new("RGBA", (overlay.width, overlay.height), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)


        # Paste the scaled PNG onto this image
        self.image.paste(overlay, (0, 0), overlay)

        horizontalPadding = 200
        verticalPadding = 400
        if pos == 1:
            self.randomPosition = (Defs.margin_left + horizontalPadding, Defs.margin_top + verticalPadding)
        elif pos == 2:
            self.randomPosition = (Defs.width-Defs.margin_right-overlay.width-horizontalPadding, Defs.margin_top + verticalPadding)
        else:
            self.randomPosition = (Defs.margin_left + horizontalPadding, Defs.height - Defs.margin_bottom - overlay.height - verticalPadding)




    def get_random_path(self, folder_path: str):

        png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
        # Choose one at random
        if png_files:
            return os.path.join(folder_path, random.choice(png_files))
        else:
            raise FileNotFoundError("No PNG files found in the folder.")

    def get_image(self):
        """Returns the generated small image."""
        return self.image