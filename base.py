import os
import random
from PIL import Image, ImageDraw, ImageFont
from pdf2image import convert_from_path

from cadview import CadView
from diamond_group import DiamondGroup
from rectangle import Rectangle
from arrow import Arrow
from defs import Defs
from circle import Circle
from rivet_group import RivetGroup
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

    def insert_onto_base(self, diamond_objects: [DiamondGroup],
                         rectangle_objects: [Rectangle],
                         circle_objects: [Circle],
                         arrow_objects: [Arrow],
                         section_bbox_objects: [Section_Bbox],
                         cadview_objects: [CadView],
                         rg_objects: [RivetGroup]):

        for rectangle_object in rectangle_objects:
            self.image.paste(rectangle_object.get_image(), rectangle_object.randomPosition, rectangle_object.get_image())

        for cadview_object in cadview_objects:
            self.image.paste(cadview_object.get_image(), cadview_object.randomPosition,
                             cadview_object.get_image())

        for arrow_object in arrow_objects:
            self.image.paste(arrow_object.get_image(), arrow_object.randomPosition, arrow_object.get_image())

        for diamond_object in diamond_objects:
            self.image.paste(diamond_object.get_image(), diamond_object.randomPosition, diamond_object.get_image())

        for rg_object in rg_objects:
            self.image.paste(rg_object.get_image(), rg_object.randomPosition, rg_object.get_image())

        for section_bbox_object in section_bbox_objects:
            self.image.paste(section_bbox_object.get_image(), section_bbox_object.randomPosition, section_bbox_object.get_image())

        for circle_object in circle_objects:
            self.image.paste(circle_object.get_image(), circle_object.randomPosition, circle_object.get_image())





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



