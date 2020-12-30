import random
import time
import os
import datetime
import sys
import pygame
import get_sound as gs

print('\33]0;ANY% Text Adventure\a', end='', flush=True)

# Setters and getters for player
class Steve:
    def __init__(self, Shealth, Sattack, Stime, Sname):
        self.health = Shealth
        self.attack = Sattack
        self.time = Stime
        self.name = Sname
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getTime(self):
        return self.time
    def getName(self):
        return self.name
    
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setTime(self, newTime):
        self.time = newTime
    def setName(self, newName):
        self.name = newName

class Blaze:
    def __init__(self, Bhealth, Battack):
        self.health = Bhealth
        self.attack = Battack
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
        
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAtack):
        self.attack = newAttack

class Piglin:
    def __init__(self, Phealth, Pattack):
        self.health = Phealth
        self.attack = Pattack
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
        
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack

class Dragon:
    def __init__(self, Dhealth, Dattack):
        self.health = Dhealth
        self.attack = Dattack
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
        
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack

class Enderman:
    def __init__(self, Ehealth, Eattack):
        self.health = Ehealth
        self.attack = Eattack
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
        
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack

class Zombie:
    def __init__(self, Zhealth, Zattack):
        self.health = Zhealth
        self.attack = Zattack
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
        
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAtack):
        self.attack = newAttack

class Skeleton:
    def __init__(self, Shealth, Sattack):
        self.health = Shealth
        self.attack = Sattack
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
        
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAtack):
        self.attack = newAttack

class Creeper:
    def __init__(self, Chealth, Cattack):
        self.health = Chealth
        self.attack = Cattack
        
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
        
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAtack):
        self.attack = newAttack

def getRandom():
    return random.randint(0, 100)
        
def getTrade():
    loot_table = ['Ender Pearl', 'Crying Obsidian', 'Leather', 'Soul Sand', 'Nether Quartz', 'Iron Nuggets']
    trade = random.choice(loot_table)
    global Barter
    Barter += 1
    gs.piglinAdmire()
    time.sleep(1)
    
    if trade == 'Ender Pearl':
        global ePearls
        num = random.randint(4, 8)
        ePearls += num
        gs.piglinCelebrate()
        return (f'You received {num} Ender Pearls.\nYou now have {ePearls} Ender Pealrs.\nYou have {gold} gold remaining')
    # elif trade == 'Crying Obsidian':
        # global cObby
        # cObby += 1
        # return (f'You received {trade}.\nThis can be used for extra portal spins.\nYou have {gold} gold remaining')
    else:
        gs.piglinCelebrate()
        return (f'You got worthless {trade}.\nYou have {gold} gold remaining')
        
def setBase(steveName):
    global player
    global blaze
    global piglin
    global dragon
    global enderman
    global zombie
    global creeper
    global skeleton
    
    global ePearls
    global cObby
    global Barter
    global gold
    global gold_total
    global rods
    global att
    global attSH
    global eyes
    global powder
    global has_seen
    global has_seenOW
    global has_seenSH
    global has_seenE
    global has_found
    global has_foundPR
    global spawn
    global portal_fill
    global seed
    
    player = Steve(20, 1, 0, steveName)
    blaze = Blaze(15, 3)
    piglin = Piglin(16, 8)
    dragon = Dragon(200, 8)
    enderman = Enderman(40, 7)
    zombie = Zombie(20, 3)
    skeleton = Skeleton(20, 4)
    creeper = Creeper(20, 8)
    
    ePearls = 0
    cObby = 0
    Barter = 0
    gold = 0
    gold_total = 0
    rods = 0
    att = 7
    attSH = 7
    eyes = 0
    powder = 0
    has_seen = False
    has_seenOW = False
    has_seenSH = False
    has_seenE = False
    has_found = False
    has_foundPR = False
    spawn = False
    portal_fill = False
    seed = [random.random() < 0.1 for _ in range(12)].count(True)
    
    return player, blaze, piglin, dragon, enderman

def intro():
    print(f'''Welcome {player.getName()}!
The year was 2020, the world was in the midst of the worst 
pandemic ever before seen. In order to save the human race, you
volunteer to freeze yourself for the next 500 years.
While you were frozen, a tear occured in the fabric of myth and reality
allowing a flood of evil mythical creatures to enter our world.
Over the last 500 years the mythical creatures have taken over,
and now rule all. Your quest, should you accept, is to escape
the Nether with the tools needed to locate and activate the
End Portal and to kill the evil Ender Dragon that rules
over all of us, thus restoring the world and saving humanity.
    ''')
    
    while True:
        ans = input('Do you accept this quest?(yes|no): ').lower().strip(' ')
        if ans == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            gear()
            break
        elif ans == 'no':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('OK')
            time.sleep(2)
            print('Goodbye')
            time.sleep(1)
            exit()
        else:
            print('Invalid Response, please try again')

def gear():
    global bed
    bed = random.randint(3, 12)
    print(f'''Oh bless you {player.getName()}!
Before you begin your quest, here is a loot crate
of stuff to help you on your journey.
    ''')
    
    input('Press Enter to open your loot chest: ')
    
    weapon = {
    'Wooden Sword': 4,
    'Stone Sword': 5,
    'Iron Sword': 6,
    'Diamond Sword': 7,
    'Stone Axe': 9
    }
    global weapon_roll
    weapon_roll = random.choice(list(weapon))
    
    armor = {
    'Leather Armor': 6,
    'Iron Armor': 8,
    'Diamond Armor': 14
    }
    global armor_roll
    armor_roll = random.choice(list(armor))
    weapon_value = weapon.get(weapon_roll)
    armor_value = armor.get(armor_roll)
    player.setAttack(weapon_value)
    health = player.getHealth() + armor_value
    player.setHealth(health)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f'''Inside the loot chest you find one {weapon_roll}, boosting your attack value to {player.getAttack()}.
You also find a set of {armor_roll}, boosting your health to {player.getHealth()}.
Here, also take these {bed} beds. They will be handy when you fight the Ender Dragon.
    ''')
    
    time.sleep(0.5)
    input('Press Enter to continue your quest: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''You are in a vast Nether waste.
Here you must search for the items needed to craft Eye's of Ender.
The Eye's are used to locate and active the End Portal. This is 
how you will travel to the End, where you must defeat the Ender Dragon.

To craft the Eye's of Ender, you'll need 2 things, Blaze powder and
ender pearls. Ender pearls can be gotten from Piglins. They barter
gold for items they have. You do not have a say in what you get for
your gold, so it might take a while to collect enough Ender Pearls
to complete the End Portal. You will need up to 12 Ender Pealrs to 
complete the Portal. But, watch out, as they can break on the way
to the portal.

Braze powder can be crafted from Blaze rods. Blaze rods are dropped from
the blaze demons located in the Nether Fortress.
One Blaze rod crafts 2 blaze powder.

Once you have enough Eye's, you must travel to the Overworld where the 
End Portal is located. Rumor has it that there is an old ruined portal
to the overworld close by. There should be enough supplies to complete
the portal. Use this portal to get to the Overworld.
{player.getName()}, you are our only hope! May you defeat the Ender Dragon
swiftly!
 ''')
    
    input('Press Enter to continue: ')
    nether()
    
def nether():
    global gold
    global gold_total
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('Welcome to the Nether! Please make a choice')
        print('(1) Search for gold\n(2) Search for a Piglin\n(3) Search for a Fortress\n(4) Search for portal to Overworld')
        print("Or you can type in 'stats', 'reset', or 'quit'")
        ans = input('--> ')
        ans = ans.lower().strip(' ')
        if ans == '1':
            pause = random.randint(1, 5)
            print('Prospecting...')
            time.sleep(pause)
            ore = random.randint(1, 4)
            if getRandom() <= 65:
                gold += ore
                gold_total += ore
                gs.oreBreak()
                print(f'You were able to collet {ore} gold!\nYou now have a total of {gold} gold!')
                input('Press Enter to continue: ')
            else:
                gs.oreMiss()
                print('You did not find any gold.')
                input('Press Enter to continue: ')
                
            
        elif ans == '2':
            pause = random.randint(1, 5)
            print('Searching for piglins...')
            time.sleep(pause)
            if getRandom() <= 75:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('You have found a piglin! What would you like to do?')
                    print('(1) Barter\n(2) Fight\n(3) Back to previous')
                    print("Or you can type in 'stats', 'reset', or 'quit'")
                    ans = input('--> ')
                    ans = ans.lower().strip(' ')
                    
                    if ans == '1':
                        if gold == 0:
                            print("You don't have any gold!")
                            input('Press Enter to continue: ')
                            pass
                        else:
                            gold -= 1
                            pause = random.randint(1, 5)
                            print('Piglin: Thinking...')
                            time.sleep(pause)
                            print(getTrade())
                            input('Press Enter to continue: ')
                    elif ans == '2':
                        piglinFight()
                        
                    elif ans == '3':
                        piglin.setHealth(16)
                        break
                        
                    elif ans == 'stats':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        etime = time.time() - stime
                        player.setTime(etime)
                        print(vars(player))
                        print(f"You have {rods} blaze rods, {ePearls} Ender Pearls, {eyes} Eye's of Ender, {powder} Blaze Powder and {bed} beds")
                        input('Press Enter to continue: ')
                        
                    elif ans == 'reset':
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            ans = input('Are you sure? (yes|no): ')
                            ans = ans.lower().strip(' ')
                            if ans == 'yes':
                                os.system('cls' if os.name == 'nt' else 'clear')
                                main()
                            elif ans == 'no':
                                break
                            else:
                                print('Invalid Response')
                                input('Press Enter to continue: ')
                            
                    elif ans == 'quit':
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            ans = input('Are you sure? (yes|no): ')
                            ans = ans.lower().strip(' ')
                            if ans == 'yes':
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print('Thanks for playing!')
                                time.sleep(1)
                                exit()
                            elif ans == 'no':
                                break
                            else:
                                print('Invalid Response')
                                input('Press Enter to continue: ')
                                    
                    else:
                        print('Invalid Responce')
                        input('Press Enter to continue: ')
                        
            else:
                print('You did not find any piglins. Please try again')
                input('Press Enter to continue: ')
                
        elif ans == '3':
            print('Searching for Fortress...')
            pause = random.randint(1, 5)
            time.sleep(pause)
            if getRandom() <= 20:
                fortress()
            else:
                print('lol, get fucked!\nNo fortress here.')
                input('Press Enter to continue: ')
        
        elif ans == '4':
            findPortal()
        
        elif ans == 'stats':
            os.system('cls' if os.name == 'nt' else 'clear')
            etime = time.time() - stime
            player.setTime(etime)
            print(vars(player))
            print(f"You have {rods} blaze rods, {ePearls} Ender Pearls, {eyes} Eye's of Ender, {powder} Blaze Powder and {bed} beds")
            input('Press Enter to continue: ')
            
        elif ans == 'reset':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
                
        elif ans == 'quit':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thanks for playing!')
                    time.sleep(1)
                    exit()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
                    
        else:
            print('Invalid Response')
            input('Press Enter to continue: ')

def overWorldStory():
    os.system('cls' if os.name == 'nt' else 'clear')
    global has_seenOW
    if has_seenOW == False:
        print(f'''You emerge from the portal. It is much different than the Nether here.
It's bright and suny, instead of dark and hot. 

From here you have access to the crafting bench, and can craft the
Eye's of Ender, needed to find the Stronghold, and activate the End Portal.
The Stronoghold is rumored to be a fair few thousand blocks from here,
so good luck {player.getName()}, you're going to need it.     
        ''')
        input('Press Enter to continue: ')
        has_seenOW = True
        overWorld()
    else:
        overWorld()
        
def overWorld():
    ranMob()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Welcome to the Overworld! What would you like to do?')
        if has_found == False:
            print("(1) Search for Stronghold\n(2) Craft Eye's of Ender\n(3) Back to Previous")
        else:
            print("(1) Enter Stronghold\n(2) Craft Eye's of Ender\n(3) Back to Previous")
        print("Or you can type in 'stats', 'reset', or 'quit'")
        ans = input('--> ')
        ans = ans.lower().strip(' ')
        
        if ans == '1':
            locateStronghold()
            
        elif ans == '2':
            crafting() 
            
        elif ans == '3':
            break
            
        elif ans == 'stats':
            os.system('cls' if os.name == 'nt' else 'clear')
            etime = time.time() - stime
            player.setTime(etime)
            print(vars(player))
            print(f"You have {rods} blaze rods, {ePearls} Ender Pearls, {eyes} Eye's of Ender, {powder} Blaze Powder and {bed} beds")
            input('Press Enter to continue: ')
            
        elif ans == 'reset':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
                
        elif ans == 'quit':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thanks for playing!')
                    time.sleep(1)
                    exit()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
        
        else:
            print('Invalid Response')
            input('Press Enter to continue: ')

def end():
    global has_seenE
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if has_seenE == False:
            print(f'''{player.getName()}, you have made it to the End!
All you must do now is defeat the evil Dragon! The beds you have are quite
exploseive here. Use them to kill the dragon.
            ''')
            has_seenE = True
            input('Press Enter to continue: ')
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Welcome to the End! What would you like to do?')
        print("(1) Fight Dragon\n(2) Back to Previous")
        print("Or you can type in 'stats', 'reset', or 'quit'")
        ans = input('--> ')
        ans = ans.lower().strip(' ')
        
        if ans == '1':
            dragonFight()
            
        elif ans == '2':
            print('No problem! Just defeat the Dragon, and you will be on your way!')
            input('Press Enter to continue: ')
            
        elif ans == 'stats':
            os.system('cls' if os.name == 'nt' else 'clear')
            etime = time.time() - stime
            player.setTime(etime)
            print(vars(player))
            print(f"You have {rods} blaze rods, {ePearls} Ender Pearls, {eyes} Eye's of Ender, {powder} Blaze Powder and {bed} beds")
            input('Press Enter to continue: ')
            
        elif ans == 'reset':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
                
        elif ans == 'quit':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thanks for playing!')
                    time.sleep(1)
                    exit()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
        
        else:
            print('Invalid Response')
            input('Press Enter to continue: ')
        
def winner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    try:
        with open("end.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line.replace('PLAYERNAME', player.getName()))
                time.sleep(0.75)
            f.close()
            input('Press Enter to continue: ')
            winnerFinal()
    except KeyboardInterrupt:
        winnerFinal()
        
def winnerFinal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''Congratulations {player.getName()}!
You have defeated to mighty and evil Ender Dragon!
Because of your brave actions, the world can go back to normal now.        
    
    
    ''')
    ftime = str(datetime.timedelta(seconds=player.getTime()))
    print(f'NAME: {player.getName()}\nTIME: {ftime}')
    print('\n\nPlease share this screen with tuxprint#5176 on Discord\nAlso please report any bugs or suggestions to tuxprint#5176')
    input('Press Enter to continue: ')
    
    while True:
        ans = input('Would you like to play again? (yes|no)')
        ans = ans.lower().strip(' ')
        if ans == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif ans == 'no':
            print('Thanks for playing!')
            time.sleep(2)
            exit()
            
def crafting():
    global rods
    global ePearls
    global powder
    global eyes
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Welcome to the Crafting Bench! What would you like to do?')
        print("(1) Craft eyes\n(2) Craft Blaze Powder\n(3) Back to Previous")
        print("Or you can type in 'stats', 'reset', or 'quit'")
        ans = input('--> ')
        ans = ans.lower().strip(' ')
        
        if ans == '1':
            if powder == 0 and ePearls == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('You do not have any supplies for crafting.')
                input('Press Enter to continue: ')
                break
            elif powder == ePearls:
                ePearls = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"You were able to craft {powder} Eye's of Ender.")
                eyes = powder
                powder = 0
                print(f"You have {powder} blaze powder and {ePearls} Ender Pearls remaining.'")
                input('Press Enter to continue: ')
                break
            elif powder < ePearls:
                ePearls -= powder
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"You were able to craft {powder} Eye's of Ender.")
                eyes += powder
                powder = 0
                print(f"You have {powder} blaze powder and {ePearls} Ender Pearls remaining.'")
                input('Press Enter to continue: ')
                break
            elif powder > ePearls:
                powder -= ePearls
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"You were able to craft {ePearls} Eye's of Ender.")
                eyes += ePearls
                ePearls = 0
                print(f"You have {powder} blaze powder and {ePearls} Ender Pearls remaining.'")
                input('Press Enter to continue: ')
                break
                
        elif ans == '2':
            if rods == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('You do not have any blaze rods')
                input('Press Enter to continue: ')
                break
                
            else:
                powder += rods * 2
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'You crafted {powder} blaze powder from {rods} rods')
                rods = 0
                input('Press Enter to continue: ')
                pass 
             
        elif ans == '3':
            break
            
        elif ans == 'stats':
            os.system('cls' if os.name == 'nt' else 'clear')
            etime = time.time() - stime
            player.setTime(etime)
            print(vars(player))
            print(f"You have {rods} blaze rods, {ePearls} Ender Pearls, {eyes} Eye's of Ender, {powder} Blaze Powder and {bed} beds")
            input('Press Enter to continue: ')
            
        elif ans == 'reset':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
                
        elif ans == 'quit':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thanks for playing!')
                    time.sleep(1)
                    exit()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
        
        else:
            print('Invalid Response')
            input('Press Enter to continue: ')
        

def locateStronghold():
    global has_found
    global eyes
    os.system('cls' if os.name == 'nt' else 'clear')
    if has_found == False:
        while True:
            if has_found == True:
                break
            os.system('cls' if os.name == 'nt' else 'clear')
            ranMob()
            if eyes == 0:
                print("You do not have any Eye's of Ender.\nPlease try again when you have crafted the eyes.")
                input('Press Enter to continue: ')
                break
            else:
                gs.eyeThrow()
                print('You throw an eye...')
                time.sleep(2)
                broken = False
                dist = random.randint(1400, 2100)
                pause = dist * 0.01
                direction = random.choice(['North', 'South', 'East', 'West'])
                if getRandom() <= 20:
                    broken = True
                    eyes -= 1
                if getRandom() <= 33:
                    if broken == True:
                        gs.eyeBreak()
                        print(f'It goes to the {direction}...\nYour eye breaks!\nLeaving you with {eyes} eyes left.\nYou follow the eye to the {direction} for {dist} blocks.')
                        print('Traveling...')
                        time.sleep(pause)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('You have found the Stronghold!')
                        has_found = True
                        input('Press Enter to continue: ')
                        stronghold()
                        
                    else:
                        print(f'It goes to the {direction}...\nYou are able to recover the eye. You stil have {eyes} eyes remaining.\nYou follow the eye to the {direction} for {dist} blocks.')
                        print('Traveling...')
                        time.sleep(pause)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('You have found the Stronghold!')
                        has_found = True
                        input('Press Enter to continue: ')
                        stronghold()
                
                else:
                    if broken == True:
                        gs.eyeBreak()
                        print(f'It goes to the {direction}...\nYour eye breaks!\nLeaving you with {eyes} eyes left.\nYou follow the eye to the {direction} for {dist} blocks.')
                        print('Traveling...')
                        time.sleep(pause)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('You have failed to find the Stronghold')
                        input('Press Enter to throw another eye: ')
                        pass
                            
                    else:
                        print(f'It goes to the {direction}...\nYou are able to recover the eye. You still have {eyes} eyes remaining.\nYou follow the eye to the {direction} for {dist} blocks.')
                        print('Traveling...')
                        time.sleep(pause)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('You have failed to find the Stronghold')
                        input('Press Enter to throw another eye: ')
                        pass
    else:
        stronghold()

def stronghold():
    global has_seenSH
    global has_foundPR
    ranMob()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if has_seenSH == False:
            print(f'''Welcome to the Strondhold, {player.getName()}!
Deep within this long abanded Stronhold, is the End Portal. You will
need to navigate,  in the dark, to find the portal room. Over the centuries
earthquacks have caused great revines to tear their way through the 
Stronghold. Also abandoned mineshafts are littered throughout the area.
Locating the portal rool will be a mighty task.
Once you locate the portal room, you will be able to activate the portal,
and travel to the End. You will be able to search the Stronghold further
for loot.
            ''')
            
            input('Press Enter to continue: ')
            
            while True:
                pause = random.randint(5, 15)
                if getRandom() <= 27:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ranMob()
                    print(f'You stumble through the dark, finding seemingly endless dead ends.')
                    print('Searching...')
                    time.sleep(pause)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('You have found the Portal Room!')
                    input('Press Enter to continue: ')
                    has_seenSH = True
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ranMob()
                    print(f'You stumble through the dark, finding seemingly endless dead ends.')
                    print('Searching...')
                    time.sleep(pause)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('You were not able to locate the Portal Room')
                    input('Press Enter to look again: ')
                    pass
                
        else:
            global spawn
            global bed
            if has_foundPR == False:
                print(f'''This is it {player.getName()}, the End Portal Room.
This seed is a {seed} eye!

From here you can activate the portal for entering the End. Once you enter the End
your health will be boosted back to full, but the End is a verry dangerous place. If you die there
it is game over. That is why it is a good idea to place a bed here to set your spawn.
You have {bed} beds.''')
            
                
                while True:
                    ans = input('Would you like to place a bed here? (yes|no): ')
                    ans = ans.lower().strip(' ')
                    if ans == 'yes':
                        bed -= 1
                        spawn = True
                        print(f'You will now respawn here in case of death in the End\nYou have {bed} beds remaining.')
                        input('Press Enter to continue: ')
                        has_foundPR = True
                        break
                    elif ans == 'no':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        ans = input('Are you sure? (yes|no): ')
                        ans = ans.lower().strip(' ')
                        if ans == 'yes':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('You will not respawn on death.')
                            input('Press Enter to continue: ')
                            has_foundPR = True
                            break
                        elif ans == 'no':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            pass
                        else:
                            print('Invalid Response')
                            input('Press Enter to continue: ')
                    else:
                        print('Invalid Response')
                        input('Press Enter to continue: ')
        
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Welcome to the End Portal Room! What would you like to do?')
            print("(1) Enter End\n(2) Complete Portal\n(3) Search for loot\n(4) Back to Previous")
            print("Or you can type in 'stats', 'reset', or 'quit'")
            ans = input('--> ')
            ans = ans.lower().strip(' ')
            
            if ans == '1':
                if portal_fill == False:
                    print('Please activate the portal first.')
                    input('Press Enter to continue: ')
                    pass
                else:
                    if player.getHealth() < 20:
                        player.setHealth(20)
                    end()
            elif ans == '2':
                portal()
            elif ans == '3':
                strongholdLoot()
            elif ans == '4':
                break
                
            elif ans == 'stats':
                os.system('cls' if os.name == 'nt' else 'clear')
                etime = time.time() - stime
                player.setTime(etime)
                print(vars(player))
                print(f"You have {rods} blaze rods, {ePearls} Ender Pearls, {eyes} Eye's of Ender, {powder} Blaze Powder and {bed} beds")
                input('Press Enter to continue: ')
                
            elif ans == 'reset':
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ans = input('Are you sure? (yes|no): ')
                    ans = ans.lower().strip(' ')
                    if ans == 'yes':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        main()
                    elif ans == 'no':
                        break
                    else:
                        print('Invalid Response')
                        input('Press Enter to continue: ')
                    
            elif ans == 'quit':
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ans = input('Are you sure? (yes|no): ')
                    ans = ans.lower().strip(' ')
                    if ans == 'yes':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Thanks for playing!')
                        time.sleep(1)
                        exit()
                    elif ans == 'no':
                        break
                    else:
                        print('Invalid Response')
                        input('Press Enter to continue: ')
                        
            else:
               print('Invalid Response')
               input('Press Enter to continue: ') 
    
    os.system('cls' if os.name == 'nt' else 'clear')

def portal():
    global portal_fill
    global eyes
    os.system('cls' if os.name == 'nt' else 'clear')
    if portal_fill == False:
        need = 12 - seed
        if need > eyes:
            need_eyes = need - eyes
            print(f'This seed is a {seed} eye.')
            print(f'{need} eyes are requird to complete the portal.\nYou only have {eyes} eyes.\nYou need {need_eyes} more eyes.')
            input('Press Enter to continue: ')
        else:
            print(f'This seed is a {seed} eye.')
            print(f'You were able to place {need} eyes in the portal activating it!')
            input('Press Enter to continue: ')
            eyes -= need
            portal_fill = True
    else:
        print(f'This seed is a {seed} eye.')
        print('This portal has already been activated.')
        input('Press Enter to continue: ')
    
def piglinFight():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if getRandom() <= 70:
            print(f'You swung your {weapon_roll}, striking the piglin for {player.getAttack()} points of damage!')
            gs.piglinHurt()
            pigHealth = piglin.getHealth()
            playerAttack = player.getAttack()
            dmg_delt = pigHealth - playerAttack
            piglin.setHealth(dmg_delt)
            if dmg_delt < 1:
                gs.piglinDeath()
                print('You have defeated the piglin!\nThere were no drops.')
                piglin.setHealth(16)
                input('Press Enter to continue: ')
                break
            else:
                print(f'The piglin has {dmg_delt} health left.')
        else:
            gs.mobMiss()
            print(f'You swung your {weapon_roll} at the piglin, but it is a miss!')
            
        time.sleep(1)
        
        if getRandom() <= 62:
            print(f'The piglin has attacked you, dealing {piglin.getAttack()} damage!')
            gs.playerDamage()
            playerHealth = player.getHealth()
            pigAttack = piglin.getAttack()
            dmg_delt = playerHealth - pigAttack
            player.setHealth(dmg_delt)
            
            if dmg_delt < 1:
                if spawn == True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'You have Died!')
                    input('Press Enter to respawn.')
                    player.setHealth(20)
                    stronghold()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('You have Died! GAME OVER!!!')
                    input('Press Enter to Reset: ')
                    main()
            else:
                gs.playerDamage()
                print(f'You have {dmg_delt} health remaining')
                input('Press Enter to continue: ')
                
        else:
            gs.mobMiss()
            print('The piglin has missed their attack!')
            input('Press Enter to continue: ')
    nether()
        
def blazeFight():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if getRandom() <= 70:
            print(f'You swung your {weapon_roll}, striking the blaze for {player.getAttack()} points of damage!')
            gs.blazeHurt()
            blaze_health = blaze.getHealth()
            playerAttack = player.getAttack()
            dmg_delt = blaze_health - playerAttack
            blaze.setHealth(dmg_delt)
            if dmg_delt < 1:
                global rods
                rods_chnc = random.randint(0, 1)
                gs.blazeDeath()
                print('You have defeated the blaze!')
                if rods_chnc == 1:
                    rods += 1
                    print('The blaze has dropped a blaze rod!')
                    print(f'You have a total of {rods} blaze rods')
                else:
                    print('There where no drops')
                    print(f'You have a total of {rods} blaze rods')
                blaze.setHealth(16)
                if player.getHealth() < 20:
                    diff = 20 - player.getHealth()
                    print('Your health has been topped up to 20')
                    player.setHealth(20)
                input('Press Enter to continue: ')
                break
                
            else:
                print(f'The blaze has {dmg_delt} health left.')
        else:
            gs.mobMiss()
            print(f'You swung your {weapon_roll} at the blaze, but it is a miss!')
            
        time.sleep(1)
        atype = random.choice(['Fire Ball', 'Melee'])
        
        if getRandom() <= 55:
            if atype == 'Melee':
                print(f'The blaze has melee attacked you, dealing {blaze.getAttack()} damage!')
                gs.playerDamage()
                playerHealth = player.getHealth()
                blazeAttack = blaze.getAttack()
                dmg_delt = playerHealth - blazeAttack
                player.setHealth(dmg_delt)
                
                if dmg_delt < 1:
                    if spawn == True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'You have Died!')
                        input('Press Enter to respawn.')
                        player.setHealth(20)
                        stronghold()
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('You have Died! GAME OVER!!!')
                        input('Press Enter to Reset: ')
                        main()
                    
                else:
                    print(f'You have {dmg_delt} health remaining')
                    input('Press Enter to continue: ')
            
            elif atype == 'Fire Ball':
                stun = random.randint(1, 5)
                dmg = random.randint(1, 7)
                playerHealth = player.getHealth()
                dmg_delt = playerHealth - dmg
                player.setHealth(dmg_delt)
                gs.playerDamage()
                print(f'The blaze has shot you with fire, dealing {dmg} damage!')
                gs.playerFire()
                
                if dmg_delt < 1:
                    print(f'You have died\nGame over, please try again.')
                    input('Press Enter to continue: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main()
                else:
                    print(f'The fire ball has stunned you for {stun} seconds, leaving you with {player.getHealth()} health')
                    time.sleep(stun)
                    input('Press Enter to continue: ')
                
                
        else:
            gs.mobMiss()
            print(f'The blaze has missed their {atype} attack!')
            input('Press Enter to continue: ')

def dragonFight():
    global bed
    os.system('cls' if os.name == 'nt' else 'clear')
    gs.dragonGrowl()
    print('Waiting for the Dragon to perch...')
    time.sleep(random.randint(1,5))
    count = 0
    perch_time = random.randint(3, 7)
    # Perch chance
    if getRandom() <= 40:
        while True:
            count += 1
            if count == perch_time:
                os.system('cls' if os.name == 'nt' else 'clear')
                gs.dragonWing()
                time.sleep(0.5)
                gs.dragonWing()
                time.sleep(0.5)
                gs.dragonWing()
                time.sleep(0.5)
                gs.dragonWing()
                print('The dragon has flown off! Wait for her to perch again.')
                input('Press Enter to continue.')
                break
                
            # Enderman Attack chance
            if getRandom() <= 10:
                os.system('cls' if os.name == 'nt' else 'clear')
                gs.endermanScream()
                time.sleep(0.5)
                gs.playerDamage()
                time.sleep(0.5)
                gs.endermanHurt()
                print(f'Oh no! You looked at an Enderman!\nYou punch him in the chest to deagro, but not before taking {enderman.getAttack()} damage!')
                newHealth = player.getHealth() - enderman.getAttack()
                if newHealth < 1:
                    if spawn == True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'You have Died!')
                        input('Press Enter to respawn.')
                        player.setHealth(20)
                        stronghold()
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('You have Died! GAME OVER!!!')
                        input('Press Enter to Reset: ')
                        main()
                else:
                    print(f'You have {player.getHealth()} health remaining.')
                player.setHealth(newHealth)
                input('Press Enter to continue: ')
                os.system('cls' if os.name == 'nt' else 'clear')
                break

        
            #player hit chance
            elif getRandom() <= 75:
                if bed > 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    bed_dmg = random.randint(5, 55)
                    gs.playerExplode()
                    print(f'You place a bed down and with stunning accuracy,\nyou BLAST the Dragon, dealing {bed_dmg} damage.')
                    bed -= 1
                    newDHealth = dragon.getHealth() - bed_dmg
                    dragon.setHealth(newDHealth)
                    
                    if dragon.getHealth() < 1:
                        print(f'The Dragons health is 0')
                        ntime = time.time() - stime
                        player.setTime(ntime)
                        gs.dragonDeath()
                        time.sleep(13)
                        input('Press Enter to continue: ')
                        winner()
                    else:
                        print(f'The Dragons health is {newDHealth}')
                elif bed <= 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    gs.dragonHurt()
                    print(f'You swing your {weapon_roll},\nStriking the Dragon, dealing {player.getAttack()} damage.')
                    bed -= 1
                    newDHealth = dragon.getHealth() - player.getAttack()
                    dragon.setHealth(newDHealth)
                    
                    if dragon.getHealth() < 1:
                        print(f'The Dragons health is 0')
                        ntime = time.time() - stime
                        player.setTime(ntime)
                        gs.dragonDeath()
                        time.sleep(13)
                        input('Press Enter to continue: ')
                        winner()
                    else:
                        print(f'The Dragons health is {newDHealth}')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'You missed your chance to get a hit in on the Dragon!')
                
            time.sleep(1)
            atype = random.choice(['Yeet', 'Melee'])
            #dragon hit chance
            if getRandom() <= 15:
                if atype == 'Melee':
                    gs.playerDamage()
                    print(f'The Dragon has melee attacked you, dealing {dragon.getAttack()} damage!')
                    playerHealth = player.getHealth()
                    dragonAttack = dragon.getAttack()
                    dmg_delt = playerHealth - dragonAttack
                    player.setHealth(dmg_delt)
                    
                    if dmg_delt < 1:
                        if spawn == True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'You have Died!')
                            input('Press Enter to respawn.')
                            player.setHealth(20)
                            stronghold()
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('You have Died! GAME OVER!!!')
                            input('Press Enter to Reset: ')
                            main()
                    print(f'You have {player.getHealth()} health remaining.')
                    input('Press Enter to continue: ')
                
                elif atype == 'Yeet':
                    stun = random.randint(1, 5)
                    dmg = random.randint(5, 10)
                    playerHealth = player.getHealth()
                    dmg_delt = playerHealth - dmg
                    player.setHealth(dmg_delt)
                    gs.playerFall()
                    print(f'The Dragon has yeeted you in the air, causing you to take {dmg} fall damage!')
                    
                    if dmg_delt < 1:
                        if spawn == True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'You have Died!')
                            input('Press Enter to respawn.')
                            player.setHealth(20)
                            stronghold()
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('You have Died! GAME OVER!!!')
                            input('Press Enter to Reset: ')
                            main()
                    print(f'You have {player.getHealth()} health remaining.')
                    input('Press Enter to continue: ')
                    
                    
            else:
                print(f'The Dragon has missed their {atype} attack!')
                input('Press Enter to continue: ')
            
    else:
        print('The Dragon did not perch this time.')
        input('Press Enter to continue: ')

def ranMob():
    if getRandom() <= 20:
        mob = random.choice(['Zombie', 'Creeper', 'Skeleton'])
        print(f'Oh no! You have been atacked by a {mob}!')
        if mob == 'Zombie':
            gs.zombieSay()
        elif mob == 'Skeleton':
            gs.skeletonSay()
        elif mob == 'Creeper':
            gs.creeperSay()
        input(f'Press Enter to fight the {mob}')
        while True:
            if mob == 'Zombie':
                if getRandom() <= 80:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'You swing your {weapon_roll}, striking {mob} causing {player.getAttack()} damage!')
                    newHealth = zombie.getHealth() - player.getAttack()
                    if newHealth < 1:
                        print(f'You have defeated {mob}!')
                        gs.zombieDeath()
                        if player.getHealth() < 20:
                            player.setHealth(20)
                            print('Your health has been topped up to 20')
                        input('Press Enter to continue: ')
                        os.system('cls' if os.name == 'nt' else 'clear')
                        zombie.setHealth(20)
                        break
                    gs.zombieHurt()
                    zombie.setHealth(newHealth)
                    print(f'The {mob} has {zombie.getHealth()} health remaining.')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    gs.mobMiss()
                    print(f'You have missed your attack on the {mob}!')
                        
            elif mob == 'Skeleton':
                if getRandom() <= 80:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'You swing your {weapon_roll}, striking {mob} causing {player.getAttack()} damage!')
                    newHealth = skeleton.getHealth() - player.getAttack()
                    if newHealth < 1:
                        print(f'You have defeated {mob}!')
                        gs.skeletonDeath()
                        if player.getHealth() < 20:
                            player.setHealth(20)
                            print('Your health has been topped up to 20')
                        input('Press Enter to continue: ')
                        os.system('cls' if os.name == 'nt' else 'clear')
                        skeleton.setHealth(20)
                        break
                    gs.skeletonHurt()
                    skeleton.setHealth(newHealth)
                    print(f'The {mob} has {skeleton.getHealth()} health remaining.')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    gs.mobMiss()
                    print(f'You have missed your attack on the {mob}!')
                        
            elif mob == 'Creeper':
                if getRandom() <= 80:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'You swing your {weapon_roll}, striking {mob} causing {player.getAttack()} damage!')
                    newHealth = creeper.getHealth() - player.getAttack()
                    if newHealth < 1:
                        print(f'You have defeated {mob}!')
                        gs.creeperDeath()
                        if player.getHealth() < 20:
                            player.setHealth(20)
                            print('Your health has been topped up to 20')
                        input('Press Enter to continue: ')
                        os.system('cls' if os.name == 'nt' else 'clear')
                        creeper.setHealth(20)
                        break
                    gs.creeperSay()
                    creeper.setHealth(newHealth)
                    print(f'The {mob} has {creeper.getHealth()} health remaining.')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    gs.mobMiss()
                    print(f'You have missed your attack on the {mob}!')
                        
            time.sleep(1)
            
            if getRandom() <= 62:
                if mob == 'Zombie':
                    gs.playerDamage()
                    print(f'The {mob} has attacked, causing {zombie.getAttack()} damage!')
                    newHealth = player.getHealth() - zombie.getAttack()
                    
                    if newHealth < 1:
                        if spawn == True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'You have Died!')
                            input('Press Enter to respawn.')
                            player.setHealth(20)
                            stronghold()
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('You have Died! GAME OVER!!!')
                            input('Press Enter to Reset: ')
                            main()
                    else:
                        player.setHealth(newHealth)
                        print(f'You have {player.getHealth()} health remaining')
                        input('Press Enter to continue: ')
                        
                if mob == 'Skeleton':
                    print(f'The {mob} has attacked, causing {skeleton.getAttack()} damage!')
                    gs.playerDamage()
                    newHealth = player.getHealth() - skeleton.getAttack()
                    
                    if newHealth < 1:
                        if spawn == True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'You have Died!')
                            input('Press Enter to respawn.')
                            player.setHealth(20)
                            stronghold()
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('You have Died! GAME OVER!!!')
                            input('Press Enter to Reset: ')
                            main()
                    else:
                        player.setHealth(newHealth)
                        print(f'You have {player.getHealth()} health remaining')
                        input('Press Enter to continue: ')
                
                if mob == 'Creeper':
                    gs.playerDamage()
                    print(f'The {mob} has attacked, causing {creeper.getAttack()} damage!')
                    newHealth = player.getHealth() - creeper.getAttack()
                    
                    if newHealth < 1:
                        if spawn == True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'You have Died!')
                            input('Press Enter to respawn.')
                            player.setHealth(20)
                            stronghold()
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('You have Died! GAME OVER!!!')
                            input('Press Enter to Reset: ')
                            main()
                    else:
                        player.setHealth(newHealth)
                        print(f'You have {player.getHealth()} health remaining')
                        input('Press Enter to continue: ')
                    
            else:
                print(f'The {mob} has missed their attack!')
                gs.mobMiss()
                input('Press Enter to continue: ')
                
                    
                
         
def fortress():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('You have found a fortress! What would you like to do?')
        print('(1) Fight Blaze\n(2) Search for loot\n(3) Back to previous')
        print("Or you can type in 'stats', 'reset', or 'quit'")
        ans = input('--> ')
        ans = ans.lower().strip(' ')
        
        if ans == '1':
            blazeFight()
            
        elif ans == '2':
            fortressLoot()
        
        elif ans == '3':
            blaze.setHealth(20)
            break
            
        elif ans == 'stats':
            os.system('cls' if os.name == 'nt' else 'clear')
            etime = time.time() - stime
            player.setTime(etime)
            print(vars(player))
            print(f"You have {rods} blaze rods, {ePearls} Ender Pearls, {eyes} Eye's of Ender, {powder} Blaze Powder and {bed} beds")
            input('Press Enter to continue: ')
            
        elif ans == 'reset':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
                
        elif ans == 'quit':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thanks for playing!')
                    time.sleep(1)
                    exit()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
        
        else:
            print('Invalid Response')
            input('Press Enter to continue: ')
    

def ruinedPortal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Welcome to the Ruined Portal! What would you like to do?')
        print('(1) Travel to Overworld\n(2) Back to previous')
        print("Or you can type in 'stats', 'reset', or 'quit'")
        ans = input('--> ')
        ans = ans.lower().strip(' ')
        
        if ans == '1':
            overWorldStory()
            
        elif ans == '2':
            break
            
        elif ans == 'stats':
            os.system('cls' if os.name == 'nt' else 'clear')
            etime = time.time() - stime
            player.setTime(etime)
            print(vars(player))
            print(f"You have {rods} blaze rods, {ePearls} Ender Pearls, {eyes} Eye's of Ender, {powder} Blaze Powder and {bed} beds")
            input('Press Enter to continue: ')
            
        elif ans == 'reset':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
                
        elif ans == 'quit':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                ans = input('Are you sure? (yes|no): ')
                ans = ans.lower().strip(' ')
                if ans == 'yes':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thanks for playing!')
                    time.sleep(1)
                    exit()
                elif ans == 'no':
                    break
                else:
                    print('Invalid Response')
                    input('Press Enter to continue: ')
        else:
            print('Invalid Response')
            input('Press Enter to continue: ')
    
def findPortal():
    os.system('cls' if os.name == 'nt' else 'clear')
    global has_seen
    if has_seen == False:
        print('''You search around the area and find a portal.
This portal was built long ago. Now it is in ruins.
You look around...
You find a chest with some original building materials!
You are able to repair the portal, and with a WHOOSH! the portal sparks to life!        
        ''')
        has_seen = True
        input('Press Enter to continue: ')
        ruinedPortal()
    else:
        ruinedPortal()

def fortressLoot():
    global att
    loot = {'HP3': 3,'HP5': 5, 'HP10': 10 }
    loot2 = random.choice(list(loot))
    loot3 = loot.get(loot2)
    health = player.getHealth()
    newHealth = health + loot3
    time.sleep(1)
    if att >= 1:
        att -= 1
        if getRandom() <= 15:
            player.setHealth(newHealth)
            print(f'You have found a health boost of {loot3}!\nYour new heath is {player.getHealth()}')
            print(f'You have {att} attemps to find loot left')
            input('Press Enter to continue: ')
        else:
            print('You found no loot')
            print(f'You have {att} attemps to find loot left')
            input('Press Enter to continue: ')
    else:
        print('You have searched the fortress far and wide,\nand there is no more loot to be found')
        input('Press Enter to continue: ')

def strongholdLoot():
    global attSH
    global ePearls
    global bed
    loot = random.choice(['Ender Pearl', 'Bed', 'Strength Potion'])
    amt = random.randint(1, 4)
    if attSH >= 1:
        attSH -= 1
        if getRandom() <= 93:
            if loot == 'Ender Pearl':
                ePearls += amt
                print(f'You found {amt} Ender Pearls!')
                print(f'You now have {ePearls} Ender Pearls.')
                input('Press Enter to continue: ')
            elif loot == 'Bed':
                bed += amt
                print(f'You found {amt} beds!')
                print(f'You now have {bed} beds.')
                input('Press Enter to continue: ')
            elif loot == 'Strength Potion':
                newAttack = player.getAttack() + 5
                player.setAttack(newAttack)
                print(f'You have found a {loot}!')
                print(f'Your new attack value is {player.getAttack()}')
                input('Press Enter to continue: ')
                
                
        else:
            print('You found no loot')
            print(f'You have {attSH} attemps to find loot left')
            input('Press Enter to continue: ')
    else:
        print('You have searched the Stronghold far and wide,\nand there is no more loot to be found')
        input('Press Enter to continue: ')

def music_play():	
	#music = ['calm1.ogg', 'calm2.ogg']
	music = random.choice(os.listdir('sounds\\game\\' if os.name == 'nt' else 'sounds/game/'))
	pygame.mixer.init()
	pygame.mixer.music.load('sounds/game/' + music)
	pygame.mixer.music.set_volume(1.0) 
	pygame.mixer.music.play(-1, 0.0)

def main():
    # Get the player name
    global stime
    steveName = input("Please Enter your name, or leave blank for a random name: ").strip(' ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if steveName == '':
        with open('names.txt', 'r') as f:
            lines = f.readlines()
            steveName = random.choice(lines)[:-1]
            f.close()
    setBase(steveName)
    music_play()
    stime = time.time()
    intro()
   
os.system('cls' if os.name == 'nt' else 'clear')
main()
    
