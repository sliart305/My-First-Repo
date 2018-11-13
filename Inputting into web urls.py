import webbrowser as wb
import pyautogui as pg

"""
birthday = input("What month is your birthday?")
wb.open("https://www.google.com/search?q=" + birthday + " birth stone")

answer = input("What's your favorite animal?")
wb.open("https://www.youtube.com/results?search_query=" + answer + " videos")

DOB = input("What's your birthday?")
wb.open("https://www.google.com/search?q=" + DOB + " zodiac")

name = input("What's your name?").title()
classmates = ["Betsy", "Owen", "Simon", "Caroline", "Ryan"]
if name in classmates:
    print("You're in my class!")

color = input("What's your favorite color?")
wb.open("https://www.google.com/search?q=" + color + " color")

book = pg.prompt("What is your favorite book series?").title()

if "Harry Potter" in book:
    character = pg.prompt("Which character is your favorite?").title()

    if character == "Harry":
        pg.alert("Well that's just fantastic!")
    elif character == "Hermoine":
        pg.alert("She helps the other two a whole more than most think doesn't she")

ice_cream = pg.confirm("Which of these flavors is your favorite?", "Choose one", ["chocolate", "vanilla", "hazelnut", "coffee"])
if ice_cream == "vanilla":
    pg.alert("OOooooo")
elif ice_cream == "chocolate":
    pg.alert("Yum!")
elif ice_cream == "coffee":
    pg.alert("YESSSSS")
elif ice_cream == "hazelnut":
    pg.alert("That sounds good!")
"""

f = open('harry secret password file.txt',"w")

house = pg.confirm("Which house are you?",
                   "Choose one",
                   ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'])

if house in ["Slytherin"]:
    password = pg.password("What's the secret code?",
                           "Enter code below")

f.write("Sarah, this is the password for the file: " + password)

f.close()

