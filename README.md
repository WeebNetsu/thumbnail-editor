# Thumbnail Editor

A thumbnail editor for influencers to speed up the creation process!

If you are an educational YouTuber then you probably create thumbnails that looks the same, but have different text on it. This software here is designed to make the process of opening a project in GIMP/Photoshop, then editing the text, setting the borders etc. and finally saving it as a jpg or png, a lot shorter! You just design a template, create a project, and boom! You can easily generate yourself a thumbnail by quickly passing in some arguments to the terminal!

## Topics

-   [Who is this for](#who-is-this-for)
-   [How does it work?](#how-does-it-work)
-   [Using a project](#using-a-project)
-   [Python Requirements](#python-requirements)
-   [Arguments](#arguments)

<h2 id="who-is-this-for">Who is this for?</h2>

This is for people who need to create new thumbnails from templates they have already made and just need to change the text every time.

<h2 id="how-does-it-work">How does it work?</h2>

It's as basic as opening the terminal and executing the program with arguments/flags. Flags is mainly in this format: **--flag-name value1 value2**. For help you can do the following: `python main.py --help`, or read the code, it's not a lot. This is a working example you can use: `python main.py python.jpg -fs 60 90 -x 415 455 -y 405 475 --text "Part 43:" "Lambda Functions" --font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic`

A breakdown of the above:

`python main.py` - execute the program

<!-- `--python` - the project that should be used (currently you should add a basic template to your thumbnails.te file to create a new project, this will later be used for defaults) -->

`python.jpg` - the image that should be used (location: _base-thumbnails/python.jpg_)

`-fs 60` - set the font size to 60 for first text and 90 for the rest

`-x 415 455 -y 405 475` - the x & y position of the text that should be added (first string of text will be at location: 415(x) 405(y))

`--text "Part 43:" "Lambda Functions"` - the text that should be added. If you want text to span more than 1 word, then **" "** is required.

`--font ubuntu/Ubuntu-Bold ubuntu/Ubuntu-BoldItalic` - the font family that should be used (can be found inside the fonts/ folder, you can add your own as long as it is in .ttf format :D), the first piece of text will be in Ubuntu-Bold and all the rest in Ubuntu-BoldItalic

<h2 id="using-a-project">Using a project</h2>
You'll notice a file called `thumbnails.conf.json`, this is where you can specify defaults for your thumbnails. Here is the breakdown:

```json
{
    "love2d": { // project name
        "image": "love2d.jpg", // image to use
        "output": "love2d thumbnail.jpg", // output name (used on save)
        "text": [ // all text to be added to image
            {
                "text": "Lesson 2", // text itself
                "x": 950, // x position
                "y": 30, // y position
                "font_size": 60, // font size
                "font": "ubuntu/Ubuntu-BoldItalic", // font
                "color": [0, 0, 0], // color (in RGB)
                "border_color": [255, 255, 255], // border color (in RGB)
                "border_width": 3 // border width
            },
            ...
        ],
        "save_path": "default" // save path (NOT IMPLEMENTED)
    }
}
```

An example of using a project looks like this: `python main.py love2d -fs 0 60 --font default ubuntu/Ubuntu-BoldItalic --save default`

Let me explain:

`python main.py love2d` - notice that love2d does not have a **.jpg, .jpeg** or **.png** extension, this is to specify that we want to use a project from inside the thumbnails.conf.json file.

`-fs 0 60` - this will use the default font size specified in the in the love2d project for the first piece of text, and use 60px for the second

`--font default ubuntu/Ubuntu-BoldItalic` - the first text will use the default (**NOT specified inside the project**, thus also allowing you to use default even when you're not using a project), and the second will use ubuntu font

`--save default` - this will save the file with the default "output" name given to the project

The nice thing about using a project is that you can now type less and just use a project to copy/paste the code for you that you aren't changing.

<h2 id="python-requirements">Python Requirements</h2>

-   PIL
-   termcolor

---

<h2 id="arguments">Arguments</h2>

### _image (required):_

**USAGE:** imagename.jpg _or_ "image name.jpg"

**DESCRIPTION:** This is the name of the image you want to modify.

**DEFAULT:** N/A

**RULES:** This has to be the first argument to be passed in.

**EXAMPLE:** `python main.py myimage.jpg`

### _--text (required):_

**USAGE:** --text _or_ -t

**DESCRIPTION:** The text that should be added to your image.

**DEFAULT:** N/A

**RULES:** No spaces allowed if text is not wrapped in double quotes.

**EXAMPLE:** `python main.py myimage.jpg --text "My first text" mySeconText`

### _--x-pos (required):_

**USAGE:** --x-pos _or_ -x

**DESCRIPTION:** The x (horizontal) position of your text.

**DEFAULT:** N/A

**RULES:** There should be the same amount of --x-pos arguments as there are --y-pos arguments and --text arguments.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -x 200 250`

### _--y-pos (required):_

**USAGE:** --y-pos _or_ -y

**DESCRIPTION:** The y (vertical) position of your text.

**DEFAULT:** N/A

**RULES:** There should be the same amount of --y-pos arguments as there are --x-pos arguments and --text arguments.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -y 200 250`

### _--save:_

**USAGE:** --save _or_ -s

**DESCRIPTION:** This allows you to save your file via the terminal.

**DEFAULT:** N/A

**RULES:** Input should not contain strings that are not allowed in file names. (ie "/"). Extension should be .jpg or .png.
**EXAMPLE:** `python main.py myimage.jpg --save "my image.png"`

### _--font:_

**USAGE:** --font _or_ -f

**DESCRIPTION:** The font you want your text to be displayed in. Fonts can be found inside the `fonts/` folder.

**DEFAULT:** open_sans/OpenSans-Regular

**RULES:** Only .ttf fonts are allowed.
**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" --font ubuntu/Ubuntu-BoldItalic`

### _--font-size:_

**USAGE:** --font-size _or_ -fs

**DESCRIPTION:** The size of your text font.

**DEFAULT:** 60

**RULES:** Only _integers_ allowed.

**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -fs 60 20`

### _--text-color:_

**USAGE:** --text-color _or_ -tc

**DESCRIPTION:** The color of your text.

**DEFAULT:** Black

**RULES:** Has to be in RGB values.

**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -tc 255 255 255 -tc 0 0 0`

### _--border-color:_

**USAGE:** --border-color _or_ -bc

**DESCRIPTION:** The color of the border around your text.

**DEFAULT:** White

**RULES:** Has to be in RGB values.

**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -bc 255 255 255 -bc 0 0 0`

### _--border-width:_

**USAGE:** --border-width _or_ -bw

**DESCRIPTION:** The width of your text border. Set it to 0 for no border, or use --no-border flag.

**DEFAULT:** 2

**RULES:** Only _integers_ allowed.

**EXAMPLE:** `python main.py myimage.jpg -t "Hello Tim" "Part 1" -bw 5 10`

### _--no-border:_

**USAGE:** --no-border

**DESCRIPTION:** Removes border from text.

**DEFAULT:** N/A

**RULES:** N/A

**EXAMPLE:** `python main.py myimage.jpg --text "Hello Tim" --no-border`

### _--no-preview:_

**USAGE:** --no-preview

**DESCRIPTION:** Do not show preview of image.

**DEFAULT:** N/A

**RULES:** N/A

**EXAMPLE:** `python main.py myimage.jpg --text "Hello Tim" --no-preview`

### _--quiet:_

**USAGE:** --quiet

**DESCRIPTION:** Do not show warnings.

**DEFAULT:** N/A

**RULES:** N/A

**EXAMPLE:** `python main.py myimage.jpg -t "hello" -s "s" --quiet`
