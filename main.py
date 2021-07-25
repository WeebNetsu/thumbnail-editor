import argparse

from PIL import Image, ImageDraw, ImageFont
from termcolor import colored

"""
RULES:
Below is a working example:
python main.py python.jpg -fs 60 90 -x 415 455 -y 405 475 --text "Part 43:" "Lambda Functions" --font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic

Explaination:
python -> the python program
main.py -> the file
python.jpg -> image that should be modified
-fs 60 90 -> font size 60 and 90 should be used
-x 415 455 -> x positions 415 and 455 should be used
-y 405 475 -> y positions 405 and 475 should be used
--text "Part 43:" "Lambda Functions" -> The text that should be added to the image
--font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic -> fonts that should be used

1. There has to be ONE image selected and it has to be the FIRST parameter
2. There should be an equal amount of x, y and text arguments
3. Text seperated by spaces should be in ""

Complex example:
python main.py python.jpg -fs 60 90 -x 415 455 -y 405 475 --text "Part 43:" "Lambda Functions" --font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic -tc 255 255 255 -tc 0 0 0 -bw 1 2 -bc 255 0 0 -bc 0 255 0
"""

# TODO: no-border, output, project, config file

parser = argparse.ArgumentParser() # define the parser
parser.add_argument("image", help="The image that should be modified.", type=str, metavar='')
# nargs -> allows us to take in multiple values with the same flag eg. -t "hello world" "I am cool" -> ["hello world", "I am cool"]
parser.add_argument("--text", "-t", help="The text that should be added to the image.", type=str, metavar='', nargs="+")
parser.add_argument("--font-size", "-fs", help="Size the font should be.", type=int, metavar='', nargs="+")
parser.add_argument("--font", "-f", help="The font that should be used (font-family)", type=str, metavar='', nargs="+")
parser.add_argument("--x-pos", "-x", help="The x position the text should be at on the image.", type=int, metavar='', default=0, nargs="+")
parser.add_argument("--y-pos", "-y", help="The y position the text should be at on the image.", type=int, metavar='', default=0, nargs="+")
parser.add_argument("--text-color", "-tc", help="The color of the text in RGB format. eg. -tc 0 100 255", type=int, metavar='', nargs="+", action="append")
parser.add_argument("--border-color", "-bc", help="The color of the border in Tuple-RGB format. eg. -bc 0 100 255", type=int, metavar='', nargs="+", action="append")
parser.add_argument("--border-width", "-bw", help="The width (size) of text border", type=int, metavar='', nargs="+")
parser.add_argument("--no-border", help="Wether a border should be added round text.", action="store_true")
parser.add_argument("--output", "-o", help="The output location of the image.", type=str, metavar='')
args = parser.parse_args()

print(args)

def giveError(message: str) -> None:
    """Display error message and exits program"""
    print(colored(f"Error: {message}", 'red'))
    exit()

def giveWarning(message: str) -> None:
    """Display warning message"""
    print(colored(f"Warning: {message}", 'yellow'))

def drawText(draw, text, font, font_size, x, y, text_color, border_width, border_color) -> None:
    """This draws the text to the image, draw and text are required inputs, the rest are optional"""
    drawFont = ImageFont.truetype(f"fonts/{font}.ttf", int(font_size))

    draw.text(
        (int(x), int(y)),  # Coordinates
        text,  # Text
        text_color,  # Color
        font=drawFont,
        stroke_width=border_width, 
        stroke_fill=border_color
    )
    
def createThumbnail() -> None:
    """This will create the thumbnail"""
    try:
        imgFace = Image.open(f"base-thumbnails/{args.image}")
    except FileNotFoundError:
        giveError(f"Image {args.image} could not be found inside the 'base-thumbnails' directory.")

    draw = ImageDraw.Draw(imgFace)
    count = 0
    for text, x_pos, y_pos in zip(args.text, args.x_pos, args.y_pos):
        try:
            font_size = args.font_size[count]
        except IndexError:
            font_size = args.font_size[-1]
        except TypeError:
            font_size = 60
        
        try:
            font_family = args.font[count]
        except IndexError:
            font_family = args.font[-1]
        except TypeError:
            font_family = "open_sans/OpenSans-Regular"
        
        try:
            text_color = tuple(args.text_color[count])
        except IndexError:
            text_color = tuple(args.text_color[-1])
        except TypeError:
            text_color = (0, 0, 0)
            
        try:
            border_width = args.border_width[count]
        except IndexError:
            border_width = args.border_width[-1]
        except TypeError:
            border_width = 2
        
        try:
            border_color = tuple(args.border_color[count])
        except IndexError:
            border_color = tuple(args.border_color[-1])
        except TypeError:
            border_color = (255, 255, 255)
        
        drawText(draw=draw, text=text, x=x_pos, y=y_pos, text_color=text_color, font=font_family, font_size=font_size, border_width=border_width, border_color=border_color)

        count += 1
    imgFace.show()

if __name__ == '__main__':
    if (len(args.x_pos) != len(args.y_pos)) or (len(args.x_pos) != len(args.text)):
        giveWarning("x, y and text does not have the same amount of arguments.")
        
    createThumbnail()

# python main.py --python --image:python.jpg --fs:60 --x:415 --y:405 --text:"Part 43:" --font:ubuntu/Ubuntu-Bold --text:"Lambda Functions" --x:455 --y:475 --fs:90 --font:ubuntu/Ubuntu-BoldItalic

"""
def getThumbailConfig(self, project: str) -> str:
        # This will get the config for the specific project entered
        with open("thumbnails.te", "r") as tFile:
            thumbnails = tFile.readlines()

            for line in thumbnails:
                texts = ""
                if not (line.startswith("#") or line == "\n"):
                    try:
                        texts = line[:line.index("#")].split(" ")
                    except ValueError: # if # was not found in string
                        texts = line.split(" ")
                    
                    # print(texts[0])
                    if texts[0].strip() == project.strip():
                        texts.pop(0)
                        return texts
        
        return ""
"""