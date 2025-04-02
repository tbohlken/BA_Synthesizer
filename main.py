from random import randint

from coordinate_tracker import CoordinateTracker
from diamond import Diamond
from base import Base
from rectangle import Rectangle
from arrow import Arrow
from defs import Defs
from utils import Utils
from circle import Circle
from section_bbox import Section_Bbox
from object_manager import ObjectManager

import visualizer

Utils.build_directory()
Utils.make_classes_file()
Utils.make_json()


for n in range(Defs.synth_count):


    # Creates background
    base_img = Base()

    fileName = "synth_drawing_" + str(n)
    object_manager = ObjectManager(fileName) #Class that generates and manages objects


    scale_factor = Defs.target_width / Defs.width



    object_manager.generate_diamonds()

    #object_manager.generate_rectangles()
    object_manager.generate_cadviews()



    object_manager.generate_section_bbox()

    object_manager.generate_arrows()

    object_manager.generate_circles()

    # Insert classes onto base
    base_img.insert_onto_base(*object_manager.get_objects())


    # Show and save final image
    base_img.save(Defs.dataset_name + "/images/" + fileName + ".png")


    visualizer.visualize_first_file()

Utils.compress_dataset()









