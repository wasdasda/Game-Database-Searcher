import json
import os
CONFIG_FILE="database.json"
db={}
def load_database():
    with open (CONFIG_FILE,"r", encoding="utf-8") as f:
        return json.load(f)
def save_database(db):
    with open (CONFIG_FILE,"w",encoding="utf-8") as f:
        return json.dump(db, f, ensure_ascii=False, indent=4)

print("Add a game:")
game=input().upper()
while game in db:
    print("Error:game is already in database!")
    print("Try again:")
    game=input().upper()
print("Enter a release year:")
year=input()
print("Enter a platform that game have been released for:")
platform=input().upper().strip()
db = load_database()
db[game]=[year, platform]
save_database(db)
print(f"Game {game} has been succesfully added")