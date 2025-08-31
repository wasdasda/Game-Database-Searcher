import os
print("Choose an action: 1.Search games; 2.Add new games")
choice=input()
if choice=="1":
    os.system("python3 ~/python-projects/gamedatasearch/database.py")
elif choice=="2":
    os.system("python3 ~/python-projects/gamedatasearch/database_adder.py")