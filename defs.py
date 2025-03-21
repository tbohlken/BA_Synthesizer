class Defs:

    ###Test

    #########Global parameters########
    #General settings
    synth_count = 1
    width = 4963 #Drawing width
    height = 3509 #Drawing height
    classes = ["Diamond"]
    target_width = 2000

    #Object counts
    min_diamond_count, max_diamond_count = 25, 25#Min and max amount of diamonds
    min_circle_count, max_circle_count = 25, 25
    min_rectangle_count, max_rectangle_count = 30, 50 #Min and max amount of rectangles
    min_arrow_count, max_arrow_count = 10, 15 #Min and max amount of arrows

    # Directory settings
    dataset_name = "synthdata"

    ######Sample ED measurements#######
    #Box measurements
    box_width = (4840-2710)
    box_height = (3400-2830)

    #Border
    margin_left = 240
    margin_right = 120
    margin_top = 120
    margin_bottom = 120

    padding = 50 #Desired gap between inner frame of ED and synthetic objects

    #######Parameters for synthetic objects########

    # Diamond
    min_diamond_width, max_diamond_width = 80, 160
    diamond_number_font_size = 26

    #Circle
    min_circle_diameter, max_circle_diameter = 50, 200
    circle_number_font_size = 42

    #Rectangle
    rect_min_width, rect_min_height = 200, 200
    rect_max_width, rect_max_height = 900, 900

    #Arrow
    min_arrow_length, max_arrow_length = 400, 1000

