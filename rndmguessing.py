from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

root = Tk()
root.title("Guess iT!")
root.geometry("800x600")
root.minsize(800, 600)
root.maxsize(800, 600)

##Variables
max_life = IntVar()
rndm = IntVar()
guess = IntVar()
news = StringVar()
stat = StringVar()
diff = IntVar()
dstat = StringVar()

##functions

##announce

def g_dstat(*args):
    d = diff.get()
    if d < 5 and d>-5:
        dstat.set("Very Close")
    elif d < 10 and d > -10:
        dstat.set("Close")
    elif d < 20 and d>-20:
        dstat.set("Somewhat close")
    else:
        dstat.set("Not even close")

def announce(*args):
    g_dstat()
    messagebox.showinfo(title="announce",message=f"Incorrect Guess!,You are {dstat.get()},{news.get()}")
    
##lose or win
def decision(*args):
    b = messagebox.askyesno(message=f"You {stat.get()},The number was {rndm.get()} do you want to Restart the Game?", title="Decide!")
    if b==True:
        initialize_game()
        entry.focus_set()
    else:
        root.destroy()
        return

##starting the game
def initialize_game(*args):
    guess.set("")##fix of the century bruhhhh i was trying so damn hard to get rid of zero shown in the entry feild when i wrote guess.set("") bruh i just needed to write guess.set("") heck nahhh
    gen_num()
    max_life.set(3)

##generating number yrr
def gen_num(*args):
    rndm.set(randint(0,100))
initialize_game()

##checking the input
def check(*args):
    try:
        user_guess = guess.get()
        if user_guess<0 or user_guess>100:
            news.set("Enter Numbers Between 0-100 Only!")
            announce()
            guess.set("")
            return
    except:
        news.set("Enter Numbers Only!!!")
        announce()
        guess.set("")
        return
    if max_life.get() == 0:
        if guess.get()==rndm.get():
            stat.set("Wonnnn!!")
            decision()
            return
        stat.set("Lost")
        decision()
        return
    max_life.set(max_life.get()-1)
    diff.set(rndm.get()-guess.get())
    if guess.get()==rndm.get():
        stat.set("Wonnnn!!")
        decision()
    elif guess.get()>rndm.get():
        news.set(f"try going lower")
        announce()
        guess.set("")    
    elif guess.get()<rndm.get():
        news.set(f"try going Higher")
        announce()
        guess.set("")



# ✅ ADD THIS - Configure root to allow mainframe to expand
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(row=0, column=0, sticky="N W E S")
mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(1, weight=1)

# Now center the label properly
##title
ttk.Label(mainframe, text="Guess The Number", 
          foreground="White", background="Black", 
          font=("Railway", 20, "bold"),
          anchor=CENTER).grid(column=0, row=0, pady=25, columnspan=2)

##subtitle
ttk.Label(mainframe, 
          text="Guess The Random Number Between 0-100").grid(row=1, column=0,columnspan=2)
ttk.Label(mainframe, textvariable=max_life).grid(row=2, column=1,sticky=W)
ttk.Label(mainframe, text="Attempts Left").grid(row=2, column=0, sticky=E)

##Entering part
ttk.Label(mainframe, text="Your Guess: ").grid(row=3, column=0,sticky=E)
entry = ttk.Entry(mainframe, width=3, textvariable=guess)##if u chain it up like directly adding .grid and stuff it wont focus because it returns none
entry.grid(row=3,column=1,sticky=W)
entry.focus_set()

##announce

#Buttons
ttk.Button(mainframe, text="Check Guess", command=check).grid(column=0,row=5, sticky=E)
ttk.Button(mainframe, text="New Game", command=initialize_game).grid(column=1,row=5,sticky=W)

root.bind("<Return>", check)

root.mainloop()


###things i learnt
##sequence matters a lot