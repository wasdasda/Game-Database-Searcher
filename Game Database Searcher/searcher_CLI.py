import json
import tkinter as tk
from tkinter import ttk
def load_db():

    with open("database.json", "r") as f:
        return json.load(f)


info=load_db()
select="p"
print("Aviable games:", ",".join(info.keys()))
print("Search for game info:")
while select!="STOP":
        select=input()
        select=select.upper()
        if select in info:
            infoplus=info [select]
            print (f"This game released in {infoplus[0]} year for {infoplus[1]} platform.")
        elif select=="STOP":
            print("Shutting searcher down...")
        else:
                matches = [game_name for game_name in info.keys() if select in game_name]
                if matches:
                    print(f"Maybe, you meant {', '.join(matches)}?")
                else:
                    print(f"Sorry, but we haven't this game in our database. Choose another game, like: {", ".join(info.keys())}")
