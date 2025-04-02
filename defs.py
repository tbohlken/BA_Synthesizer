class Defs:

    ###Test

    #########Global parameters########
    #General settings
    synth_count = 1
    width = 4963 #Drawing width
    height = 3509 #Drawing height
    classes = ["FlagNoteSymbol", "PartNumber", "Rivet", "SectionText", "Cross"]
    target_width = 2000



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
    diamond_standard_width = 120
    min_diamond_scale_factor, max_diamond_scale_factor = 0.7, 1.5
    diamond_number_font_size = 26
    min_diamond_count, max_diamond_count = 30, 40  # Min and max amount of diamonds

    #Rivet groups
    min_rg_scale, max_rg_scale = 0.09, 0.18
    min_rg_count, max_rg_count = 5, 12
    min_rg_rows, max_rg_rows = 1, 4
    min_rg_columns, max_rg_columns = 1, 5

    #Circle
    min_circle_count, max_circle_count = 10, 16
    min_circle_diameter, max_circle_diameter = 50, 150
    circle_number_font_size = 42

    #Rectangle
    min_rectangle_count, max_rectangle_count = 10, 20  # Min and max amount of rectangles
    rect_min_width, rect_min_height = 200, 200
    rect_max_width, rect_max_height = 900, 900

    #Arrow
    min_arrow_count, max_arrow_count = 10, 15  # Min and max amount of arrows
    min_arrow_length, max_arrow_length = 400, 1000

    #Cross
    min_cross_count, max_cross_count = 10, 12
    min_cross_scale_factor, max_cross_scale_factor = 0.7, 1.4

