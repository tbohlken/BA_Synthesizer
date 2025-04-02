from random import randint
from coordinate_tracker import CoordinateTracker
from rivet_group import RivetGroup
from utils import Utils
from diamond import Diamond
from rectangle import Rectangle
from arrow import Arrow
from defs import Defs
from circle import Circle
from section_bbox import Section_Bbox
from cadview import CadView
from diamond_group import DiamondGroup



class ObjectManager:

    def __init__(self, fileName):
        self.diamond_list = []
        self.circle_list = []
        self.rectangle_list = []
        self.arrow_list = []
        self.section_bbox_list = []
        self.cadview_list = []
        self.rg_list = []

        self.fileName = fileName  # Save file name for use in label output

        self.tracker =  CoordinateTracker() #Tracker for detectable objects

        self.diamond_tracker = self.tracker
        self.circle_tracker = self.tracker

        self.arrow_tracker = CoordinateTracker()
        self.rectangle_tracker = CoordinateTracker()


    def generate_diamonds(self):



        # Generate diamonds
        for i in range(randint(Defs.min_diamond_count, Defs.max_diamond_count)):
            group = DiamondGroup(tracker=self.tracker, num_diamonds=randint(1, 4))
            self.diamond_list.append(group)
            for diamond_obj in group.diamonds:
                with open(Defs.dataset_name + "/labels/" + self.fileName + ".txt",
                          "a") as file:  # Append mode, file is created if missing
                    file.write(
                        f"0 {diamond_obj.randomXFraction} {diamond_obj.randomYFraction} {diamond_obj.relativeWidth} {diamond_obj.relativeHeight}\n")



    def generate_rivet_groups(self):
        for i in range(randint(Defs.min_rg_count, Defs.max_rg_count)):
            rg_object = RivetGroup(self.tracker)
            self.rg_list.append(rg_object)




    def generate_rectangles(self):
        # Generate rectangles
        for i in range(randint(Defs.min_rectangle_count, Defs.max_rectangle_count)):
            rectangle_obj = Rectangle(self.rectangle_tracker)
            self.rectangle_list.append(rectangle_obj)

    def generate_cadviews(self):
        # Generate rectangles
        for i in range(3): #Three views (emulating front view, top, and left)

            cadview_obj = CadView(pos = i)

            self.cadview_list.append(cadview_obj)


    def generate_arrows(self):
        # Generate arrows
        for i in range(randint(Defs.min_arrow_count, Defs.max_arrow_count)):
            arrow_obj = Arrow(self.arrow_tracker)
            self.arrow_list.append(arrow_obj)

    def generate_section_bbox(self):
        # Generate section_bbox
        for i in range(10):
            section_bbox_obj = Section_Bbox(self.tracker)
            self.section_bbox_list.append(section_bbox_obj)

            with open(Defs.dataset_name + "/labels/" + self.fileName + ".txt",
                      "a") as file:  # Append mode, file is created if missing
                file.write(
                    f"2 {section_bbox_obj.randomXFraction} {section_bbox_obj.randomYFraction} {section_bbox_obj.relativeWidth} {section_bbox_obj.relativeHeight}\n")

    def generate_circles(self):
        # Generate circles
        for i in range(randint(Defs.min_circle_count, Defs.max_circle_count)):
            circle_obj = Circle(self.tracker)
            self.circle_list.append(circle_obj)

            with open(Defs.dataset_name + "/labels/" + self.fileName + ".txt",
                      "a") as file:  # Append mode, file is created if missing
                file.write(
                    f"1 {circle_obj.randomXFraction} {circle_obj.randomYFraction} {circle_obj.relativeWidth} {circle_obj.relativeHeight}\n")

    def get_objects(self):

        return self.diamond_list, self.rectangle_list, self.circle_list, self.arrow_list, self.section_bbox_list, self.cadview_list, self.rg_list