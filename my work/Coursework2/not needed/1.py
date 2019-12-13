from tkinter import Tk, Canvas
from random import randint as rand

def create_arc(start, end, colour):
    xy = 50,50,500,500
    return canvas.create_arc(xy, start=start, extent=end, fill=colour)

def create_gui():
    light_colour = ['#ffcccb', '#add8e6', '#90ee90', '#ffffed']
    for i in range(4):
        arc.append(create_arc(i*90,90,light_colour[i]))
    global text, score_text
    text = canvas.create_text(700,275, fill="white", font="Times 20 italic bold", text="Get Ready !!!")
    score_text = canvas.create_text(900,20, fill="white", font="Times 20 italic bold", text="Score: 0")
    canvas.pack()

def move_arc(arcc, x, y):
    print(arcc)
    print (arc[arcc])
    canvas.move(arc[arcc],x,y)


def dim_arc(r):
    colour = ['#ffcccb', '#add8e6', '#90ee90', '#ffffed']
    canvas.itemconfigure(arc[r], fill=colour[r])

def light_arc(r):
    colour = ['red', 'blue', 'green', 'yellow']
    canvas.itemconfigure(arc[r], fill=colour[r])
    canvas.after(500, dim_arc,r)

def active_mouse():
    canvas.itemconfig(text, text="Recall")
    canvas.bind("<Button-1>", click_event)

def deactive_mouse():
    canvas.unbind("<Button-1>")

def watch_remember():
    canvas.itemconfig(text, text="Watch and Remember!")


def click_event(event):
    x = event.x
    y = event.y
    global click_num
    print(seq_list)
    area_clicked = -1
    if (x > 275 and y < 275):
        print("Area clicked is 0")
        area_clicked = 0
        light_arc(0)
        canvas.after(200, move_arc, area_clicked, 5,-5)
        canvas.after(400, move_arc, area_clicked, -5,5)
    elif (x < 275 and y < 275):
        print("Area clicked is 1")
        area_clicked = 1
        light_arc(1)
        canvas.after(200, move_arc, area_clicked, -5,-5)
        canvas.after(400, move_arc, area_clicked, 5,5)
    elif (x < 275 and y > 275):
        print("Area clicked is 2")
        area_clicked = 2
        light_arc(2)
        canvas.after(200, move_arc, area_clicked, -5,5)
        canvas.after(400, move_arc, area_clicked, 5,-5)
    elif (x > 275 and y > 275):
        print("Area clicked is 3")
        area_clicked = 3
        light_arc(3)
        canvas.after(200, move_arc, area_clicked, 5,5)
        canvas.after(400, move_arc, area_clicked, -5,-5)


    if (area_clicked == seq_list[click_num]):
        global score
        score += 10
        canvas.itemconfig(score_text, text="Score: " + str(score))
    else:
        deactive_mouse()
        click_num = -1
        canvas.itemconfig(text, text="Incorrect\nGame Over!")

    click_num += 1

    if (click_num == len(seq_list)):
        deactive_mouse()
        flash_count = click_num + 1
        click_num = 0
        seq_list.clear()
        canvas.after(2000, flash_loop, flash_count)

def flash_loop(flash_count):
    flash_count -= 1
    r = rand(0,3)
    seq_list.append(r)
    canvas.after(1000, light_arc, r)
    watch_remember()
    if flash_count > 0:
        canvas.after(2000, flash_loop, flash_count)
    else:
        canvas.after(2000, active_mouse)

score = 0
score_text = None
text = None

window = Tk()
canvas = Canvas(window, bg="black", width=1000, height=550)

arc = []
seq_list = []
create_gui()
canvas.after(4000, flash_loop, 1)
click_num = 0
window.mainloop()
