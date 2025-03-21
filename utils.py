import os, json, shutil
import random

from defs import Defs

class Utils:
    #Make the directories
    @staticmethod
    def build_directory():

        cwd = os.getcwd()
        dir_path = os.path.abspath(os.path.join(cwd, Defs.dataset_name))
        #Clear previous directory if it exists
        try:
            shutil.rmtree(dir_path)  # Deletes folder and all files/subfolders
            print(f"Folder removed: {dir_path}")
        except FileNotFoundError:
            print(f"Folder not found: {dir_path}")
        except PermissionError:
            print(f"Permission denied: {dir_path}")
        except Exception as e:
            print(f"Error deleting folder: {e}")

        os.makedirs(Defs.dataset_name, exist_ok=True)

        os.makedirs(Defs.dataset_name + "/labels", exist_ok=True)  # ✅ Creates "labels" folder if missing
        os.makedirs(Defs.dataset_name + "/images", exist_ok=True)  # ✅ Creates "labels" folder if missing

    @staticmethod
    def make_classes_file():
        for _class in Defs.classes:
            with open(Defs.dataset_name + "/classes.txt", "a") as file:  # Append mode, file is created if missing
                file.write(_class+"\n")

    @staticmethod
    def make_json():
        # Generate categories dynamically based on the list
        categories = [{"id": i, "name": name} for i, name in enumerate(Defs.classes)]
        # Define the dictionary (matching your structure)
        data = {
            "categories": categories,
            "info": {
                "year": 2025,
                "version": "1.0",
                "contributor": "Torge Bohlken"
            }
        }

        # Define the file name
        file_path = Defs.dataset_name + "/notes.json"

        # Save the JSON file
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)  # Pretty-print with indentation

    @staticmethod
    def compress_dataset():
        """
        Compresses a directory into a .zip file and saves it in the parent directory.
        :param directory: The path to the directory to be compressed.
        """
        # Get the absolute path of the directory
        cwd = os.getcwd()

        dir_path = os.path.abspath(os.path.join(cwd, Defs.dataset_name))

        # Get parent directory
        parent_dir = os.path.dirname(dir_path)

        # Name of the zip file (same as folder name)
        zip_name = "data"

        # Full path of the zip file (saved in the parent directory)
        zip_path = os.path.join(parent_dir, zip_name)

        # Create the zip archive
        shutil.make_archive(zip_path, 'zip', dir_path)


    @staticmethod
    def generate_rand_allowed_xyPos(obj_width, obj_height):
        available_width = Defs.width-Defs.margin_left-Defs.margin_right-2*Defs.padding
        available_height = Defs.height-Defs.margin_top-Defs.margin_bottom-2*Defs.padding

        min_width = available_width-Defs.box_width
        min_height= available_height-Defs.box_height

        random.seed(os.urandom(1024))

        randX = int(random.uniform(0, available_width-obj_width))
        randY = int(random.uniform(0, available_height-obj_height))


        if randX > (min_width-obj_width) and randY > (min_height-obj_height):
            return Utils.generate_rand_allowed_xyPos(obj_width, obj_height)

        return (randX+Defs.margin_left+Defs.padding, randY+Defs.margin_top+Defs.padding)





