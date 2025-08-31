import json
import tkinter as tk
from tkinter import ttk
#Declaring Variables
infoplus=[]
db={}
#Import JSON Function
def load_db():
    with open ("database.json","r") as f:
        return json.load(f)
#Export JSON Function
def write_db(db):
    with open ("database.json","w",encoding="utf-8") as f:
        return json.dump(db, f, ensure_ascii=False, indent=4)

#Game Database Adder Window
def add():
    global gn_etr, yr_etr,plt_etr, wdw2
    wdw2=tk.Toplevel()
    wdw2.title("Database Game Adder")
    hed=tk.Label(wdw2, text="Adding Game Database Tool(2025)")
    gn_etr=tk.Entry(wdw2,width="40")
    yr_etr=tk.Entry(wdw2,width="40")
    plt_etr=tk.Entry(wdw2,width="40")
    gn=tk.Label(wdw2, text="Name:")
    yr=tk.Label(wdw2, text="Year:")
    plt=tk.Label(wdw2, text="Platform:")
    plusbtn=tk.Button(wdw2, text="Add", command=add_db)
    hed.grid()
    gn.grid(row=1, column=0)
    yr.grid(row=2, column=0)
    plt.grid(row=3, column=0)
    gn_etr.grid(row=1, column=1)
    yr_etr.grid(row=2, column=1)
    plt_etr.grid(row=3, column=1)
    plusbtn.grid(row=4, column=1)

    wdw2.mainloop()
#Adding Games Function
def add_db():
    db=load_db()
    game=gn_etr.get().upper()
    year=yr_etr.get().upper()
    platform=plt_etr.get().upper()
    db[game]=[year, platform]
    write_db(db)
    wdw2.destroy()
#Searching Games Function
def search():
    select=etr.get().upper()
    info=load_db()
    if select in info:
        infoplus=info[select]
        xtt= f"This game released in {infoplus[0]} year for {infoplus[1]} platform."
    else:
                matches = [game_name for game_name in info.keys() if select in game_name]
                if matches:
                    xtt=f"Maybe, you meant {', '.join(matches)}?"
                else:
                    xtt=f"Sorry, but we haven't this game in our database. Choose another game, like: {", ".join(info.keys())}"
#Result Window
    wdw1=tk.Toplevel()
    wdw1.title(f"Result for '{select}'")
    wdw1.geometry("400x100")
    gdt=tk.Label(wdw1, text=xtt, wraplength=400)
    gdt.grid(row=0,column=0)
    wdw1.mainloop()
#Main Menu
xtt=""
info=load_db()
wdw=tk.Tk()
wdw.title("Game Database  Searcher")
wdw.geometry=("800x600")
dgm=tk.Button(wdw, text="+", command=add)
lbl=tk.Label(wdw, text="Game Database Searcher(2025)")
etr=tk.Entry(wdw, width="60")
btn=tk.Button(wdw, text="Search It!", command=lambda: search())
btn.grid(row=1, column=1)
etr.grid(row=1,column=0)
lbl.grid(row=0, column=0)
dgm.grid(column=1)
wdw.mainloop()