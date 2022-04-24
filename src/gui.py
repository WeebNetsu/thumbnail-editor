import json

from tkinter import *

from .utils import THUMB_CONF_FILE_PATH

# THUMB_CONF_FILE_PATH -> from root, we need to path to it manuallu
file = open(THUMB_CONF_FILE_PATH, "r")
json_stuff = json.load(file)  # will read from file (and convert to dictionary)
file.close()
print(json_stuff)

root = Tk()
root.title("Thumbnail Editor")
# root.geometry("400x400")

foodOptions = ["Pizza", "Salad", "Pasta"]
optionSelected = StringVar()
optionSelected.set(foodOptions[0])


def buyStuff(x):
    Label(root, text=x).pack()


# the * breaks the list into multiple items
omFood = OptionMenu(root, optionSelected, *foodOptions)
omFood.pack()

btnBuy = Button(root, text="Buy Item", command=lambda: buyStuff(optionSelected.get()))
btnBuy.pack()

# root.mainloop()
