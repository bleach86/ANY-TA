import random
import os
import pygame
import time


def zombieSay():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        while 'say' not in sound:
            sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        ps = pygame.mixer.Sound('sounds\\zombie\\' + sound if os.name == 'nt' else 'sounds/zombie/' + sound)
        ps.play()
    
def zombieHurt():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        while 'hurt' not in sound:
            sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        ps = pygame.mixer.Sound('sounds\\zombie\\' + sound if os.name == 'nt' else 'sounds/zombie/' + sound)
        ps.play()

def zombieDeath():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        while 'death' not in sound:
            sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        ps = pygame.mixer.Sound('sounds\\zombie\\' + sound if os.name == 'nt' else 'sounds/zombie/' + sound)
        ps.play()
    
def zombieMiss():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        while 'block' not in sound:
            sound = random.choice(os.listdir('sounds\\zombie\\' if os.name == 'nt' else 'sounds/zombie/'))
        ps = pygame.mixer.Sound('sounds\\zombie\\' + sound if os.name == 'nt' else 'sounds/zombie/' + sound)
        ps.play()

def skeletonSay():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
        while 'say' not in sound:
            sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
        ps = pygame.mixer.Sound('sounds\\skeleton\\' + sound if os.name == 'nt' else 'sounds/skeleton/' + sound)
        ps.play()
    
def skeletonHurt():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
        while 'hurt' not in sound:
            sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
        ps = pygame.mixer.Sound('sounds\\skeleton\\' + sound if os.name == 'nt' else 'sounds/skeleton/' + sound)
        ps.play()
    
def skeletonDeath():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
        while 'death' not in sound:
            sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
        ps = pygame.mixer.Sound('sounds\\skeleton\\' + sound if os.name == 'nt' else 'sounds/skeleton/' + sound)
        ps.play()

def skeletonMiss():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
        while 'block' not in sound:
            sound = random.choice(os.listdir('sounds\\skeleton\\' if os.name == 'nt' else 'sounds/skeleton/'))
        ps = pygame.mixer.Sound('sounds\\skeleton\\' + sound if os.name == 'nt' else 'sounds/skeleton/' + sound)
        ps.play()

def creeperSay():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
        while 'say' not in sound:
            sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
        ps = pygame.mixer.Sound('sounds\\creeper\\' + sound if os.name == 'nt' else 'sounds/creeper/' + sound)
        ps.play()
    
def creeperDeath():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
        while 'death' not in sound:
            sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
        ps = pygame.mixer.Sound('sounds\\creeper\\' + sound if os.name == 'nt' else 'sounds/creeper/' + sound)
        ps.play()
    
def endermanScream():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\enderman\\' if os.name == 'nt' else 'sounds/enderman/'))
        while 'scream' not in sound:
            sound = random.choice(os.listdir('sounds\\enderman\\' if os.name == 'nt' else 'sounds/enderman/'))
        ps = pygame.mixer.Sound('sounds\\enderman\\' + sound if os.name == 'nt' else 'sounds/enderman/' + sound)
        ps.play()

def endermanHurt():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\enderman\\' if os.name == 'nt' else 'sounds/enderman/'))
        while 'hit' not in sound:
            sound = random.choice(os.listdir('sounds\\enderman\\' if os.name == 'nt' else 'sounds/enderman/'))
        ps = pygame.mixer.Sound('sounds\\enderman\\' + sound if os.name == 'nt' else 'sounds/enderman/' + sound)
        ps.play()

def creeperMiss():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
        while 'block' not in sound:
            sound = random.choice(os.listdir('sounds\\creeper\\' if os.name == 'nt' else 'sounds/creeper/'))
        ps = pygame.mixer.Sound('sounds\\creeper\\' + sound if os.name == 'nt' else 'sounds/creeper/' + sound)
        ps.play()
    
def playerDamage():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        while 'hit' not in sound:
            sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
        ps.play()
    
def playerFire():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        while 'fire' not in sound:
            sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
        ps.play()
    
def playerExplode():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        while 'explode' not in sound:
            sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
        ps.play()

def playerFall():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        while 'fall' not in sound:
            sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
        ps.play()
    
def mobMiss():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        while 'block' not in sound:
            sound = random.choice(os.listdir('sounds\\player\\' if os.name == 'nt' else 'sounds/player/'))
        ps = pygame.mixer.Sound('sounds\\player\\' + sound if os.name == 'nt' else 'sounds/player/' + sound)
        ps.play()
    
def piglinHurt():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
        while 'hurt' not in sound:
            sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
        ps = pygame.mixer.Sound('sounds\\piglin\\' + sound if os.name == 'nt' else 'sounds/piglin/' + sound)
        ps.play()

def piglinDeath():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
        while 'death' not in sound:
            sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
        ps = pygame.mixer.Sound('sounds\\piglin\\' + sound if os.name == 'nt' else 'sounds/piglin/' + sound)
        ps.play()
    
def piglinCelebrate():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
        while 'celebrate' not in sound:
            sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
        ps = pygame.mixer.Sound('sounds\\piglin\\' + sound if os.name == 'nt' else 'sounds/piglin/' + sound)
        ps.play()

def piglinAdmire():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
        #print(sound)
        #pygame.mixer.init()
        while 'admire' not in sound:
            sound = random.choice(os.listdir('sounds\\piglin\\' if os.name == 'nt' else 'sounds/piglin/'))
        ps = pygame.mixer.Sound('sounds\\piglin\\' + sound if os.name == 'nt' else 'sounds/piglin/' + sound)
        ps.play()

def blazeHurt():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\blaze\\' if os.name == 'nt' else 'sounds/blaze/'))
        while 'hit' not in sound:
            sound = random.choice(os.listdir('sounds\\blaze\\' if os.name == 'nt' else 'sounds/blaze/'))
        ps = pygame.mixer.Sound('sounds\\blaze\\' + sound if os.name == 'nt' else 'sounds/blaze/' + sound)
        ps.play()

def blazeDeath():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\blaze\\' if os.name == 'nt' else 'sounds/blaze/'))
        while 'death' not in sound:
            sound = random.choice(os.listdir('sounds\\blaze\\' if os.name == 'nt' else 'sounds/blaze/'))
        ps = pygame.mixer.Sound('sounds\\blaze\\' + sound if os.name == 'nt' else 'sounds/blaze/' + sound)
        ps.play()

def dragonHurt():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
        while 'hit' not in sound:
            sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
        ps = pygame.mixer.Sound('sounds\\dragon\\' + sound if os.name == 'nt' else 'sounds/dragon/' + sound)
        ps.play()

def dragonWing():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
        #print(sound)
        #pygame.mixer.init()
        while 'wings' not in sound:
            sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
        ps = pygame.mixer.Sound('sounds\\dragon\\' + sound if os.name == 'nt' else 'sounds/dragon/' + sound)
        ps.play()

def dragonGrowl():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
        while 'growl' not in sound:
            sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
        ps = pygame.mixer.Sound('sounds\\dragon\\' + sound if os.name == 'nt' else 'sounds/dragon/' + sound)
        ps.play()

def dragonDeath():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
        while 'end' not in sound:
            sound = random.choice(os.listdir('sounds\\dragon\\' if os.name == 'nt' else 'sounds/dragon/'))
        ps = pygame.mixer.Sound('sounds\\dragon\\' + sound if os.name == 'nt' else 'sounds/dragon/' + sound)
        ps.play()

def oreBreak():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\ore\\' if os.name == 'nt' else 'sounds/ore/'))
        while 'break' not in sound:
            sound = random.choice(os.listdir('sounds\\ore\\' if os.name == 'nt' else 'sounds/ore/'))
        ps = pygame.mixer.Sound('sounds\\ore\\' + sound if os.name == 'nt' else 'sounds/ore/' + sound)
        ps.play()
    
def oreMiss():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\ore\\' if os.name == 'nt' else 'sounds/ore/'))
        while 'stone' not in sound:
            sound = random.choice(os.listdir('sounds\\ore\\' if os.name == 'nt' else 'sounds/ore/'))
        ps = pygame.mixer.Sound('sounds\\ore\\' + sound if os.name == 'nt' else 'sounds/ore/' + sound)
        ps.play()

def eyeThrow():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\eye\\' if os.name == 'nt' else 'sounds/eye/'))
        while 'endereye' not in sound:
            sound = random.choice(os.listdir('sounds\\eye\\' if os.name == 'nt' else 'sounds/eye/'))
        ps = pygame.mixer.Sound('sounds\\eye\\' + sound if os.name == 'nt' else 'sounds/eye/' + sound)
        ps.play()
        
def eyeBreak():
    if pygame.mixer.get_init() == None:
        pass
    else:
        sound = random.choice(os.listdir('sounds\\eye\\' if os.name == 'nt' else 'sounds/eye/'))
        while 'dead' not in sound:
            sound = random.choice(os.listdir('sounds\\eye\\' if os.name == 'nt' else 'sounds/eye/'))
        ps = pygame.mixer.Sound('sounds\\eye\\' + sound if os.name == 'nt' else 'sounds/eye/' + sound)
        ps.play()

# while True:
    # zombieSay()
    # time.sleep(1)
