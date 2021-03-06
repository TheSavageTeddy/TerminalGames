import os, re, time, random, keyboard, math, platform

if platform.system() == "Windows":
    pass
else:
    try:
        os.system("stty -echo") #makes text entered in terminal invisible
    except:
        pass

try:
    height = int(re.search("(\d+)\)", str(os.get_terminal_size())).group(1))-1 #the terminal needs -1 because uh
    width = int(re.search("(\d+),", str(os.get_terminal_size())).group(1))
except OSError: #if not ran in terminal
    print("This game should be played in the terminal.")
    height = 15
    width = 15
    # exit()

#
#    ASCII
#
#    ┃
#    ━
#    ┛
#    ┗
#    ┓
#    ┏
#        ●
#        ✡
#        ·

snakearray = []
stop = False

speed = 0.1
starx = random.randint(0, width)
stary = random.randint(0, height)

px = round(width/2)-1
py = round(height/2)-1
plength = 1
pdir = "right" #possible dir: right left up down


#key detection
def wkey(x):
    global pdir
    if not pdir == "down": #cant go straight opposite dir
        pdir = "up"

def akey(x):
    global pdir
    if not pdir == "right":
        pdir = "left"

def skey(x):
    global pdir
    if not pdir == "up":
        pdir = "down"

def dkey(x):
    global pdir
    if not pdir == "left":
        pdir = "right"

def ekey(x):
    global stop
    stop = True

keyboard.on_press_key("up arrow", wkey) #cant use lambda because cannot contain assignment
keyboard.on_press_key("left arrow", akey)
keyboard.on_press_key("down arrow", skey)
keyboard.on_press_key("right arrow", dkey)
keyboard.on_press_key("e", ekey)

'''
def printthing():
    for i in range(0, height):
        if i == stary:
            if i == py:
                if starx > px:
                    print("·"*(width-(width-px)-1) + "●" + "·"*(starx - px - 1)+"✡"+"·"*(width-starx))
                else:
                    print("·"*(width-(width-starx)-1) + "✡" + "·"*(px - starx - 1)+"●"+"·"*(width - px))
            else:
                print("·"*(width-(width-starx)-1) + "✡" + "·"*(width-starx))
        elif i == py:
            print("·"*(width-(width-px)-1) + "●" + "·"*(width-px))
        else:
            print("·"*width)
'''

def printarray():
    global snakearray
    
    count = 0
    for item in snakearray:
        print(("".join(map(str, item[1:]))))


def updatearray():
    global snakearray

    snakearray[stary][starx] = "✡"
    snakearray[py][px] = "●"
    print(snakearray)


templist = []
for i in range(0, height):
    templist.clear()
    for i in range(0, width):
        templist.append("·")
    snakearray.append(templist)
    
print(snakearray)
printarray()
while True:
    
    if pdir == "right":
        px = px + 1
    elif pdir == "left":
        px = px - 1
    elif pdir == "up":
        py = py - 1 #up is closer to top and y is from top not bottom
    elif pdir == "down":
        py = py + 1
    
    #when goes off boundary
    if px > width: #right
        px = 1
    if px < 1: #left
        px = width
    if py > height-1: #down
        py = 0
    if py < 0: #up
        py = height

    if px == starx and py == stary: #if they are on star
        plength = plength + 1
        starx = random.randint(0, width)
        stary = random.randint(0, height)

    updatearray()
    printarray()
    

    # print(starx, stary, px, py)

    # half speed when upwards because text
    '''
    if pdir == "up" or pdir == "down":
        time.sleep(speed/(7/17))
    else:
        time.sleep(speed)
    '''

    if stop == True:
        exit()
    time.sleep(speed)