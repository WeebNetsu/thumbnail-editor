import argparse

"""
RULES:
Below are working examples:
python main.py python.jpg -fs 60 90 -x 415 455 -y 405 475 --text "Part 43:" "Lambda Functions" --font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic
python main.py tkinter.jpg -fs 60 90 -x 80 150 -y 455 525 --text "Lesson 1:" "Creating our first Window" --font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic
python main.py cpp.jpg -fs 60 140 -x 70 150 -y 350 450 --text "Lesson 2:" "Hello World" --font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic -tc 255 255 255 -bc 0 0 0 -bc 99 154 210 -bw 3
python main.py love2d.jpg -fs 60 140 -x 950 120 -y 30 450 --text "Lesson 2" "Config File" --font ubuntu/Ubuntu-BoldItalic ubuntu/Ubuntu-BoldItalic -tc 0 0 0 -bc 255 255 255 -bc 255 255 255 -bw 3

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

You can also use a project! Just open thumbnails.conf.json and modify the content! You can read README.md for more information!
"""

parser = argparse.ArgumentParser()  # define the parser
parser.add_argument(
    "image",
    help="The image that should be modified OR the project name.",
    type=str,
    metavar="",
)
parser.add_argument(
    "--save",
    "-s",
    help="The output (save) location of the image.",
    type=str,
    metavar="",
)

# nargs -> allows us to take in multiple values with the same flag eg. -t "hello world" "I am cool" -> ["hello world", "I am cool"]
parser.add_argument(
    "--text",
    "-t",
    help="The text that should be added to the image.",
    type=str,
    metavar="",
    nargs="+",
)
parser.add_argument(
    "--font-size",
    "-fs",
    help="Size the font should be.",
    type=int,
    metavar="",
    nargs="+",
)
parser.add_argument(
    "--font",
    "-f",
    help="The font that should be used (font-family)",
    type=str,
    metavar="",
    nargs="+",
)
parser.add_argument(
    "--x-pos",
    "-x",
    help="The x position the text should be at on the image.",
    type=int,
    metavar="",
    default=0,
    nargs="+",
)
parser.add_argument(
    "--y-pos",
    "-y",
    help="The y position the text should be at on the image.",
    type=int,
    metavar="",
    default=0,
    nargs="+",
)
parser.add_argument(
    "--text-color",
    "-tc",
    help="The color of the text in RGB format. eg. -tc 0 100 255",
    type=int,
    metavar="",
    nargs="+",
    action="append",
)
parser.add_argument(
    "--border-color",
    "-bc",
    help="The color of the border in Tuple-RGB format. eg. -bc 0 100 255",
    type=int,
    metavar="",
    nargs="+",
    action="append",
)
parser.add_argument(
    "--border-width",
    "-bw",
    help="The width (size) of text border",
    type=int,
    metavar="",
    nargs="+",
)

parser.add_argument(
    "--no-border", help="Wether a border should be added on text.", action="store_true"
)
parser.add_argument(
    "--no-preview", help="Do not show a preview of the image.", action="store_true"
)
parser.add_argument("--quiet", help="Ignore all warnings.", action="store_true")

args = parser.parse_args()
