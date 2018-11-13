import webbrowser as wb
import time as t
import pyautogui as pg
points = 0

name = pg.prompt("Hi! What's your name? ").title()

if name == "Murp":
    pg.alert ("hi me")
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=otfFW4vHGMe9ggfZ2r_4DA&q=alpaca&oq=alpaca&gs_l=img.3..0i67l2j0l2j0i67j0l2j0i67j0l2.3794.4865..5101...0.0..0.62.340.6......0....1..gws-wiz-img.FLEU5mw_LgE#imgrc=KvzBnpN81bKsrM:")
    points += 13
elif name == "Betsy":
    pg.alert ("Hey! I know you!")
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=otfFW4vHGMe9ggfZ2r_4DA&q=alpaca&oq=alpaca&gs_l=img.3..0i67l2j0l2j0i67j0l2j0i67j0l2.3794.4865..5101...0.0..0.62.340.6......0....1..gws-wiz-img.FLEU5mw_LgE#imgrc=s8X1zKLL6iIP4M:")
    points += 20
elif name == "Simon":
    pg.alert ("Yello")
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=otfFW4vHGMe9ggfZ2r_4DA&q=alpaca&oq=alpaca&gs_l=img.3..0i67l2j0l2j0i67j0l2j0i67j0l2.3794.4865..5101...0.0..0.62.340.6......0....1..gws-wiz-img.FLEU5mw_LgE#imgdii=nwM0sDMDkAUJtM:&imgrc=zo4BWRVMmwNAmM:")
    points += 5
elif name == "Ryan":
    pg.alert ("Hey Gordo")
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=otfFW4vHGMe9ggfZ2r_4DA&q=alpaca&oq=alpaca&gs_l=img.3..0i67l2j0l2j0i67j0l2j0i67j0l2.3794.4865..5101...0.0..0.62.340.6......0....1..gws-wiz-img.FLEU5mw_LgE#imgrc=zo4BWRVMmwNAmM:")
    points += 2
elif name == "Owen":
    pg.alert("Hola Owen")
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=alpaca&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi9oarnx5zeAhXEnOAKHaSRAgIQ_AUIDigB&biw=681&bih=616#imgrc=qGvHE0eXF3A-nM:")
elif name == "Caroline":
    pg.alert("Bello!")
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=alpaca&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi9oarnx5zeAhXEnOAKHaSRAgIQ_AUIDigB&biw=681&bih=616#imgrc=MwYytv4jWzWlpM:")
elif name == "Brooks":
    pg.alert("You're way to good for this class go home.")
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=alpaca&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi9oarnx5zeAhXEnOAKHaSRAgIQ_AUIDigB&biw=681&bih=616#imgrc=IU8ml8GMFcbSkM:")
elif name == "Mr. Rill":
    pg.alert("This was really annoying to do but i'm done now!")
else:
    pg.alert ("Hi " + name)
    t.sleep(.5)
    points += 0
    wb.open("https://www.google.com/search?q=alpaca&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi0t-jigoveAhVPh-AKHUjeDf0Q_AUIDigB&biw=681&bih=616#imgrc=iw0JmIfeZAtgQM:")

color = pg.prompt ("What's your favorite color?").lower()

if color == "purple":
    pg.alert("Well that's one of mine.")
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=purple&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjI86jB-oreAhVGh-AKHXufCZEQ_AUIDigB&biw=681&bih=616#imgrc=hLGloeJ6n3RdHM:")
    points += 7
elif color == "blue":
    pg.alert ("Yeah me too!")
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=blue&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjTpeDS-oreAhWHmeAKHU5uD1EQ_AUIDygC&biw=681&bih=616#imgdii=hnqXVjd_PhYZRM:&imgrc=55W__RRn4jKvPM:")
    points += 13
elif color == "white":
    pg.alert ("Yay! By the way, did you know " + color + " is the color of death.")
    t.sleep(.5)
    points += 23
    wb.open("https://www.google.com/search?q=the+mortal+instruments+quote+white+is+the+color+of+death&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiO-Jfr-oreAhVPhOAKHbaKCsYQ_AUIDigB&biw=681&bih=616#imgdii=48BRBd1131Ox4M:&imgrc=SNXbQEdbyDcd-M:")
elif color == "black":
    pg.alert ("Oooooo! " + color + " is the color of my soul. :)")
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=the+mortal+instruments+quote+white+is+the+color+of+death&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiO-Jfr-oreAhVPhOAKHbaKCsYQ_AUIDigB&biw=681&bih=616#imgrc=dXsmUpRT5xghYM:")
    points += 23
elif color == "orange":
    pg.alert("ewwwww")
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=HhXPW-XvEuKV_QbTqbjoCg&q=orange&oq=orange&gs_l=img.3..0i67l4j0l2j0i67j0l2j0i67.10785.11530..11659...0.0..0.56.307.6......0....1..gws-wiz-img.VrZEWO7KOAw#imgrc=_81V-vb8kUzMhM:")
elif color == "yellow":
    pg.alert("eh it's okay")
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=yellow&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj20cLHyZzeAhWtT98KHRyTDMgQ_AUIDigB&biw=681&bih=616")    
else:
    pg.alert ("Eh, okay, but I like a different one.")
    points += 0

t.sleep(1)

book = pg.prompt ("What is your favorite book or series?").lower()
    
if book == "i don't have one":
    pg.alert ("Actually same! It's too hard to pick.")
    points += 13
elif book == "something":
    pg.alert ("Well I guess that's probably true.")
    points += 9
elif book == "i don't like reading":
    pg.alert ("*GASP* How could you! Unfriending you now.")
    points -= 1000
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=why+reading+is+the+best+hobby&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwis_oCW9_vdAhWhneAKHUpvBIkQ_AUIDigB&biw=1366&bih=626#imgrc=JBCi92MiWjW-8M:")
elif book == "i don't have one, but i do have a favorite author":
    author = pg.prompt ("Yeah! Same! What's yours?")
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=sarah+j+maas&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjF9JKt-4reAhVBc98KHcYCCWIQ_AUIECgD&biw=681&bih=616#imgrc=2YbIv8_l6Y42UM:")
    points += 7
elif book == "no":
     answer = pg.prompt("Come on! Why not?")
     t.sleep(.5)
     wb.open("https://www.google.com/search?q=why&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj5mpHr-4reAhUvU98KHfUCCEkQ_AUIDigB&biw=681&bih=616#imgrc=5CPFRjs0iLKT4M:")

else:
    pg.alert ("Okay that's cool! I now know that " + name + " likes " + color + " and " + book)

dessert = pg.prompt("What's your favorite dessert?").lower()

if dessert == "brownies":
    pg.alert("yum!")
    points +=5
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=brownies&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjHxqSgypzeAhXjT98KHY4kBiYQ_AUIDigB&biw=681&bih=616")
elif dessert == "cookies":
    pg.alert("Ooooo those are good!")
    points +=4
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=cookies&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjlltC3ypzeAhVpneAKHSwMApwQ_AUIDigB&biw=681&bih=616")
elif dessert == "cake":
    pg.alert("Hi cake")
    points +=3
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=cake&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjzzp6ay5zeAhWuneAKHZUYASQQ_AUIDigB&biw=681&bih=616")
elif dessert == "ice cream":
    pg.alert("oooo yummy!")
    points +=5
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=LRfPW-zNBc_N_AaPvLlg&q=ice+cream&oq=ice+cream&gs_l=img.3..0i67l6j0l4.64880.66715..67037...0.0..0.71.634.12......0....1..gws-wiz-img.mWF299WhiTA")
elif dessert == "chocolate":
    pg.alert("yassss I love chocolate")
    points += 10
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=cRfPW7nhAZKe_QaxmorwCA&q=chocolate&oq=chocolate&gs_l=img.3..0i67l7j0l2j0i67.95442.97236..97358...1.0..0.68.511.10......0....1..gws-wiz-img.......0i10.PImIkhwyNAE")
elif dessert == "pie":
    pg.alert("I love pie, i also love making pie")
    points +=10
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=0hfPW-WtO_CzggfMmo2gBw&q=pie&oq=pie&gs_l=img.3..0i67j0j0i67j0l2j0i67j0j0i67j0l2.99457.100909..101053...1.0..0.50.239.5......0....1..gws-wiz-img.SgPM6bgu-eM")
else:
    pg.alert("OOoooooo yummy!")

art = pg.prompt("What is your favorite median for art?").lower()


if art == "pencil":
    art2 == pg.prompt("Yeah same! Is this the only median you use?")
    pg.alert("Okay that's cool!")
    points +=10
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=3BjPW-DjN6bp_Qb76qKgCQ&q=sketch+pencil&oq=sketch+pencil&gs_l=img.3..0l10.5383.6353..7808...0.0..0.61.372.7......0....1..gws-wiz-img.......0i7i30.eSylDl7DHdE#imgrc=c6KM6eecZAd90M:")
elif art == "oil paint":
    pg.alert("oh I like that")
    points +=5
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=QBnPW4meN6WIggf-jauIBQ&q=oil+paint&oq=oil+paint&gs_l=img.3..0i67l3j0j0i67l4j0l2.22066.22538..22719...0.0..0.80.252.4......0....1..gws-wiz-img.......0i7i30j0i10.mRIJQN1s0gE#imgrc=sS0RXEEP9uoWlM:")
elif art == "acrylic":
    pg.alert("Yeah, but in my opinion it is too fast drying")
    points +=3
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=mhnPW7jVAou2ggfZ66_QCA&q=acrylic+poaint&oq=acrylic+poaint&gs_l=img.3..0i10i24.1654.2417..2516...0.0..0.55.345.7......0....1..gws-wiz-img.......0j0i67.x2bAZCye5T4#imgrc=VpOlkz7siWhFhM:")
elif art == "pastel":
    pg.alert("I really like that but I don't have any at home")
    points +=5
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=-BnPW_KqKeKhggeOnLjIDg&q=pastel+chalk&oq=pastel+chalk&gs_l=img.3..0l10.6121.8483..8740...0.0..0.63.313.6......0....1..gws-wiz-img.......0i67.2QCmRgXF0Ao#imgrc=scJOFCDzxmgYTM:")
elif art == "watercolor":
    pg.alert("Yeshhhh I LOVE watercolor")
    points +=10
    t.sleep(.5)
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=681&bih=616&tbm=isch&sa=1&ei=RhrPW5SxLsPn_Qa9_ZOwCg&q=watercolor+tubes&oq=watercolor+tubes&gs_l=img.3..0l5j0i5i30l5.2126.2733..2857...0.0..0.71.326.6......0....1..gws-wiz-img.......0i67.a6NnBcOCOFs#imgrc=pZDXoFkvPMAW3M:")  
elif art == "i don't have one":
    pg.alert("okay that's fine")
    points +=1
    t.sleep(.5)
    wb.open("https://www.google.com/search?q=poof&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwivo9bbzpzeAhUFhuAKHRTZDDkQ_AUIDigB&biw=681&bih=616#imgrc=3uSMngUAJy5xVM:")
else:
    pg.alert("oh okay, I like something else though")


pg.alert ("You have scored: " + str(points))
favorite = pg.prompt ("Last question, do you like kittens?").lower()
if favorite == "yes":
    pg.alert ("great here's a random video!")
    t.sleep(.5)
    wb.open("https://www.youtube.com/watch?v=sYa-QqB5hHQ")
elif favorite == "no":
    pg.alert ("too bad here's a video anyways")
    t.sleep(.5)
    wb.open("https://www.youtube.com/watch?v=sYa-QqB5hHQ")
else:
    pg.alert ("oh well, here's a video anyways :)")
    t.sleep(.5)
    wb.open("https://www.youtube.com/watch?v=sYa-QqB5hHQ")
