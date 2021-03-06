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
    time.sleep(2)
    height = 14
    width = 30
    # exit()

if height < 9 or width < 15:
    print("The terminal size should be at least 15x9 (width x height)")
    time.sleep(2)


'''
   ► · ┃ · ┃ ·   0
    ━━━╋━━━╋━━━  1
     · ┃ · ┃ ·   2
    ━━━╋━━━╋━━━  3
     · ┃ · ┃ ·   4
     ▲           5
                 6
    P1           7
    P2           8
'''

cursorx = 1
cursory = 1
update = 0
grid = [
    ["0", "0", "0"],
    ["0", "0", "0"],
    ["0", "0", "0"]
]
player = 1
win = 0

# key detection

def keyright(x):
    global cursorx, update
    
    if cursorx < 2:
        cursorx = cursorx + 1
    update = 1

def keyleft(x):
    global cursorx, update
    
    if cursorx > 0:
        cursorx = cursorx - 1
    update = 1

def keyup(x):
    global cursory, update
    
    if cursory > 0:
        cursory = cursory - 1
    update = 1

def keydown(x):
    global cursory, update
    
    if cursory < 2:
        cursory = cursory + 1
    update = 1

def place(x):
    global cursorx, cursory, update, player

    if grid[cursory][cursorx] == "0":
        grid[cursory][cursorx] = str(player)

        if player == 1:
            player = 2
        else:
            player = 1
        checkwin()
        update = 1
    

def checkwin():
    global win
    for i in range(0, 2):
        if "".join(grid[i]) == "111" or "".join(grid[i]) == "222":
            win = grid[i][0]
            break
        if grid[0][i] + grid[1][i] + grid[2][i] == "111" or grid[0][i] + grid[1][i] + grid[2][i] =="222":
            win = grid[0][i]
            break
    
    if grid[0][0] + grid[1][1] + grid[2][2] == "111" or grid[0][0] + grid[1][1] + grid[2][2] == "222":
        win = grid[0][i]

    


keyboard.on_press_key("right arrow", keyright)
keyboard.on_press_key("left arrow", keyleft)
keyboard.on_press_key("up arrow", keyup)
keyboard.on_press_key("down arrow", keydown)
keyboard.on_press_key("space", place)

def printboard(x):
    if x == 1 or x == 3:
        print("    ━━━╋━━━╋━━━")
    if x == 0 or x == 2 or x == 4:
        thing = [' ', ' ', ' ', ' ', ' ', '·', ' ', '┃', ' ', '·', ' ', '┃', ' ', '·']
        complete = ""
        count = 0
        for i in range(0, len(thing)):
            if i == 3 and cursory == ((x+2)/2)-1:
                complete = complete + "►"
            elif thing[i] == "·":
                complete = complete + grid[int(x/2)][count].replace("0", " ").replace("1", "o").replace("2", "x")
                count = count + 1
            else:
                complete = complete + thing[i]
        print(" "+complete)
    if x == 5:
        print("     "+"    "*cursorx+"▲")


while True:
    for i in range(0, 6):
        printboard(i)
    update = 0
    while update == 0:
        pass