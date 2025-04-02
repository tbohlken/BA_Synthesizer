from PIL import Image, ImageDraw
import os
import random

def load_diamond_data(file_path):
    """Reads diamond coordinates from a text file and returns them as a list of tuples."""
    diamonds = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()  # Split values by spaces
            if len(parts) == 5:  # Ensure correct format
                class_id = int(parts[0])  # Convert class ID to int
                x_rel, y_rel, w_rel, h_rel = map(float, parts[1:])  # Convert coords to float
                diamonds.append((class_id, x_rel, y_rel, w_rel, h_rel))
    return diamonds

class Rivet:
    def __init__(self, symbol_folder="resources/rivet_symbols", rows=2, cols=3, spacing=10):
        self.symbol_folder = symbol_folder
        self.rows = rows
        self.cols = cols
        self.spacing = spacing

        # Get all PNG files in the symbol folder
        symbol_paths = [os.path.join(self.symbol_folder, f) for f in os.listdir(self.symbol_folder) if f.lower().endswith(".png")]
        if not symbol_paths:
            raise ValueError("No rivet symbols found in the specified folder.")

        # Load one symbol to determine size
        sample_symbol = Image.open(symbol_paths[0]).convert("RGBA")
        symbol_width, symbol_height = sample_symbol.size

        # Create the final image canvas
        canvas_width = self.cols * symbol_width + (self.cols - 1) * self.spacing
        canvas_height = self.rows * symbol_height + (self.rows - 1) * self.spacing
        self.image = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

        # Paste symbols into grid
        for row in range(self.rows):
            for col in range(self.cols):
                symbol_path = random.choice(symbol_paths)
                symbol = Image.open(symbol_path).convert("RGBA")
                x = col * (symbol_width + self.spacing)
                y = row * (symbol_height + self.spacing)
                self.image.paste(symbol, (x, y), symbol)

    def get_image(self):
        """Returns the generated rivet grid image."""
        return self.image

def visualize_first_file():
    cwd = os.getcwd()

    # File paths
    diamond_file = cwd + "/synthdata/labels/synth_drawing_0.txt"
    image_path = cwd + "/synthdata/images/synth_drawing_0.png"
    output_folder = cwd + "/visualization"
    output_path = output_folder + "/output_with_diamonds.png"

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)  # Creates folder if missing

    # Load the diamond coordinates from the file
    diamonds = load_diamond_data(diamond_file)

    # Load the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Get image dimensions
    img_width, img_height = image.size

    print(image.size)
    # Draw red bounding boxes

    class_colors = {
        0: "red",
        1: "cyan",
        2: "green",
        3: "yellow"
        # Add more class IDs and colors as needed
    }

    for class_id, x_rel, y_rel, w_rel, h_rel in diamonds:
        cx = int(x_rel * img_width) #Center x
        cy = int(y_rel * img_height) #Center y

        w = int(w_rel * img_width) #Width
        h = int(h_rel * img_height) #Height

        x = cx - 0.5*w
        y = cy - 0.5*h

        bbox = [(x, y), (x + w, y + h)]

        # Get the color based on class_id, default to black if not found
        color = class_colors.get(class_id, "black")

        draw.rectangle(bbox, outline=color, width=3)

    # Save the modified image
    image.save(output_path)
