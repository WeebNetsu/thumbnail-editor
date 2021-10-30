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

`python.jpg` - the image that should be used (location: _base-thumbnails/python.jpg_)

`-fs 60` - set the font size to 60 for first text and 90 for the rest

`-x 415 455 -y 405 475` - the x & y position of the text that should be added (first string of text will be at location: 415(x) 405(y))

`--text "Part 43:" "Lambda Functions"` - the text that should be added. If you want text to span more than 1 word, then **" "** is required.

`--font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic` - the font family that should be used (can be found inside the fonts/ folder, you can add your own as long as it is in .ttf format :D), the first piece of text will be in Ubuntu-Bold and all the rest in Ubuntu-BoldItalic

## Python Requirements

- PIL
- termcolor

---

## Arguments:

image (required)
: **USAGE:** imagename.jpg _or_ "image name.jpg"
**DESCRIPTION:** This is the name of the image you want to modify.
**DEFAULT:** N/A
**RULES:** This has to be the first argument to be passed in.
**EXAMPLE:** `python main.py myimage.jpg`

--save
: **USAGE:** --save _or_ -s
**DESCRIPTION:** This allows you to save your file via the terminal.
**DEFAULT:** N/A
**RULES:** Input should not contain strings that are not allowed in file names. (ie "/"). Extension should be .jpg or .png.
**EXAMPLE:** `python main.py myimage.jpg --save "my image.png"`

--text (required)
: **USAGE:** --text _or_ -t
**DESCRIPTION:** The text that should be added to your image.
**DEFAULT:** N/A
**RULES:** No spaces allowed if text is not wrapped in double quotes.
**EXAMPLE:** `python main.py myimage.jpg --text "My first text" mySeconText`

--x-pos (required)
: **USAGE:** --x-pos _or_ -x
**DESCRIPTION:** The x (horizontal) position of your text.
**DEFAULT:** N/A
**RULES:** There should be the same amount of --x-pos arguments as there are --y-pos arguments and --text arguments.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -x 200 250`

--y-pos (required)
: **USAGE:** --y-pos _or_ -y
**DESCRIPTION:** The y (vertical) position of your text.
**DEFAULT:** N/A
**RULES:** There should be the same amount of --y-pos arguments as there are --x-pos arguments and --text arguments.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -y 200 250`

--font
: **USAGE:** --font _or_ -f
**DESCRIPTION:** The font you want your text to be displayed in. Fonts can be found inside the `fonts/` folder.
**DEFAULT:** open_sans/OpenSans-Regular
**RULES:** Only .ttf fonts are allowed.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" --font ubuntu/Ubuntu-BoldItalic`

--font-size
: **USAGE:** --font-size _or_ -fs
**DESCRIPTION:** The size of your text font.
**DEFAULT:** 60
**RULES:** Only *integers* allowed.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -fs 60 20`


--text-color
: **USAGE:** --text-color _or_ -tc
**DESCRIPTION:** The color of your text.
**DEFAULT:** Black
**RULES:** Has to be in RGB values.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -tc 255 255 255 -tc 0 0 0`

--border-color
: **USAGE:** --border-color _or_ -bc
**DESCRIPTION:** The color of the border around your text.
**DEFAULT:** White
**RULES:** Has to be in RGB values.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -bc 255 255 255 -bc 0 0 0`

--border-width
: **USAGE:** --border-width _or_ -bw
**DESCRIPTION:** The width of your text border. Set it to 0 for no border, or use --no-border flag.
**DEFAULT:** 2
**RULES:** Only *integers* allowed.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -bw 5 10`

--no-border
: **USAGE:** --no-border
**DESCRIPTION:** Removes border from text.
**DEFAULT:** N/A
**RULES:** N/A
**EXAMPLE:** `python main.py myimage.jpg --text "Hello Tim" --no-border`

--no-preview
: **USAGE:** --no-preview
**DESCRIPTION:** Do not show preview of image.
**DEFAULT:** N/A
**RULES:** N/A
**EXAMPLE:** `python main.py myimage.jpg --text "Hello Tim" --no-preview`

--quiet
: **USAGE:** --quiet
**DESCRIPTION:** Do not show warnings.
**DEFAULT:** N/A
**RULES:** N/A
**EXAMPLE:** `python main.py myimage.jpg -t "hello" -s "s" --quiet`
