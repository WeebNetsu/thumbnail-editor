import re, os, json

from PIL import Image, ImageDraw, ImageFont

from cli import giveWarning, giveError
from parser import args

ALLOWED_EXT = ("jpg", "jpeg", "png")
THUMB_CONF_FILE_PATH = "conf/thumbnails.conf.json"  # from root


def saveFile(imgFace: Image, fileWarningGiven=False) -> None:
    if not re.search("[^\w\-_\. ]", args.save):
        try:
            if args.save.split(".")[-1].lower() in ALLOWED_EXT:
                imgFace.save(f"saves/{args.save}")
            else:
                if not fileWarningGiven:
                    giveWarning("Invalid file name extension. Defaulting to jpg.")
                imgFace.save(f"saves/{args.save}.jpg")
        except FileNotFoundError:
            giveWarning("No saves folder detected. Creating new folder.")
            if not os.path.exists("saves/"):
                os.makedirs("saves/")
            saveFile(imgFace, True)
    else:
        giveError("Invalid characters in file name.")


def drawText(
    draw: ImageDraw,
    text: str,
    font: str,
    font_size: int,
    x: int,
    y: int,
    text_color: tuple,
    border_width: int,
    border_color: tuple,
) -> None:
    """This draws the text to the image, draw and text are required inputs, the rest are optional"""
    drawFont = ImageFont.truetype(f"fonts/{font}.ttf", int(font_size))

    draw.text(
        (int(x), int(y)),  # Coordinates
        text,  # Text
        text_color,  # Color
        font=drawFont,
        stroke_width=border_width,
        stroke_fill=border_color,
    )


def setThumbnailConfig() -> Image:
    """This will set the all the arguments if a project was chosen; AKA, fill in the blanks"""
    try:
        confData = json.load(open(f"../{THUMB_CONF_FILE_PATH}", "r"))[args.image]
    except KeyError:
        giveError(
            f"Could not find project '{args.image}'. If this was supposed to be an image, make sure the extension is one of the following: {ALLOWED_EXT}"
        )
    else:
        if args.save == "default":
            args.save = confData["output"]

        if not args.text:
            args.text = []

        if not args.x_pos:
            args.x_pos = []

        if not args.y_pos:
            args.y_pos = []

        if not args.font_size:
            args.font_size = []

        if not args.font:
            args.font = []

        if not args.text_color:
            args.text_color = []

        if not args.border_width:
            args.border_width = []

        if not args.border_color:
            args.border_color = []

        try:
            longer = (
                len(args.text)
                if len(args.text) > len(confData["text"])
                else len(confData["text"])
            )
            for index in range(longer):
                try:
                    conf = confData["text"][index]
                except IndexError:
                    conf = confData["text"][-1]

                try:
                    args.text[index]
                except IndexError:
                    args.text.append(conf["text"])

                try:
                    args.x_pos[index] = (
                        args.x_pos[index] if args.x_pos[index] > 0 else conf["x"]
                    )
                except IndexError:
                    args.x_pos.append(conf["x"])

                try:
                    args.y_pos[index] = (
                        args.y_pos[index] if args.y_pos[index] > 0 else conf["y"]
                    )
                except IndexError:
                    args.y_pos.append(conf["y"])

                try:
                    args.font_size[index] = (
                        args.font_size[index]
                        if args.font_size[index] > 0
                        else conf["font_size"]
                    )
                except IndexError:
                    args.font_size.append(conf["font_size"])

                try:
                    args.font[index]
                except IndexError:
                    args.font.append(conf["font"])

                try:
                    args.text_color[index]
                except IndexError:
                    args.text_color.append(conf["color"])

                try:
                    args.border_width[index]
                except IndexError:
                    args.border_width.append(conf["border_width"])

                try:
                    args.border_color[index]
                except IndexError:
                    args.border_color.append(conf["border_color"])
        except KeyError:
            giveError(
                "Uneven amounts of x, y, and/or text provided in defaults or as arguments."
            )

    return Image.open(f"base-thumbnails/{confData['image']}")


def createThumbnail(imgFace: Image) -> None:
    """This will create the thumbnail"""
    if args.quiet:
        print("Not showing warnings")

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
            if font_family == "default":
                raise TypeError
        except IndexError:
            font_family = args.font[-1]
        except TypeError:
            font_family = "open_sans/OpenSans-Regular"

        try:
            text_color = tuple(args.text_color[count])
            if text_color == tuple("default"):
                raise TypeError
        except IndexError:
            text_color = tuple(args.text_color[-1])
        except TypeError:
            text_color = (0, 0, 0)

        if not args.no_border:
            try:
                border_width = args.border_width[count]
                if border_width == "default":
                    raise TypeError
            except IndexError:
                border_width = args.border_width[-1]
            except TypeError:
                border_width = 2
        else:
            border_width = 0

        try:
            border_color = tuple(args.border_color[count])
            if border_color == tuple("default"):
                raise TypeError
        except IndexError:
            border_color = tuple(args.border_color[-1])
        except TypeError:
            border_color = (255, 255, 255)

        drawText(
            draw=draw,
            text=text,
            x=x_pos,
            y=y_pos,
            text_color=text_color,
            font=font_family,
            font_size=font_size,
            border_width=border_width,
            border_color=border_color,
        )

        count += 1

    if args.save:
        saveFile(imgFace)

    if not args.no_preview:
        imgFace.show()
    else:
        giveWarning("Not showing preview.")
