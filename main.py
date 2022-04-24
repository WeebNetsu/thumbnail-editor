from PIL import Image

from src.cli import giveError
from src.parser import args
from src.utils import createThumbnail, setThumbnailConfig, ALLOWED_EXT

if __name__ == "__main__":
    try:
        if args.image.split(".")[-1].lower() in ALLOWED_EXT:
            imgFace = Image.open(f"base-thumbnails/{args.image}")
        else:
            imgFace = setThumbnailConfig()

        if (len(args.x_pos) != len(args.y_pos)) or (len(args.x_pos) != len(args.text)):
            giveError("x, y and text does not have the same amount of arguments.")
    except TypeError:
        giveError("x position, y position and/or text was not provided")
    except FileNotFoundError:
        giveError(
            f"Image {args.image} could not be found inside the 'base-thumbnails' directory."
        )
    else:
        createThumbnail(imgFace)
