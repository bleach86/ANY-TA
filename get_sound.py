import random
import os
import pygame
import time


def zombieSay():
    if pygame.mixer.get_init() == None:
        print('damn')
        pass
    else:
        sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        while 'say' not in sound:
            sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        #pygame.mixer.init()
        ps = pygame.mixer.Sound('sounds\\zombie\\' + sound if os.name == 'nt' else 'sounds/zombie/' + sound)
        ps.play()
    
def zombieHurt():
    sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
    #print(sound)
    while 'hurt' not in sound:
        sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
    #pygame.mixer.init()
    ps = pygame.mixer.Sound('sounds\\zombie\\' + sound if os.name == 'nt' else 'sounds/zombie/' + sound)
    ps.play()

def zombieDeath():
    sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
    #print(sound)
    while 'death' not in sound:
        sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
    #pygame.mixer.init()
    ps = pygame.mixer.Sound('sounds\\zombie\\' + sound if os.name == 'nt' else 'sounds/zombie/' + sound)
    ps.play()
    
def zombieMiss():
    sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
    #print(sound)
    while 'block' not in sound:
        sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
    #pygame.mixer.init()
    ps = pygame.mixer.Sound('sounds\\zombie\\' + sound if os.name == 'nt' else 'sounds/zombie/' + sound)
    ps.play()

def skeletonSay():
    sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
    #print(sound)
    #pygame.mixer.init()
    while 'say' not in sound:
        sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
    ps = pygame.mixer.Sound('sounds\\skeleton\\' + sound if os.name == 'nt' else 'sounds/skeleton/' + sound)
    ps.play()
    
def skeletonHurt():
    sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
    #print(sound)
    #pygame.mixer.init()
    while 'hurt' not in sound:
        sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
    ps = pygame.mixer.Sound('sounds\\skeleton\\' + sound if os.name == 'nt' else 'sounds/skeleton/' + sound)
    ps.play()
    
def skeletonDeath():
    sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
    #print(sound)
    #pygame.mixer.init()
    while 'death' not in sound:
        sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
    ps = pygame.mixer.Sound('sounds\\skeleton\\' + sound if os.name == 'nt' else 'sounds/skeleton/' + sound)
    ps.play()

def skeletonMiss():
    sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
    #print(sound)
    #pygame.mixer.init()
    while 'block' not in sound:
        sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
    ps = pygame.mixer.Sound('sounds\\skeleton\\' + sound if os.name == 'nt' else 'sounds/skeleton/' + sound)
    ps.play()

def creeperSay():
    sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
    #print(sound)
    #pygame.mixer.init()
    while 'say' not in sound:
        sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
    ps = pygame.mixer.Sound('sounds\\creeper\\' + sound if os.name == 'nt' else 'sounds/creeper/' + sound)
    ps.play()
    
def creeperDeath():
    sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
    #print(sound)
    #pygame.mixer.init()
    while 'death' not in sound:
        sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
    ps = pygame.mixer.Sound('sounds\\creeper\\' + sound if os.name == 'nt' else 'sounds/creeper/' + sound)
    ps.play()
    
def endermanScream():
    sound = random.choice(os.listdir('sounds\\enderman\\' if os.name == 'nt' else 'sounds/enderman/'))
    #print(sound)
    #pygame.mixer.init()
    while 'scream' not in sound:
        sound = random.choice(os.listdir('sounds\\enderman\\' if os.name == 'nt' else 'sounds/enderman/'))
    ps = pygame.mixer.Sound('sounds\\enderman\\' + sound if os.name == 'nt' else 'sounds/enderman/' + sound)
    ps.play()

def endermanHurt():
    sound = random.choice(os.listdir('sounds\\enderman\\' if os.name == 'nt' else 'sounds/enderman/'))
    #print(sound)
    #pygame.mixer.init()
    while 'hit' not in sound:
        sound = random.choice(os.listdir('sounds\\enderman\\' if os.name == 'nt' else 'sounds/enderman/'))
    ps = pygame.mixer.Sound('sounds\\enderman\\' + sound if os.name == 'nt' else 'sounds/enderman/' + sound)
    ps.play()

def creeperMiss():
    sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
    #print(sound)
    #pygame.mixer.init()
    while 'block' not in sound:
        sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
    ps = pygame.mixer.Sound('sounds\\creeper\\' + sound if os.name == 'nt' else 'sounds/creeper/' + sound)
    ps.play()
    
def playerDamage():
    sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    #print(sound)
    #pygame.mixer.init()
    while 'hit' not in sound:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
    ps.play()
    
def playerFire():
    sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    #print(sound)
    #pygame.mixer.init()
    while 'fire' not in sound:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
    ps.play()
    
def playerExplode():
    sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    #print(sound)
    #pygame.mixer.init()
    while 'explode' not in sound:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
    ps.play()

def playerFall():
    sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    #print(sound)
    #pygame.mixer.init()
    while 'fall' not in sound:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
    ps.play()
    
def mobMiss():
    sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    #print(sound)
    #pygame.mixer.init()
    while 'block' not in sound:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
    ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
    ps.play()

def piglinHurt():
    sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
    #print(sound)
    #pygame.mixer.init()
    while 'hurt' not in sound:
        sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
    ps = pygame.mixer.Sound('sounds\\piglin\\' + sound if os.name == 'nt' else 'sounds/piglin/' + sound)
    ps.play()

def piglinDeath():
    sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
    #print(sound)
    #pygame.mixer.init()
    while 'death' not in sound:
        sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
    ps = pygame.mixer.Sound('sounds\\piglin\\' + sound if os.name == 'nt' else 'sounds/piglin/' + sound)
    ps.play()
    
def piglinCelebrate():
    sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
    #print(sound)
    #pygame.mixer.init()
    while 'celebrate' not in sound:
        sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
    ps = pygame.mixer.Sound('sounds\\piglin\\' + sound if os.name == 'nt' else 'sounds/piglin/' + sound)
    ps.play()

def piglinAdmire():
    sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
    #print(sound)
    #pygame.mixer.init()
    while 'admire' not in sound:
        sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
    ps = pygame.mixer.Sound('sounds\\piglin\\' + sound if os.name == 'nt' else 'sounds/piglin/' + sound)
    ps.play()

def blazeHurt():
    sound = random.choice(os.listdir('sounds\\blaze\\' if os.name == 'nt' else 'sounds/blaze/'))
    #print(sound)
    #pygame.mixer.init()
    while 'hit' not in sound:
        sound = random.choice(os.listdir('sounds\\blaze\\' if os.name == 'nt' else 'sounds/blaze/'))
    ps = pygame.mixer.Sound('sounds\\blaze\\' + sound if os.name == 'nt' else 'sounds/blaze/' + sound)
    ps.play()

def blazeDeath():
    sound = random.choice(os.listdir('sounds\\blaze\\' if os.name == 'nt' else 'sounds/blaze/'))
    #print(sound)
    #pygame.mixer.init()
    while 'death' not in sound:
        sound = random.choice(os.listdir('sounds\\blaze\\' if os.name == 'nt' else 'sounds/blaze/'))
    ps = pygame.mixer.Sound('sounds\\blaze\\' + sound if os.name == 'nt' else 'sounds/blaze/' + sound)
    ps.play()

def dragonHurt():
    sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
    #print(sound)
    #pygame.mixer.init()
    while 'hit' not in sound:
        sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
    ps = pygame.mixer.Sound('sounds\\dragon\\' + sound if os.name == 'nt' else 'sounds/dragon/' + sound)
    ps.play()

def dragonWing():
    sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
    #print(sound)
    #pygame.mixer.init()
    while 'wings' not in sound:
        sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
    ps = pygame.mixer.Sound('sounds\\dragon\\' + sound if os.name == 'nt' else 'sounds/dragon/' + sound)
    ps.play()

def dragonGrowl():
    sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
    #print(sound)
    #pygame.mixer.init()
    while 'growl' not in sound:
        sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
    ps = pygame.mixer.Sound('sounds\\dragon\\' + sound if os.name == 'nt' else 'sounds/dragon/' + sound)
    ps.play()

def dragonDeath():
    sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
    #print(sound)
    #pygame.mixer.init()
    while 'end' not in sound:
        sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
    ps = pygame.mixer.Sound('sounds\\dragon\\' + sound if os.name == 'nt' else 'sounds/dragon/' + sound)
    ps.play()

def oreBreak():
    sound = random.choice(os.listdir('sounds\\ore\\' if os.name == 'nt' else 'sounds/ore/'))
    #print(sound)
    #pygame.mixer.init()
    while 'break' not in sound:
        sound = random.choice(os.listdir('sounds\\ore\\' if os.name == 'nt' else 'sounds/ore/'))
    ps = pygame.mixer.Sound('sounds\\ore\\' + sound if os.name == 'nt' else 'sounds/ore/' + sound)
    ps.play()
    
def oreMiss():
    sound = random.choice(os.listdir('sounds\\ore\\' if os.name == 'nt' else 'sounds/ore/'))
    #print(sound)
    #pygame.mixer.init()
    while 'stone' not in sound:
        sound = random.choice(os.listdir('sounds\\ore\\' if os.name == 'nt' else 'sounds/ore/'))
    ps = pygame.mixer.Sound('sounds\\ore\\' + sound if os.name == 'nt' else 'sounds/ore/' + sound)
    ps.play()

def eyeThrow():
    sound = random.choice(os.listdir('sounds\\eye\\' if os.name == 'nt' else 'sounds/eye/'))
    #print(sound)
    #pygame.mixer.init()
    while 'endereye' not in sound:
        sound = random.choice(os.listdir('sounds\\eye\\' if os.name == 'nt' else 'sounds/eye/'))
    ps = pygame.mixer.Sound('sounds\\eye\\' + sound if os.name == 'nt' else 'sounds/eye/' + sound)
    ps.play()
def eyeBreak():
    sound = random.choice(os.listdir('sounds\\eye\\' if os.name == 'nt' else 'sounds/eye/'))
    #print(sound)
    #pygame.mixer.init()
    while 'dead' not in sound:
        sound = random.choice(os.listdir('sounds\\eye\\' if os.name == 'nt' else 'sounds/eye/'))
    ps = pygame.mixer.Sound('sounds\\eye\\' + sound if os.name == 'nt' else 'sounds/eye/' + sound)
    ps.play()

# while True:
    # zombieSay()
    # time.sleep(1)
