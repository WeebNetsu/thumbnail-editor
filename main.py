from PIL import Image, ImageDraw, ImageFont
import sys
from termcolor import colored

class ThumbnailEditor():
    def __init__(self, argv: list):
        """
        This will take in argv (usually provided by sys.argv being passed in), the argv is an list that should look something
        like this: ["--text:Hello World", "--x:500", "--y:300"]. This will clean the inputs, set & check the properties and
        get project data from thumbnails.te file.
        """
        self.argv = argv
        self.flags = ("image", "text", "fs", "font", "x", "y", "output")
        self.inputs, self.project = self.cleanInput()
        self.projects_data = self.getThumbailConfig(self.project)
        self.properties = self.fillProperties(self.inputs)

        if self.projects_data == "":
            self.giveError(f"Project '{self.project}' not found in thumbnails.te")

        # self.default_inputs, _ = self.cleanInput(self.projects_data)
        # self.default_properties = self.fillProperties(self.default_inputs)
        # print(self.default_properties)

    def cleanInput(self, args = []) -> tuple:
        """
        Cleans input flags provided by user when running the program (usually sys.argv passed into constructor), removes '--' and split args at ':'
        -- is optional in flags, but recommended!
        """
        
        inputs = [arg.replace("--", "").split(":") for arg in args]
        # print(inputs)
        project = ""

        if not args: # if no custom arguments were passed in
            inputs = [arg.replace("--", "").split(":") for arg in self.argv]
            inputs.pop(0) # remove executed python file
            project = inputs[0][0]
            inputs.pop(0) # project
            
        return (inputs, project)
    
    def giveError(self, message: str) -> None:
        """Display error message and exits program"""
        print(colored(f"Error: {message}", 'red'))
        sys.exit()

    def giveWarning(self, message: str) -> None:
        """Display warning message"""
        print(colored(f"Warning: {message}", 'yellow'))

    def fillProperties(self, inputs: list) -> dict:
        """
        Takes in list of cleaned flags (check cleanInput()) and returns a dict that has all the properties from the cleaned input and defaults
        from thumbnails.te
        """
        props = {"image": "", "text": [], "font_size": [], "font_family": [], "x": [], "y": [], "output": ""}

        # print(self.projects_data)

        for arg in inputs:
            if arg[0] in self.flags:
                if arg[0] == "image":
                    props["image"] = arg[1]
                    
                if arg[0] == "fs":
                    props["font_size"].append(arg[1])

                if arg[0] == "font":
                    props["font_family"].append(arg[1])
                    
                if arg[0] == "text":
                    props["text"].append(arg[1])
                    
                if arg[0] == "x":
                    props["x"].append(arg[1])

                if arg[0] == "y":
                    props["y"].append(arg[1])
                
                if arg[0] == "no-default":
                    props["load_defaults"] = False
                
                if arg[0] == "output":
                    props["output"] = arg[1]

            else:
                self.giveError(f"Flag '{arg[0]}' does not exist")

        if props["x"] or props["y"]: # if they specify x or y positions
            if len(props["text"]) != len(props["x"]) or len(props["text"]) != len(props["y"]):
                self.giveError("--text, --x and --y should be used the same amount of times")

        # if not((props["x"] or props["y"]) and props["load_defaults"]) : # if they dont specify x or y positions and said not to load the defaults
        #     if len(props["text"]) != len(props["x"]) or len(props["text"]) != len(props["y"]):
        #         self.giveError("--text, --x and --y should be used the same amount of times or load defaults file")

        # if not props["load_defaults"]:
        #     self.giveWarning("Not loading defaults from file")
        #     return props

        return props        

    def getThumbailConfig(self, project: str) -> str:
        """
        This will get the config for the specific project entered
        """
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

    def drawText(self, draw, text, x=0, y=0, color=(0,0,0), font="open_sans/OpenSans-Regular", font_size=30, border_width=0, border_color=(255, 255, 255)) -> None:
        """This draws the text to the image, draw and text are required inputs, the rest are optional"""
        drawFont = ImageFont.truetype(f"fonts/{font}.ttf", int(font_size))

        draw.text(
            (int(x), int(y)),  # Coordinates
            text,  # Text
            color,  # Color
            font=drawFont,
            stroke_width=border_width, 
            stroke_fill=border_color
        )

    def createThumbnail(self) -> None:
        """This will create the thumbnail"""
        try:
            imgFace = Image.open(f"base-thumbnails/{self.properties['image']}")
        except FileNotFoundError:
            self.giveError(f"Image {self.properties['image']} could not be found inside the 'base-thumbnails' directory.")

        draw = ImageDraw.Draw(imgFace)
        count = 0
        for text, x_pos, y_pos in zip(self.properties["text"], self.properties["x"], self.properties["y"]):
            try:
                font_size = self.properties["font_size"][count]
            except IndexError:
                try:
                    font_size = self.properties["font_size"][-1]
                except IndexError:
                    font_size = 60
            
            try:
                font_family = self.properties["font_family"][count]
            except IndexError:
                try:
                    font_family = self.properties["font_family"][-1]
                except IndexError:
                    font_family = "open_sans/OpenSans-Regular"
            
            self.drawText(draw=draw, text=text, x=x_pos, y=y_pos, color=(0, 0, 0), font=font_family, font_size=font_size, border_width=2, border_color=(255, 255, 255))

            count += 1
        imgFace.show()


if __name__ == '__main__':
    # A working command:
    # python main.py --python --image:python.jpg --fs:60 --x:415 --y:405 --text:"Part 43:" --font:ubuntu/Ubuntu-Bold --text:"Lambda Functions" --x:455 --y:475 --fs:90 --font:ubuntu/Ubuntu-BoldItalic
    thumb = ThumbnailEditor(sys.argv)
    thumb.createThumbnail()