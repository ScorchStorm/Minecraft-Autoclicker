from pyautogui import click, mouseDown, mouseUp, keyDown, keyUp, scroll, press, hold, sleep
#from time import sleep
lag = 6

def Main():
    #Sweeping_Edge()
    #Wither_Farm_Sweeping_Edge()
    #Combat()
    #river_fishing()
    #cave_fishing()
    #auto_fishing()
    #quick_jump()
    #cobblestone_generator()
    #copper_farm()
    afk()  

def Sweeping_Edge():
    """Performs a Sweeping Edge Attack Each Time the Cooldown is Expired"""
    while True:
        click()
        sleep(0.5) # This is the real time it take to reload a sweeping edge attack with a diamond sword
        sleep(0.04*lag) # This is to account for lag. Adjust accordingly

def Wither_Farm_Sweeping_Edge():
    #This is so you eat food that's in your left hand
    #mouseDown(button='right')
    while True:
        click()  
        sleep(0.7) #This works 0.7
 
def Combat():
    mouseDown(button='right')
    while True:
        jump()  
        sleep(0.06 ) # Gives just enough time for Sweeeping Edge to reload
        mouseUp(button='right') # Takes about 0.104 seconds?
        click() # Takes almost exactly 0.102 seconds
        mouseDown(button='right') # Takes about 0.104 seconds?
 
def river_fishing():
    """ 
    Reels in the fishing rod during the time when a fish is most likely to be caught while fishing in a river
    Calibrated for Lure III 
    """
    while True:
        click(button='right')
        click(button='right')
        sleep(15)

def cave_fishing():
    """
    Reels in the fishing rod during the time when a fish is most likely to be caught while fishing in a cave
    Calibrated for Lure III
    """
    while True:
        click(button='right')
        click(button='right')
        sleep(14)

def cobblestone_generator():
    mouseDown(button='left')
    n=0
    while True:
        #sleep(180) # For stone pickaxe
        sleep(60*45) # For diamond Efficiency V, Unbreaking III pickaxe
        scroll(260) # Average scroll found experimentally with 5 scrolls
        n+=1
        if n == 4:
            return

def copper_farm():
    while True:
        sleep(2.5)
        click(button='left')

def auto_fishing():
    """Pretty much just spams right click to farm fish at a specialized micro auto fisher"""
    sleep(4)
    mouseDown(duration=100,button='right')

def afk():
    mouseDown(button='right') # This is so you eat the food you're holding
    while True:
        with hold('a'):
            sleep(1)
        with hold('d'):
            sleep(1)
        sleep(10)

def quick_jump():
    while True:
        jump()
        sleep(0.3) # What is required for an actual jump?
        sleep(0.02) # This is to account for lag, adjust accordingly

def jump():
    keyDown('space')
    keyUp('space')

Main()

# For sword and shield
# 0 seconds fails afeter about 16 attempts
# 0.0000000001 seconds worked 250 times without failing (what was even the point of all this???)
# 0.0005 seconds work 250 times without failing
# 0.001 seconds worked 500 times without failing
# 0.002 seconds worked 250 times without failing
# 0.004 seconds worked 300 times without failing
# 0.0081 seconds worked 400 times without failing
#Notes:
#jump() 
#sleep(0.2161) #without shield -> 0.18
#sleep(0.102) #The time it takes to click() #failed after 202 successful attempts
#jump()
#sleep(0.2161) #0.2161 successfully performed 200 jumps in a row 0.2160 failed once at 70, once at 203, and once at 30
#click()