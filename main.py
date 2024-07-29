from tkinter import *
from tkinter import ttk
import os

# Make window
root = Tk()
root.title("Tic Tac Toe")
root.geometry("238x255")

# Winning Possibilites
wins = [(1,2,3),(4,5,6), (7,8,9),(1,5,9), (3,5,7),(1,4,7),(2,5,8), (3,6,9)]

player1 = []
player2 = []

# 0 = player1's turn
# 1 = player2's turn
turn = 0
total_turn = 0

# End game functionality 
end_game = False

# Message
msg = ""

def popup_window():
    global msg
    win = Toplevel()
    win.geometry("300x100")
    win.lift()
    win.wm_title("Game Over")
    label = Label(win, text=msg, justify="center", width=90, font=("Courier", 20))
    label.pack()

def check_winnder(player):
    for tpl in wins:
        if tpl[0] in player and tpl[1] in player and tpl[2] in player:
            return 0
    
    return 1

path = os.path.dirname(os.path.realpath(__file__))

def play(s, cbutton):
    global turn
    global total_turn
    global end_game
    global msg

    if(total_turn > 9):
        # Game should end after all spots are filled
        end_game = TRUE
        msg = "Draw"
        popup_window()       
    elif(s in player1 or s in player2 or end_game == TRUE):
        # Make sure no one is able to click on the same spot more than once
        return
    
    # How game takes turns    
    if turn == 0:
        player1.append(s)
        # img = PhotoImage(file= path + '/images/circle.png')        
        # cbutton.config(image = img)
        cbutton.config(bg='red')
        if (check_winnder(player1) == 0):
            end_game = TRUE
            msg = "Player 1 wins"
            popup_window()     
    else:
        player2.append(s)
        # img = PhotoImage(file= path + '/images/x.png')
        # cbutton.config(image = img)
        cbutton.config(bg='blue')
        if(check_winnder(player2) == 0):
            end_game = TRUE
            msg = "Player 2 wins"
            popup_window()   
    
    total_turn += 1
    turn = 1 if turn == 0  else 0    

button1 = Button(root,width=10,height=5)
button1.grid(column=0,row=0)
button1.config(command=lambda m=1: play(m, button1))

button2 = Button(root,width=10,height=5)
button2.grid(column=1,row=0)
button2.config(command=lambda m=2: play(m, button2))

button3 = Button(root,width=10,height=5)
button3.grid(column=2,row=0)
button3.config(command=lambda m=3: play(m, button3))

button4 = Button(root,width=10,height=5)
button4.grid(column=0,row=1)
button4.config(command=lambda m=4: play(m, button4))

button5 = Button(root,width=10,height=5)
button5.grid(column=1,row=1)
button5.config(command=lambda m=5: play(m,button5))

button6 = Button(root,width=10,height=5)
button6.grid(column=2,row=1)
button6.config(command=lambda m=6: play(m,button6))

button7 = Button(root,width=10,height=5)
button7.grid(column=0,row=2)
button7.config(command=lambda m=7: play(m,button7))

button8 = Button(root,width=10,height=5)
button8.grid(column=1,row=2)
button8.config(command=lambda m=8: play(m,button8))

button9 = Button(root,width=10,height=5)
button9.grid(column=2,row=2)
button9.config(command=lambda m=9: play(m,button9))

root.mainloop()



