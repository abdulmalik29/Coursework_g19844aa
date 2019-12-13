from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Title")
root.geometry('600x600')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = new_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo

image = Image.open('blocks100.png')
new_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Button(root, image = photo)
label.bind('<Configure>', resize_image)
label.place(relheight = .2, relwidth =.2)

root.mainloop()
