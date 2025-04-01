import os
import random
from PIL import Image, ImageDraw, ImageFont
from pdf2image import convert_from_path
from diamond import Diamond
from rectangle import Rectangle
from arrow import Arrow
from defs import Defs
from circle import Circle
from section_bbox import Section_Bbox

class Base:
    def __init__(self, width=Defs.width, height=Defs.height):

        cwd = os.getcwd()
        base_path = cwd + "/resources/base_ed.png"
        self.image = Image.open(base_path).convert("RGBA")
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = self.image.size

        # self.width = width
        # self.height = height
        # self.image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))

    def insert_onto_base(self, diamond_objects: [Diamond], rectangle_objects: [Rectangle], circle_objects: [Circle],arrow_objects: [Arrow], section_bbox_objects: [Section_Bbox]):

        self.paste_scaled_png()

        for rectangle_object in rectangle_objects:
            self.image.paste(rectangle_object.get_image(), rectangle_object.randomPosition, rectangle_object.get_image())

        for arrow_object in arrow_objects:
            self.image.paste(arrow_object.get_image(), arrow_object.randomPosition, arrow_object.get_image())

        for diamond_object in diamond_objects:
            self.image.paste(diamond_object.get_image(), diamond_object.randomPosition, diamond_object.get_image())

        for section_bbox_object in section_bbox_objects:
            self.image.paste(section_bbox_object.get_image(), section_bbox_object.randomPosition, section_bbox_object.get_image())

        for circle_object in circle_objects:
            self.image.paste(circle_object.get_image(), circle_object.randomPosition, circle_object.get_image())



    def get_random_path(self, folder_path:str):

        png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
        # Choose one at random
        if png_files:
            return os.path.join(folder_path, random.choice(png_files))
        else:
            raise FileNotFoundError("No PNG files found in the folder.")

    def paste_scaled_png(self):
        """
        Pastes a PNG onto the base image with optional scaling.

        :param png_path: Path to the PNG file
        :param position: (x, y) position on the base image
        :param scale: Scale factor (e.g., 0.5 for half size, 2.0 for double size)
        """


        png_path = self.get_random_path(folder_path= os.getcwd() + "/resources/cad_views/")

        position = (500, 200)
        scale = 3


        # Load PNG and convert to RGBA
        overlay = Image.open(png_path).convert("RGBA")

        # Scale PNG if needed
        if scale != 1.0:
            new_size = (int(overlay.width * scale), int(overlay.height * scale))
            overlay = overlay.resize(new_size, Image.Resampling.LANCZOS)

        # Paste using the alpha channel as mask
        self.image.paste(overlay, position, overlay)

    def show(self):
        """Displays the final large image."""
        self.image.show()

    def save(self, path):
        # Save the image

        # Scale down image size

        scale_factor = Defs.target_width / Defs.width

        compressed_image = self.image.resize((int(self.image.width*scale_factor), int(self.image.height * scale_factor)), Image.Resampling.LANCZOS)
        # Save the compressed image
        compressed_image.save(path, quality=95)  # Adjust quality if needed



