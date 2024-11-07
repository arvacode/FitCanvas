# FitCanvas
Resize Images and Place on Canvas

[@arvacode](https://instagram.com/arvacode)

https://hephium.com

## Features

* Resizes images to fit within a canvas while maintaining aspect ratio.
* Adds padding (border) around images.
* Centers images on a canvas with a specified background color.
* Supports batch processing of images in a directory.
* Allows specifying the output image format.
* Retains or changes the image format based on configuration.

## Requirements

* Python 3.x
* Pillow library for image processing.

## Installation

* Clone the repository or download the script file.
* Install the required Python library: `pip install Pillow`

## Customization
* The parameters of the script can be customized by editing the `FitCanvas.py` file with the following parameters:
```
# Width of the output canvas
OUTPUT_WIDTH = 1080

# Height of the output canvas
OUTPUT_HEIGHT = 1080

# Padding around the image
PADDING = 60

# Background color of the canvas
BACKGROUND_COLOR = 'white'

# Output image format (e.g., 'JPEG', 'PNG', or None to retain original)
OUTPUT_FORMAT = None
```

## Usage

### Mac

* Open Terminal
  * Navigate to Applications > Utilities > Terminal.
* Navigate to the Desired Output Directory:
  * `cd /path/to/your/desired/output/directory` *Replace /path/to/your/desired/output/directory with the actual path where you want the output images to be saved.*
* Execute Script
  * `python FitCanvas.py /path/to/image_or_folder` *Replace /path/to/image_or_folder with the path to an image file or a directory containing images.*
* Output Images
  * Processed images will be saved in a subdirectory named `fitcanvas-output` within your current working directory.

#### Example
`cd ~/Desktop`

`python FitCanvas.py ~/Pictures/ImageFolder`

#### Basic Mac Instructions
* Open Terminal.
* Type `cd Desktop` and press enter.
* Type `python ` and drag the `FitCanvas.py` file into terminal. Locate an image or folder of images from Finder and drag it into terminal. Press Enter.
* Output images will be saved in the `fitcanvas-output` folder on your Desktop.

### Windows

* Open Command Prompt:
  * Press Win + R, type cmd, and press Enter.
* Navigate to the Desired Output Directory:
  * `cd C:\path\to\your\desired\output\directory` *Replace C:\path\to\your\desired\output\directory with the actual path where you want the output images to be saved.*
* Execute the Script:
  * `python FitCanvas.py C:\path\to\image_or_folder` *Replace C:\path\to\image_or_folder with the path to a single image file or a directory containing multiple images.*
* Locate the Output Images:
  * Processed images will be saved in a subdirectory named `fitcanvas-output` within your current working directory.

#### Example
`cd C:\Users\YourName\Desktop`

`python FitCanvas.py C:\Users\YourName\Pictures\ImageFolder`