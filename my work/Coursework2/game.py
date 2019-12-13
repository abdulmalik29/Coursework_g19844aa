from tkinter import *
from PIL import Image, ImageTk
import random
import time


def move_character(event):
    global direction, positions, lost, X, Y, score, lose1x, lose2x, lose3x, lose4x,lose1y, lose2y, lose3y, lose4y
    # positions = []                            # to record the positions for
    if event.char == "a": #move the character to the left
        X = X - 25
        print (str(X) + " , " + str(Y))
        char_canvas.place(width = 50, height= 50, x = X, y = Y)
        char_canvas.update()

    elif event.char == "d": #move the character to the right
        X = X + 25
        print (str(X) + " , " + str(Y))
        char_canvas.place(width = 50, height= 50, x = X, y = Y)
        char_canvas.update()

    elif event.char == "w": #move the character up
        Y = Y - 25
        print (str(X) + " , " + str(Y))
        char_canvas.place(width = 50, height= 50, x = X, y = Y)
        char_canvas.update()


    elif event.char == "s": #move the character down
        Y = Y + 25
        print (str(X) + " , " + str(Y))
        char_canvas.place(width = 50, height= 50, x = X, y = Y)
        char_canvas.update()

    elif event.char == "p": #print stop
        print ("stop")

    elif event.char == "l": # to start the game
        stage_0()
        window.unbind("<p>")

    elif event.char == "k": # cheat code to increase the score
        score += 10
        txt = "score:" + str(score)
        canvas.itemconfigure(score_text, text=txt)
        canvas.update()




    if X == 25 or X == 625 or Y == 25 or Y == 625: # checs for overlapping
        print("lost")
        lose_game()


def creat_character():
    global character_image, character, char_canvas, X, Y,lose1x, lose2x, lose3x, lose4x,lose1y, lose2y, lose3y, lose4y, score_text

    X = 175 # the starting cords of the character
    Y = 175
    score_text = canvas.create_text(350,20, fill="white", font="Times 20 italic bold", text="Score: 0") # displays the score
    char_canvas = Frame(window, bg= "white")
    char_canvas.place(width = 50, height= 50, x = X, y = Y) # place the character
    char_canvas.update()



def stage_0():
    shake12(block_a3,block_b3,block_c3,block_d3,block_e3,block_f3,block_a4,block_b4,block_c4,block_d4,block_e4,block_f4)
    global score
    score+=10 # increase the score
    txt = "score:" + str(score)
    canvas.itemconfigure(score_text, text=txt) # and display it

    canvas.move(block_a3,2000,2000) # hide the blocks
    canvas.move(block_b3,2000,2000)
    canvas.move(block_c3,2000,2000)
    canvas.move(block_d3,2000,2000)
    canvas.move(block_e3,2000,2000)
    canvas.move(block_f3,2000,2000)
    canvas.move(block_a4,2000,2000)
    canvas.move(block_b4,2000,2000)
    canvas.move(block_c4,2000,2000)
    canvas.move(block_d4,2000,2000)
    canvas.move(block_e4,2000,2000)
    canvas.move(block_f4,2000,2000)
    canvas.update()
    if X == 25 or X == 625 or Y == 25 or Y == 625 or Y ==  225 or Y == 425: # checks for overlapping between the character and the lava
        print("lost")
        lose_game()

    canvas.after(1000 - time)
    canvas.move(block_a3,-2000,-2000)  # show the b;ocks
    canvas.move(block_b3,-2000,-2000)
    canvas.move(block_c3,-2000,-2000)
    canvas.move(block_d3,-2000,-2000)
    canvas.move(block_e3,-2000,-2000)
    canvas.move(block_f3,-2000,-2000)
    canvas.move(block_a4,-2000,-2000)
    canvas.move(block_b4,-2000,-2000)
    canvas.move(block_c4,-2000,-2000)
    canvas.move(block_d4,-2000,-2000)
    canvas.move(block_e4,-2000,-2000)
    canvas.move(block_f4,-2000,-2000)
    canvas.update()
    stage_1() # go to the next stage


def stage_1():
    global score
    score+=10 # increase the score and diplay it
    txt = "score:" + str(score)
    canvas.itemconfigure(score_text, text=txt)

    shake18(block_a2,block_b2,block_c2,block_d2,block_e2,block_f2,block_a4,block_b4,block_c4,block_d4,block_e4,block_f4,block_a6,block_b6,block_c6,block_d6,block_e6,block_f6)
    canvas.move(block_a2,2000,2000)
    canvas.move(block_b2,2000,2000)
    canvas.move(block_c2,2000,2000)
    canvas.move(block_d2,2000,2000)
    canvas.move(block_e2,2000,2000)
    canvas.move(block_f2,2000,2000)

    canvas.move(block_a4,2000,2000)
    canvas.move(block_b4,2000,2000)
    canvas.move(block_c4,2000,2000)
    canvas.move(block_d4,2000,2000)
    canvas.move(block_e4,2000,2000)
    canvas.move(block_f4,2000,2000)

    canvas.move(block_a6,2000,2000)
    canvas.move(block_b6,2000,2000)
    canvas.move(block_c6,2000,2000)
    canvas.move(block_d6,2000,2000)
    canvas.move(block_e6,2000,2000)
    canvas.move(block_f6,2000,2000)
    canvas.update()
    if X == 25 or X == 625 or Y == 25 or Y == 625 or Y == 125 or Y == 225 or Y == 325 or Y == 425: # checks for overlapping
        print("lost")
        lose_game()

    canvas.after(1000 - time)

    canvas.move(block_a2,-2000,-2000)
    canvas.move(block_b2,-2000,-2000)
    canvas.move(block_c2,-2000,-2000)
    canvas.move(block_d2,-2000,-2000)
    canvas.move(block_e2,-2000,-2000)
    canvas.move(block_f2,-2000,-2000)

    canvas.move(block_a4,-2000,-2000)
    canvas.move(block_b4,-2000,-2000)
    canvas.move(block_c4,-2000,-2000)
    canvas.move(block_d4,-2000,-2000)
    canvas.move(block_e4,-2000,-2000)
    canvas.move(block_f4,-2000,-2000)

    canvas.move(block_a6,-2000,-2000)
    canvas.move(block_b6,-2000,-2000)
    canvas.move(block_c6,-2000,-2000)
    canvas.move(block_d6,-2000,-2000)
    canvas.move(block_e6,-2000,-2000)
    canvas.move(block_f6,-2000,-2000)
    canvas.update()
    lose1y = 0
    lose2y = 0
    lose3y = 0
    lose4y = 0
    stage_2()


def stage_2():
    global score
    score+=10
    txt = "score:" + str(score)
    canvas.itemconfigure(score_text, text=txt)
    shake18(block_a1,block_b1,block_c1,block_d1,block_e1,block_f1,block_a3,block_b3,block_c3,block_d3,block_e3,block_f3,block_a5,block_b5,block_c5,block_d5,block_e5,block_f5)
    canvas.move(block_a1,2000,2000)
    canvas.move(block_b1,2000,2000)
    canvas.move(block_c1,2000,2000)
    canvas.move(block_d1,2000,2000)
    canvas.move(block_e1,2000,2000)
    canvas.move(block_f1,2000,2000)

    canvas.move(block_a3,2000,2000)
    canvas.move(block_b3,2000,2000)
    canvas.move(block_c3,2000,2000)
    canvas.move(block_d3,2000,2000)
    canvas.move(block_e3,2000,2000)
    canvas.move(block_f3,2000,2000)

    canvas.move(block_a5,2000,2000)
    canvas.move(block_b5,2000,2000)
    canvas.move(block_c5,2000,2000)
    canvas.move(block_d5,2000,2000)
    canvas.move(block_e5,2000,2000)
    canvas.move(block_f5,2000,2000)
    canvas.update()

    if X == 25 or X == 625 or Y == 25 or Y == 625 or Y == 225 or Y == 325 or Y == 425 or Y == 525 or Y == 125: # checks for overlapping
        print("lost")
        lose_game()

    canvas.after(1000 - time)
    canvas.move(block_a1,-2000,-2000)
    canvas.move(block_b1,-2000,-2000)
    canvas.move(block_c1,-2000,-2000)
    canvas.move(block_d1,-2000,-2000)
    canvas.move(block_e1,-2000,-2000)
    canvas.move(block_f1,-2000,-2000)

    canvas.move(block_a3,-2000,-2000)
    canvas.move(block_b3,-2000,-2000)
    canvas.move(block_c3,-2000,-2000)
    canvas.move(block_d3,-2000,-2000)
    canvas.move(block_e3,-2000,-2000)
    canvas.move(block_f3,-2000,-2000)

    canvas.move(block_a5,-2000,-2000)
    canvas.move(block_b5,-2000,-2000)
    canvas.move(block_c5,-2000,-2000)
    canvas.move(block_d5,-2000,-2000)
    canvas.move(block_e5,-2000,-2000)
    canvas.move(block_f5,-2000,-2000)
    canvas.update()
    stage_3()


def stage_3():
    global score
    score+=10
    txt = "score:" + str(score)
    canvas.itemconfigure(score_text, text=txt)

    shake18(block_a1,block_b1,block_c1,block_a2,block_b2,block_c2,block_a3,block_b3,block_c3,block_d4,block_e4,block_f4,block_d5,block_e5,block_f5,block_d6,block_e6,block_f6)
    canvas.move(block_a1,2000,2000)
    canvas.move(block_b1,2000,2000)
    canvas.move(block_c1,2000,2000)

    canvas.move(block_a2,2000,2000)
    canvas.move(block_b2,2000,2000)
    canvas.move(block_c2,2000,2000)

    canvas.move(block_a3,2000,2000)
    canvas.move(block_b3,2000,2000)
    canvas.move(block_c3,2000,2000)

    canvas.move(block_d4,2000,2000)
    canvas.move(block_e4,2000,2000)
    canvas.move(block_f4,2000,2000)

    canvas.move(block_d5,2000,2000)
    canvas.move(block_e5,2000,2000)
    canvas.move(block_f5,2000,2000)

    canvas.move(block_d6,2000,2000)
    canvas.move(block_e6,2000,2000)
    canvas.move(block_f6,2000,2000)
    canvas.update()

    if X == 25 or X == 625 or Y == 25 or Y == 625 or X == 325 or Y == 325: # checks for overlapping
        print("lost")
        lose_game()
    canvas.after(1000 - time)
    canvas.move(block_a1,-2000,-2000)
    canvas.move(block_b1,-2000,-2000)
    canvas.move(block_c1,-2000,-2000)

    canvas.move(block_a2,-2000,-2000)
    canvas.move(block_b2,-2000,-2000)
    canvas.move(block_c2,-2000,-2000)

    canvas.move(block_a3,-2000,-2000)
    canvas.move(block_b3,-2000,-2000)
    canvas.move(block_c3,-2000,-2000)

    canvas.move(block_d4,-2000,-2000)
    canvas.move(block_e4,-2000,-2000)
    canvas.move(block_f4,-2000,-2000)

    canvas.move(block_d5,-2000,-2000)
    canvas.move(block_e5,-2000,-2000)
    canvas.move(block_f5,-2000,-2000)

    canvas.move(block_d6,-2000,-2000)
    canvas.move(block_e6,-2000,-2000)
    canvas.move(block_f6,-2000,-2000)
    canvas.update()
    stage_4()


def stage_4(): # stage 4 of the game
    global score
    score+=10
    txt = "score:" + str(score)
    canvas.itemconfigure(score_text, text=txt)

    shake12(block_c1,block_c2,block_c3,block_c4,block_c5,block_c6,block_d1,block_d2,block_d3,block_d4,block_d5,block_d6)
    canvas.move(block_c1,2000,2000)
    canvas.move(block_c2,2000,2000)
    canvas.move(block_c3,2000,2000)
    canvas.move(block_c4,2000,2000)
    canvas.move(block_c5,2000,2000)
    canvas.move(block_c6,2000,2000)
    canvas.move(block_d1,2000,2000)
    canvas.move(block_d2,2000,2000)
    canvas.move(block_d3,2000,2000)
    canvas.move(block_d4,2000,2000)
    canvas.move(block_d5,2000,2000)
    canvas.move(block_d6,2000,2000)
    canvas.update()

    if X == 25 or X == 625 or Y == 25 or Y == 625 or X == 425 or X == 225: # checks for overlapping
        print("lost")
        lose_game()
    canvas.after(1000 - time)
    canvas.move(block_c1,-2000,-2000)
    canvas.move(block_c2,-2000,-2000)
    canvas.move(block_c3,-2000,-2000)
    canvas.move(block_c4,-2000,-2000)
    canvas.move(block_c5,-2000,-2000)
    canvas.move(block_c6,-2000,-2000)
    canvas.move(block_d1,-2000,-2000)
    canvas.move(block_d2,-2000,-2000)
    canvas.move(block_d3,-2000,-2000)
    canvas.move(block_d4,-2000,-2000)
    canvas.move(block_d5,-2000,-2000)
    canvas.move(block_d6,-2000,-2000)
    canvas.update()
    stage_5()


def stage_5(): # stage 5 of the game
    shake18(block_a4,block_b4,block_c4,block_a5,block_b5,block_c5,block_a6,block_b6,block_c6,block_d1,block_e1,block_f1,block_d2,block_e2,block_f2,block_d3,block_e3,block_f3)
    global score, time
    score+=10 # increase the score
    txt = "score:" + str(score)
    canvas.itemconfigure(score_text, text=txt)
    time += 200 # reduce the delay between stages
    canvas.move(block_a6,2000,2000)
    canvas.move(block_b6,2000,2000)
    canvas.move(block_c6,2000,2000)

    canvas.move(block_a5,2000,2000)
    canvas.move(block_b5,2000,2000)
    canvas.move(block_c5,2000,2000)

    canvas.move(block_a4,2000,2000)
    canvas.move(block_b4,2000,2000)
    canvas.move(block_c4,2000,2000)

    canvas.move(block_d3,2000,2000)
    canvas.move(block_e3,2000,2000)
    canvas.move(block_f3,2000,2000)

    canvas.move(block_d2,2000,2000)
    canvas.move(block_e2,2000,2000)
    canvas.move(block_f2,2000,2000)

    canvas.move(block_d1,2000,2000)
    canvas.move(block_e1,2000,2000)
    canvas.move(block_f1,2000,2000)
    canvas.update()

    if X == 25 or X == 625 or Y == 25 or Y == 625 or X == 325 or Y == 325: # check for overlapping
        print("lost")
        lose_game()
    canvas.after(1000 - time)
    canvas.move(block_a6,-2000,-2000)
    canvas.move(block_b6,-2000,-2000)
    canvas.move(block_c6,-2000,-2000)

    canvas.move(block_a5,-2000,-2000)
    canvas.move(block_b5,-2000,-2000)
    canvas.move(block_c5,-2000,-2000)

    canvas.move(block_a4,-2000,-2000)
    canvas.move(block_b4,-2000,-2000)
    canvas.move(block_c4,-2000,-2000)

    canvas.move(block_d3,-2000,-2000)
    canvas.move(block_e3,-2000,-2000)
    canvas.move(block_f3,-2000,-2000)

    canvas.move(block_d2,-2000,-2000)
    canvas.move(block_e2,-2000,-2000)
    canvas.move(block_f2,-2000,-2000)

    canvas.move(block_d1,-2000,-2000)
    canvas.move(block_e1,-2000,-2000)
    canvas.move(block_f1,-2000,-2000)
    canvas.update()
    stage_0()

def lose_game():
    window.unbind("<a>") # disable the keys
    window.unbind("<w>")
    window.unbind("<s>")
    window.unbind("<d>")
    window.unbind("<p>")
    canvas.after(300)
    canvas.destroy()

    global l_canvas
    l_canvas = Canvas(window, bg= "orange") # creat a canvas to display game over
    l_canvas.place(relwidth= 1,relheight=1, relx= 0, rely=0)

    l_canvas.create_text(350,350,fill="white",font="Times 25 italic bold", text="Game Over!")
    l_canvas.update()
    back = Button(l_canvas, text= " home menu", command = lambda: home_buttons())  # go back to home menu
    back.place(x = 300, y = 400)
    play = Button(l_canvas, text= " play again", command = lambda: start_game()) # start the game
    play.place(x = 300, y = 450)


def exit():
    window.destroy()


def instructions():
    global ins_canvas    # creat a canvas to show all the instructions
    ins_canvas = Canvas(window, bg= "white")
    ins_canvas.place(relwidth= 1,relheight=1, relx= 0, rely=0)
    ins_canvas.create_text(300,600,fill="red",font="Times 25 italic bold", text=" (k) increase the score")
    ins_canvas.create_text(300,550,fill="black",font="Times 25 italic bold", text=" press (l) to start the game")
    ins_canvas.create_text(300,500,fill="black",font="Times 25 italic bold", text=" press (w) to move forward")
    ins_canvas.create_text(300,450,fill="black",font="Times 25 italic bold", text=" press (s) to move backward")
    ins_canvas.create_text(300,400,fill="black",font="Times 25 italic bold", text=" press (a) to move to the left")
    ins_canvas.create_text(300,350,fill="black",font="Times 25 italic bold", text=" press (d) to move to the right")
    ins_canvas.create_text(350,300,fill="black",font="Times 25 italic bold", text=" to win you have to avoid falling into the lava")
    ins_canvas.create_text(350,250,fill="black",font="Times 25 italic bold", text="by staying in a stable block as some blocks will fall ")
    ins_canvas.update()

    back =Button(ins_canvas, text= " home menu", command = lambda: home_buttons()) # go back to home menu
    back.place(relx=.35, rely= .1, relwidth=0.11, relheight=.11)
    play = Button(ins_canvas, text = " play", command = lambda: start_game()) # start the game
    play.place(relx=.46, rely= .1, relwidth=0.11, relheight=.11)


def home_buttons():  # main menu function
    l_canvas.destroy()
    ins_canvas.destroy()
    button = [None]*4
    new_game = PhotoImage(file="newgame1.png")   # impors images
    resume = PhotoImage(file="resume1.png")
    how_to_play= PhotoImage(file="instructions1.png")
    leaderBoard = PhotoImage(file="leaderboard1.png")

    button[0] = Button(window, image=new_game, command = lambda: start_game()) # starts the game
    button[0].place(relx=.3, rely= .1, relwidth=0.42, relheight=.18)

    button[1] = Button(window, image=resume)
    button[1].place(relx=0.3, rely= .3, relwidth=.42, relheight=.18)


    button[2] = Button(window, image=how_to_play, command = lambda: instructions()) # displays instructions
    button[2].place(relx=.3, rely= .5, relwidth=0.42, relheight=.18)

    button[3] = Button(window, image=leaderBoard)
    button[3].place(relx=.3, rely= .7, relwidth=.42, relheight=.18)

    esc = Button(window,bg = "orange", text= " exit ", command = lambda: exit())
    esc.place(x = 600, y = 650, width = 100, height = 50)
    window.mainloop()


# a function to shake (move) 18 blocks
def shake18(image1,image2,image3,image4,image5,image6,image7,image8, image9,image1a,image2a,image3a,image4a,image5a,image6a,image7a,image8a, image9a):
    counter = 0
    while counter < 3:
        counter += 1
        canvas.move(image1, 0, 1)
        canvas.move(image3, 0, 1)
        canvas.move(image5, 0, 1)
        canvas.move(image7, 0, 1)
        canvas.move(image9, 0, 1)
        canvas.move(image1a, 0, 1)
        canvas.move(image3a, 0, 1)
        canvas.move(image5a, 0, 1)
        canvas.move(image7a, 0, 1)
        canvas.move(image9a, 0, 1)
        window.update()
        canvas.after(200)

        canvas.move(image1, 0, -1)
        canvas.move(image3, 0, -1)
        canvas.move(image5, 0, -1)
        canvas.move(image7, 0, -1)
        canvas.move(image9, 0, -1)
        canvas.move(image1a, 0, -1)
        canvas.move(image3a, 0, -1)
        canvas.move(image5a, 0, -1)
        canvas.move(image7a, 0, -1)
        canvas.move(image9a, 0, -1)
        window.update()
        canvas.after(200)

        canvas.move(image2, 0, -1)
        canvas.move(image4, 0, -1)
        canvas.move(image6, 0, -1)
        canvas.move(image8, 0, -1)
        canvas.move(image2a, 0, -1)
        canvas.move(image4a, 0, -1)
        canvas.move(image6a, 0, -1)
        canvas.move(image8a, 0, -1)
        window.update()
        canvas.after(200)

        canvas.move(image2, 0, 1)
        canvas.move(image4, 0, 1)
        canvas.move(image6, 0, 1)
        canvas.move(image8, 0, 1)
        canvas.move(image2a, 0, 1)
        canvas.move(image4a, 0, 1)
        canvas.move(image6a, 0, 1)
        canvas.move(image8a, 0, 1)
        window.update()

        canvas.after(200)
        canvas.move(image1, 1, 0)
        canvas.move(image2, 0, 1)
        canvas.move(image3, -1, 0)
        canvas.move(image4, 0, -1)
        canvas.move(image5, 1, 0)
        canvas.move(image6, 0, 1)
        canvas.move(image7, -1, 0)
        canvas.move(image8, 0, -1)
        canvas.move(image9, 1, 1)
        canvas.move(image1a, 1, 0)
        canvas.move(image2a, 0, 1)
        canvas.move(image3a, -1, 0)
        canvas.move(image4a, 0, -1)
        canvas.move(image5a, 1, 0)
        canvas.move(image6a, 0, 1)
        canvas.move(image7a, -1, 0)
        canvas.move(image8a, 0, -1)
        canvas.move(image9a, 1, 1)
        window.update()
        canvas.after(200)

        canvas.move(image1, -1, 0)
        canvas.move(image2, 0, -1)
        canvas.move(image3, 1, 0)
        canvas.move(image4, 0, 1)
        canvas.move(image5, -1, 0)
        canvas.move(image6, 0, -1)
        canvas.move(image7, 1, 0)
        canvas.move(image8, 0, 1)
        canvas.move(image9, -1, -1)
        canvas.move(image1a, -1, 0)
        canvas.move(image2a, 0, -1)
        canvas.move(image3a, 1, 0)
        canvas.move(image4a, 0, 1)
        canvas.move(image5a, -1, 0)
        canvas.move(image6a, 0, -1)
        canvas.move(image7a, 1, 0)
        canvas.move(image8a, 0, 1)
        canvas.move(image9a, -1, -1)
        window.update()
        canvas.after(200)
        window.update()


def shake9(image1,image2,image3,image4,image5,image6,image7,image8, image9): # a function to shake (move) 9 blocks
    counter = 0
    while counter < 3:
        counter += 1
        canvas.move(image1, 0, 1)
        canvas.move(image3, 0, 1)
        canvas.move(image5, 0, 1)
        canvas.move(image7, 0, 1)
        canvas.move(image9, 0, 1)
        window.update()
        canvas.after(200)

        canvas.move(image1, 0, -1)
        canvas.move(image3, 0, -1)
        canvas.move(image5, 0, -1)
        canvas.move(image7, 0, -1)
        canvas.move(image9, 0, -1)
        window.update()
        canvas.after(200)

        canvas.move(image2, 0, -1)
        canvas.move(image4, 0, -1)
        canvas.move(image6, 0, -1)
        canvas.move(image8, 0, -1)
        window.update()
        canvas.after(200)

        canvas.move(image2, 0, 1)
        canvas.move(image4, 0, 1)
        canvas.move(image6, 0, 1)
        canvas.move(image8, 0, 1)
        window.update()

        canvas.after(200)
        canvas.move(image1, 1, 0)
        canvas.move(image2, 0, 1)
        canvas.move(image3, -1, 0)
        canvas.move(image4, 0, -1)
        canvas.move(image5, 1, 0)
        canvas.move(image6, 0, 1)
        canvas.move(image7, -1, 0)
        canvas.move(image8, 0, -1)
        canvas.move(image9, 1, 1)
        window.update()
        canvas.after(200)

        canvas.move(image1, -1, 0)
        canvas.move(image2, 0, -1)
        canvas.move(image3, 1, 0)
        canvas.move(image4, 0, 1)
        canvas.move(image5, -1, 0)
        canvas.move(image6, 0, -1)
        canvas.move(image7, 1, 0)
        canvas.move(image8, 0, 1)
        canvas.move(image9, -1, -1)
        window.update()
        canvas.after(200)
        window.update()


def shake12(image1,image2,image3,image4,image5,image6,image1b,image2b,image3b,image4b,image5b,image6b): # a function to shake (move) 12 blocks
    counter = 0
    while counter < 3:
        counter += 1
        canvas.move(image1, 0, 1)
        canvas.move(image3, 0, 1)
        canvas.move(image5, 0, 1)
        canvas.move(image1b, 0, 1)
        canvas.move(image3b, 0, 1)
        canvas.move(image5b, 0, 1)
        window.update()
        canvas.after(200)

        canvas.move(image1, 0, -1)
        canvas.move(image3, 0, -1)
        canvas.move(image5, 0, -1)
        canvas.move(image1b, 0, -1)
        canvas.move(image3b, 0, -1)
        canvas.move(image5b, 0, -1)
        window.update()
        canvas.after(200)

        canvas.move(image2, 0, -1)
        canvas.move(image4, 0, -1)
        canvas.move(image6, 0, -1)
        canvas.move(image2b, 0, -1)
        canvas.move(image4b, 0, -1)
        canvas.move(image6b, 0, -1)
        window.update()
        canvas.after(200)

        canvas.move(image2, 0, 1)
        canvas.move(image4, 0, 1)
        canvas.move(image6, 0, 1)
        canvas.move(image2b, 0, 1)
        canvas.move(image4b, 0, 1)
        canvas.move(image6b, 0, 1)
        window.update()

        canvas.after(200)
        canvas.move(image1, 1, 0)
        canvas.move(image2, 0, 1)
        canvas.move(image3, -1, 0)
        canvas.move(image4, 0, -1)
        canvas.move(image5, 1, 0)
        canvas.move(image6, 1, 1)
        canvas.move(image1b, 1, 0)
        canvas.move(image2b, 0, 1)
        canvas.move(image3b, -1, 0)
        canvas.move(image4b, 0, -1)
        canvas.move(image5b, 1, 0)
        canvas.move(image6b, 1, 1)
        window.update()
        canvas.after(200)

        canvas.move(image1, -1, 0)
        canvas.move(image2, 0, -1)
        canvas.move(image3, 1, 0)
        canvas.move(image4, 0, 1)
        canvas.move(image5, -1, 0)
        canvas.move(image6, -1, -1)
        canvas.move(image1b, -1, 0)
        canvas.move(image2b, 0, -1)
        canvas.move(image3b, 1, 0)
        canvas.move(image4b, 0, 1)
        canvas.move(image5b, -1, 0)
        canvas.move(image6b, -1, -1)
        window.update()


def default():
    global block_a1, block_a2, block_a3, block_a4, block_a5, block_a6
    global block_b1, block_b2, block_b3, block_b4, block_b5, block_b6
    global block_c1, block_c2, block_c3, block_c4, block_c5, block_c6
    global block_d1, block_d2, block_d3, block_d4, block_d5, block_d6
    global block_e1, block_e2, block_e3, block_e4, block_e5, block_e6
    global block_f1, block_f2, block_f3, block_f4, block_f5, block_f6,blockImage
    blockImage = PhotoImage(file="blocks100.png")                   #gets the images of the blocks
    block_a1 = canvas.create_image(100, 100, image = blockImage)    # displays all 36 blocks
    block_a2 = canvas.create_image(100, 200, image = blockImage)    # i ordered then so the first rows are a,b,c,d,e,f and columns are numbers
    block_a3 = canvas.create_image(100, 300, image = blockImage)
    block_a4 = canvas.create_image(100, 400, image = blockImage)
    block_a5 = canvas.create_image(100, 500, image = blockImage)
    block_a6 = canvas.create_image(100, 600, image = blockImage)

    block_b1 = canvas.create_image(200, 100, image = blockImage)
    block_b2 = canvas.create_image(200, 200, image = blockImage)
    block_b3 = canvas.create_image(200, 300, image = blockImage)
    block_b4 = canvas.create_image(200, 400, image = blockImage)
    block_b5 = canvas.create_image(200, 500, image = blockImage)
    block_b6 = canvas.create_image(200, 600, image = blockImage)

    block_c1 = canvas.create_image(300, 100, image = blockImage)
    block_c2 = canvas.create_image(300, 200, image = blockImage)
    block_c3 = canvas.create_image(300, 300, image = blockImage)
    block_c4 = canvas.create_image(300, 400, image = blockImage)
    block_c5 = canvas.create_image(300, 500, image = blockImage)
    block_c6 = canvas.create_image(300, 600, image = blockImage)

    block_d1 = canvas.create_image(400, 100, image = blockImage)
    block_d2 = canvas.create_image(400, 200, image = blockImage)
    block_d3 = canvas.create_image(400, 300, image = blockImage)
    block_d4 = canvas.create_image(400, 400, image = blockImage)
    block_d5 = canvas.create_image(400, 500, image = blockImage)
    block_d6 = canvas.create_image(400, 600, image = blockImage)

    block_e1 = canvas.create_image(500, 100, image = blockImage)
    block_e2 = canvas.create_image(500, 200, image = blockImage)
    block_e3 = canvas.create_image(500, 300, image = blockImage)
    block_e4 = canvas.create_image(500, 400, image = blockImage)
    block_e5 = canvas.create_image(500, 500, image = blockImage)
    block_e6 = canvas.create_image(500, 600, image = blockImage)

    block_f1 = canvas.create_image(600, 100, image = blockImage)
    block_f2 = canvas.create_image(600, 200, image = blockImage)
    block_f3 = canvas.create_image(600, 300, image = blockImage)
    block_f4 = canvas.create_image(600, 400, image = blockImage)
    block_f5 = canvas.create_image(600, 500, image = blockImage)
    block_f6 = canvas.create_image(600, 600, image = blockImage)
    global score, time
    time = 0                                   # reset the time and score so it start from zero if you played again
    score = 0
    creat_character()

    window.bind("<a>", move_character)        # bind all the keys that will be used in the game
    window.bind("<w>", move_character)
    window.bind("<s>", move_character)
    window.bind("<d>", move_character)
    window.bind("<p>", move_character)
    window.bind("<l>", move_character)
    window.bind("<k>", move_character)
    window.bind("<j>", move_character)
    window.mainloop()


def start_game():
    l_canvas.destroy()
    global canvas, be_ready # canvas to (display be ready)
    canvas = Canvas(window, bg= "#ff9900")
    canvas.place(relwidth= 1,relheight=1, relx= 0, rely=0)
    be_ready = canvas.create_text(350,350,fill="white",font="Times 25 italic bold", text="Be Ready!")
    window.update()
    canvas.after(1500)
    canvas.delete(be_ready) # after a delay start the game
    window.update()
    default()
    canvas.pack

width = 700                                     #the window coords
height = 700


window = Tk()                               #creat the main window for the game
window.title("My Game")
window.configure(background='white')
screen_width = window.winfo_screenwidth()
screen_hight = window.winfo_screenheight()
senter_x = (screen_width/2) - (width/2)
senter_y = (screen_hight/2) - (height/2)           # to senter the window
window.geometry('%dx%d+%d+%d' % (width, height, senter_x, senter_y))
l_canvas = Canvas(window, bg= "orange")
ins_canvas = Canvas(window, bg= "white")
X = 0                                           # coodrs for the character
Y = 0                                           # coodrs for the character
home_buttons()
