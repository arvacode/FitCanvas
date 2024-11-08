"""
     _    ______     ___    ____ ___  ____  _____               
    / \  |  _ \ \   / / \  / ___/ _ \|  _ \| ____|              
   / _ \ | |_) \ \ / / _ \| |  | | | | | | |  _|                
  / ___ \|  _ < \ V / ___ \ |__| |_| | |_| | |___               
 /_/   \_\_| \_\ \_/_/   \_\____\___/|____/|_____|              
  _                _     _                                      
 | |__   ___ _ __ | |__ (_)_   _ _ __ ___    ___ ___  _ __ ___  
 | '_ \ / _ \ '_ \| '_ \| | | | | '_ ` _ \  / __/ _ \| '_ ` _ \ 
 | | | |  __/ |_) | | | | | |_| | | | | | || (_| (_) | | | | | |
 |_| |_|\___| .__/|_| |_|_|\__,_|_| |_| |_(_)___\___/|_| |_| |_|
            |_|                                                 

FitCanvas https://github.com/arvacode/FitCanvas
This script resizes images to fit within a specified canvas size, adds padding, and saves the processed images.

ARVACODE
https://Hephium.com

"""

from PIL import Image
import os
import sys
import glob

# [ Customization ]

# Width of the output canvas
OUTPUT_WIDTH = 1080
# Height of the output canvas
OUTPUT_HEIGHT = 1080
# Padding around the image
PADDING = 30
# Background color of the canvas
BACKGROUND_COLOR = 'white'
# Output image format (e.g., 'JPEG', 'PNG', or None to retain original)
OUTPUT_FORMAT = None


# [ Code ]

def get_image_paths(input_path):
    # List of supported image extensions
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']

    image_paths = []

    if os.path.isfile(input_path):
        if os.path.splitext(input_path)[1].lower() in extensions:
            image_paths.append(input_path)
    elif os.path.isdir(input_path):
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if os.path.splitext(file)[1].lower() in extensions:
                    image_paths.append(os.path.join(root, file))
    else:
        print("The specified path is neither a file nor a directory.")
        sys.exit(1)

    return image_paths

def process_image(image_path):
    with Image.open(image_path) as img:
        usable_width = OUTPUT_WIDTH - 2 * PADDING
        usable_height = OUTPUT_HEIGHT - 2 * PADDING
        scale_width = usable_width / img.width
        scale_height = usable_height / img.height
        scale_factor = min(scale_width, scale_height)
        new_width = int(img.width * scale_factor)
        new_height = int(img.height * scale_factor)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        canvas = Image.new('RGB', (OUTPUT_WIDTH, OUTPUT_HEIGHT), BACKGROUND_COLOR)
        x = (OUTPUT_WIDTH - new_width) // 2
        y = (OUTPUT_HEIGHT - new_height) // 2
        canvas.paste(img, (x, y))
        return canvas

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py /path/to/image_or_folder")
        sys.exit(1)

    input_path = sys.argv[1]
    output_folder = 'fitcanvas-output'

    os.makedirs(output_folder, exist_ok=True)
    image_paths = get_image_paths(input_path)

    if not image_paths:
        print("No images found in the specified path.")
        sys.exit(1)

    def save_image(p):
        output_image = process_image(p)
        base_name = os.path.splitext(os.path.basename(p))[0]
        output_ext = f".{OUTPUT_FORMAT.lower()}" if OUTPUT_FORMAT else os.path.splitext(p)[1]
        output_path = os.path.join(output_folder, f"{base_name}_canvas{output_ext}")
        save_params = {'format': OUTPUT_FORMAT} if OUTPUT_FORMAT else {}
        output_image.save(output_path, **save_params)

    list(map(save_image, image_paths))

if __name__ == "__main__":
    main()
