from tkinter import Tk, Canvas, PhotoImage, Button, messagebox


window = Tk()
window.title("My Game")
window.geometry("700x735")
window.configure(background='white')


new_game = PhotoImage(file="newgame2.png")
resume = PhotoImage(file="resume.png")
how_to_play= PhotoImage(file="instructions.png")
leaderBoard = PhotoImage(file="leaderboard.png")

def creat_character():#############################################



button = [None]*4

def home_buttons():
    button[0] = Button(window, image=new_game, command = lambda: create_blocks())
    button[0].place(relx=.2, rely= 0, relwidth=0.6, relheight=.3)

    button[1] = Button(window, image=resume)
    button[1].place(relx=0.2, rely= .4, relwidth=.6, relheight=.2)


    button[2] = Button(window, image=how_to_play)
    button[2].place(relx=.2, rely= .6, relwidth=0.6, relheight=.2)

    button[3] = Button(window, image=leaderBoard)
    button[3].place(relx=.2, rely= .8, relwidth=.6, relheight=.2)
    window.mainloop()


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


home_buttons()
