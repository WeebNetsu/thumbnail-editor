# thumbnail-editor
A thumbnail editor for influencers to speed up the creation process!

**NOTE: This software is still in development**

## For who is this?
This is for people who need to create new thumbnails from templates they have already made and just need to change the text every time.

## How does this work?
It's as basic as opening the terminal and executing the program with arguments/flags. Flags (except for the project) is in this format: **--flag-name:flag-value**. This is a working example you can use: `python main.py --python --image:python.jpg --fs:60 --x:415 --y:405 --text:"Part 43:" --font:ubuntu/Ubuntu-Bold --text:"Lambda Functions" --x:455 --y:475 --fs:90 --font:ubuntu/Ubuntu-BoldItalic`

A breakdown of the above:

`python main.py` - execute the program

`--python` - the project that should be used (currently you should add a basic template to your thumbnails.te file to create a new project, this will later be used for defaults)

`--image:python.jpg` - the image that should be used (location: *base-thumbnails/python.jpg*)

`--fs:60` - set the font size to 60

`--x:415 --y:405` - the x & y position of the text that should be added

`--text:"Part 43:"` - the text that should be added. If you want text to span more than 1 word, then **" "** is required.

`--font:ubuntu/Ubuntu-Bold` - the font family that should be used (can be found inside the fonts/ folder, you can add your own as long as it is in .ttf format :D)

`--text:"Lambda Functions" --x:455 --y:475 --fs:90 --font:ubuntu/Ubuntu-BoldItalic` - same as above, but for 2nd line of text
The "--" for each flag is optional, but recommended.

## Python Requirements
- PIL
- termcolor

## Plans for the future
- Have a config file for program configs and a config file for thumbnail configs.
- Have a UI for less tech-savvy people.
- Add the ability to add line-breaks in text without needing to create new text
- Better README