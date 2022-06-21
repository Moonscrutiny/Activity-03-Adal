import math
import sys
from pickletools import read_int4
import time
import pokeStats_calc as calcStat
import pokeEV_calc as EVcalculator
from time import sleep

attnat = 1
defnat = 1
speatnat = 1
spdefnat = 1
spenat = 1 

print ("===================Choose which calculator to use!===================")
print ("[1] EV Calculator")
print ("[2] Stats Calculator")
answer = int(input("Answer: "))

#if the plans to use calculator for EV
if answer == 1:
    stat = ["ss", "Hp", "Attack", "Defense", "Special Attack", "Special Defense" , "Speed"]
    base = [6]
    iv = [6]
    ev = [0,0,0,0,0,0,0]
    evstat = 0
    level = int(input("Input the level of your pokemon: "))
    if(level<0 or level>100):
        print("Level Can only reach max 100!")
        sleep(1)
        exit()

    print("Input Base Stats")
    for x in range(1, 7):
        base.append(int(input("Input "+stat[x]+": ")))

    print("Input Iv's on each Stats")
    for y in range(1, 7):
        iv.append(int(input("Input "+stat[y]+" IV: ")))
        if (iv[y] < 0 or iv[y] > 31):
                print("You can only set Ivs from 0 to 31!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()
    print("===================Choosse an option!===================")
    print("[1]Single EV Stat\n[2]All of the Stats")
    k = int(input("Answer: "))
    if(k == 1):
        s = int(input("Which Stat would you like to input?\n[1]HP [2]Attack [3]Defense [4]Special Attack [5]Special defefesne [6]Speed\n"))
        tray = int(input("Input how much Ev: "))
        if (s < 0 or s > 255):
            print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
            sleep(3)
            print("System is closing!")
            sleep(3)                
            exit()
        for p in range(1,7):
            if (p==s):
                ev.insert(p, tray)
    elif(k == 2):        
        print("Input Ev's on each Stats")
        for z in range(1, 7):
            ev.append(int(input("Input "+stat[z]+" Ev: ")))
            if (ev[z] < 0 or ev[z] > 255):
                print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()
        evstat = evstat + ev[z]
        if (evstat > 510):
                print("You can only set Evs to a total of 510 Ev!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()    
    else:
        print("Invalid Input!"); exit()
        
    print("\n[1]hardy [2]lonely [3]brave [4]adamant [5]naughty\n"
          "[6]bold [7]docile [8]relaxed [9]impish [10]lax\n "
          "[11]timid [12]hasty [13]serious [14]jolly [15]naive\n "
          "[16]modest [17]mild [18]quiet [19]bashful [20]rash\n "
          "[21]calm [22]gentle [23]sassy [24]careful [25]quirky")

    nature = int(input("Pick Pokemon's Nature: "))
    if(nature == 1 or nature == 7 or nature == 13 or nature == 19 or nature == 25):
        attnat = 1
        defnat = 1
        speatnat = 1
        spdefnat = 1
        spenat = 1
    if(nature == 2 or nature == 3 or nature == 4 or nature == 5): 
        attnat = 1.1
        if(nature == 2):
            defnat = 0.9
        elif(nature == 3):
            spenat = 0.9
        elif(nature == 4):
            speatnat = 0.9
        else:
            spdefnat = 0.9
    if(nature == 6 or nature == 8 or nature == 9 or nature == 10):
        defnat = 1.1
        if(nature == 6):
            attnat = 0.9
        elif(nature == 8):
            spenat = 0.9
        elif(nature == 9):
            speatnat = 0.9
        else:
            spdefnat = 0.9
    if(nature == 11 or nature == 12 or nature == 14 or nature == 15):
        spenat = 1.1
        if(nature == 11):
            attnat = 0.9
        elif(nature == 12):
            defnat = 0.9
        elif(nature == 14):
            spenat = 0.9
        else:
            spdefnat = 0.9    
    if(nature == 16 or nature == 17 or nature == 18 or nature == 20):
        speatnat = 1.1
        if(nature == 16):
            attnat = 0.9
        elif(nature == 17):
            defnat = 0.9
        elif(nature == 18):
            spenat = 0.9
        else:
            spdefnat = 0.9      
    if(nature == 21 or nature == 22 or nature == 23 or nature == 24):
        spdefnat = 1.1
        if(nature == 16):
            attnat = 0.9
        elif(nature == 17):
            defnat = 0.9
        elif(nature == 18):
            spenat = 0.9
        else:
            speatnat = 0.9
    if(nature <= 0 or nature >=25):
        print("Invalid input!");exit()
   
    option = int(input("Which stat do you want to check?\n[1] Attack [2] Defense [3] Special Attack \n [4] Special Defense [5] Speed \n"))
    modify = 0
    if option == 1:
            modify = attnat
    elif option == 2:
            modify = defnat
    elif option == 3:
            modify = speatnat
    elif option == 4:
            modify = spdefnat
    elif option == 5:
            modify = spenat
    else:
        print("Invald input!"); exit()

    di = int(input("Enter desired increase: "))

    print("This is the amount of needed Ev for your pokemon: ", EVcalculator.EV.desired(base,ev,iv,option,level,di,modify)) 
    exit()
#When the user plans to usse calculator for stats
elif answer == 2:
    stat = ["ss", "Hp", "Attack", "Defense", "Special Attack", "Special Defense" , "Speed"]
    base = [6]
    iv = [6]
    ev = [0,0,0,0,0,0,0]
    evstat = 0
    pokemon = str(input("Enter Pokemon: "))
    level = int(input("Enter level: "))
    if(level<0 or level>100):
        print("Level Can only reach max 100!")
        sleep(1)
        exit()    
    print("[1]hardy [2]lonely [3]brave [4]adamant [5]naughty\n"
          "[6]bold [7]docile [8]relaxed [9]impish [10]lax\n "
          "[11]timid [12]hasty [13]serious [14]jolly [15]naive\n "
          "[16]modest [17]mild [18]quiet [19]bashful [20]rash\n "
          "[21]calm [22]gentle [23]sassy [24]careful [25]quirky")

    nature = int(input("Pick Pokemon's Nature: "))
    if(nature == 1 or nature == 7 or nature == 13 or nature == 19 or nature == 25):
        attnat = 1
        defnat = 1
        speatnat = 1
        spdefnat = 1
        spenat = 1
    if(nature == 2 or nature == 3 or nature == 4 or nature == 5): 
        attnat = 1.1
    if(nature == 2):
        defnat = 0.9
    elif(nature == 3):
        spenat = 0.9
    elif(nature == 4):
        speatnat = 0.9
    else:
        spdefnat = 0.9
    if(nature == 6 or nature == 8 or nature == 9 or nature == 10):
        defnat = 1.1
    if(nature == 6):
        attnat = 0.9
    elif(nature == 8):
        spenat = 0.9
    elif(nature == 9):
        speatnat = 0.9
    else:
        spdefnat = 0.9
    if(nature == 11 or nature == 12 or nature == 14 or nature == 15):
        spenat = 1.1
    if(nature == 11):
        attnat = 0.9
    elif(nature == 12):
        defnat = 0.9
    elif(nature == 14):
        spenat = 0.9
    else:
        spdefnat = 0.9    
    if(nature == 16 or nature == 17 or nature == 18 or nature == 20):
        speatnat = 1.1
    if(nature == 16):
        attnat = 0.9
    elif(nature == 17):
        defnat = 0.9
    elif(nature == 18):
        spenat = 0.9
    else:
        spdefnat = 0.9      
    if(nature == 21 or nature == 22 or nature == 23 or nature == 24):
        spdefnat = 1.1
    if(nature == 16):
        attnat = 0.9
    elif(nature == 17):
        defnat = 0.9
    elif(nature == 18):
        spenat = 0.9
    else:
        speatnat = 0.9

    print("Input Base Stats")
    for x in range(1, 7):
        base.append(int(input("Input "+stat[x]+": ")))

    print("Input Iv's on each Stats")
    for y in range(1, 7):
        iv.append(int(input("Input "+stat[y]+" Iv: ")))
        if (iv[y] < 0 or iv[y] > 31):
                print("You can only set Ivs from 0 to 31!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()

    k = int(input("Input for [1]Single Ev Stat or [2]All the stats?\n"))
    if(k == 1):
        s = int(input("Which Stat would you like to input?\n[1]HP [2]Att [3]Def [4]SpeA [5]Spdef [6]Spe\n"))
        tray = int(input("Input how much Ev: "))
        if (s < 0 or s > 255):
            print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
            sleep(3)
            print("System is closing!")
            sleep(3)                
            exit()
        for p in range(1,7):
            if (p==s):
                ev.insert(p, tray)
    elif(k == 2):        
        print("Input Ev's on each Stats")
        for z in range(1, 7):
            ev.append(int(input("Input "+stat[z]+" Ev: ")))
            if (ev[z] < 0 or ev[z] > 255):
                print("You can only set Evs from 0 to 255 and with a total of 510 Ev!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()
        evstat = evstat + ev[z]
        if (evstat > 510):
                print("You can only set Evs to a total of 510 Ev!")
                sleep(3)
                print("System is closing!")
                sleep(3)                
                exit()  
else:
    print("Invalid Input!")
    exit()
print("Here's the stats of your pokemon: ")
print("HP: ", calcStat.Status.hpReturn(base,iv,ev,level))
print("Attack: ", calcStat.Status.attackReturn(base,iv,ev,level,attnat))
print("Defense: ", calcStat.Status.defenseReturn(base,iv,ev,level,defnat))
print("Speocial Attack: ", calcStat.Status.spattackReturn(base,iv,ev,level,speatnat))
print("Special Defense: ", calcStat.Status.spdefenseReturn(base,iv,ev,level,spdefnat))
print("Speed: ", calcStat.Status.speedReturn(base,iv,ev,level,spenat))