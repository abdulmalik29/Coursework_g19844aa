from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
from PIL import Image


window = Tk()
window.title("My Game")
window.geometry("700x735")
window.configure(background='white')


def create_blocks():

    canvas = Canvas(window, bg= "#ff9900")
    canvas.pack
    canvas.place(relwidth= 1,relheight=1, relx= 0, rely=0)

    blockImage = PhotoImage(file="blocks103.png")
    block = [None]*36
    y_cord = 100
    x_cord = 100
    n = 1

    while x_cord < 700 :
        while y_cord < 630 :
            block[-1 + n] = canvas.create_image(x_cord, y_cord, image = blockImage)
            y_cord += 105
            n += 1
        x_cord += 100
        y_cord = 100
    window.mainloop()


create_blocks()
