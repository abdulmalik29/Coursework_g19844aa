from tkinter import Tk, Canvas, PhotoImage, Button, messagebox


window = Tk()
window.title("My Game")
window.geometry("600x600")
window.configure(background='white')

new_game = PhotoImage(file="newgame2.png")
resume = PhotoImage(file="resume.png")
how_to_play= PhotoImage(file="instructions.png")
leaderBoard = PhotoImage(file="leaderboard.png")

button = [None]*4

def home_buttons():
    button[0] = Button(window, image=new_game)
    button[0].place(relx=.2, rely= 0, relwidth=0.6, relheight=.1)

    button[1] = Button(window, image=resume)
    button[1].place(relx=0.2, rely= .2, relwidth=.8, relheight=.1)


    button[2] = Button(window, image=how_to_play)
    button[2].place(relx=.2, rely= .4, relwidth=0.6, relheight=.1)

    button[3] = Button(window, image=leaderBoard)
    button[3].place(relx=.2, rely= .6, relwidth=.6, relheight=.1)



home_buttons()
window.mainloop()
