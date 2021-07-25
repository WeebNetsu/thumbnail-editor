# thumbnail-editor
A thumbnail editor for influencers to speed up the creation process!

**NOTE: This software is still in development**

## For who is this?
This is for people who need to create new thumbnails from templates they have already made and just need to change the text every time.

## How does this work?
It's as basic as opening the terminal and executing the program with arguments/flags. Flags is mainly in this format: **--flag-name value1 value2**. For help you can do the following: `python main.py --help`, or read the code, it's not a lot. This is a working example you can use: `python main.py python.jpg -fs 60 90 -x 415 455 -y 405 475 --text "Part 43:" "Lambda Functions" --font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic`

A breakdown of the above:

`python main.py` - execute the program

<!-- `--python` - the project that should be used (currently you should add a basic template to your thumbnails.te file to create a new project, this will later be used for defaults) -->

`python.jpg` - the image that should be used (location: *base-thumbnails/python.jpg*)

`-fs 60` - set the font size to 60 for first text and 90 for the rest

`-x 415 455 -y 405 475` - the x & y position of the text that should be added (first string of text will be at location: 415(x) 405(y))

`--text "Part 43:" "Lambda Functions"` - the text that should be added. If you want text to span more than 1 word, then **" "** is required.

`--font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic` - the font family that should be used (can be found inside the fonts/ folder, you can add your own as long as it is in .ttf format :D), the first piece of text will be in Ubuntu-Bold and all the rest in Ubuntu-BoldItalic

## Python Requirements
- PIL
- termcolor

----------

## Plans for the future
- Have a config file for program configs and a config file for thumbnail configs.
- Have a UI for less tech-savvy people.