from tkinter import Tk, Canvas, PhotoImage, Button, messagebox, ttk
from PIL import Image, ImageTk

button = [None]*4




def home_buttons():
    new_game = PhotoImage(file="newgame1.png")
    resume = PhotoImage(file="resume1.png")
    how_to_play= PhotoImage(file="instructions1.png")
    leaderBoard = PhotoImage(file="leaderboard1.png")

    button[0] = Button(window, image=new_game, command = lambda: start_game())
    button[0].place(relx=.3, rely= .1, relwidth=0.42, relheight=.18)

    button[1] = Button(window, image=resume)
    button[1].place(relx=0.3, rely= .3, relwidth=.42, relheight=.18)


    button[2] = Button(window, image=how_to_play)
    button[2].place(relx=.3, rely= .5, relwidth=0.42, relheight=.18)

    button[3] = Button(window, image=leaderBoard)
    button[3].place(relx=.3, rely= .7, relwidth=.42, relheight=.18)
    window.mainloop()

def start_game():
    global canvas
    canvas = Canvas(window, bg= "#ff9900")
    canvas.pack
    canvas.place(relwidth= 1,relheight=1, relx= 0, rely=0)
home_buttons()
