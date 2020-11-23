import os, re, time, random, keyboard, math

os.system("stty -echo") #makes text entered in terminal invisible

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
# ┣ ╋ ━ ┫
#┗ ┻ ━ ┛
#┏ ┳ ━ ┓

'''
GRID

  ━╋━━━━━━━━━━━━━━━━━━━━━╋━
   ┃ ·  ·  ·  ·  ·  ·  · ┃
   ┃ ·  ·  ·  ·  ·  ·  · ┃
   ┃ ·  ·  ·  ·  ·  ·  · ┃
   ┃ ·  ·  ·  ·  ·  ·  · ┃
   ┃ ·  ·  ·  ·  ·  ·  · ┃
   ┃ ·  ·  ·  ·  ·  ·  · ┃
  ━╋━━━━━━━━━━━━━━━━━━━━━╋━
     1  2  3  4  5  6  7

P1 - ●
P2 - ○
'''

'''
  ━╋━━━━━━━━━━━━━━━━━━━━━╋━  1
   ┃ ·  ·  ·  ·  ·  ·  · ┃   2
   ┃ ·  ·  ·  ·  ·  ·  · ┃   3
   ┃ ·  ·  ·  ·  ·  ·  · ┃   4
   ┃ ·  ·  ·  ·  ·  ·  · ┃   5
   ┃ ·  ·  ·  ·  ·  ·  · ┃   6
   ┃ ·  ·  ·  ·  ·  ·  · ┃   7
  ━╋━━━━━━━━━━━━━━━━━━━━━╋━  8
     1  2  3  4  5  6  7     9
                             10
P1 - ●
P2 - ○
'''

#Key listners and actions

def keyright(x):
    global cursor, update
    
    if cursor < 7:
        cursor = cursor + 1
    update = 1

def keyleft(x):
    global cursor, update

    if cursor > 1:
        cursor = cursor - 1
    update = 1


keyboard.on_press_key("right arrow", keyright)
keyboard.on_press_key("left arrow", keyleft)

array = [
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
]
# 0 - nothing
# 1 - player 1
# 2 - player 2
cursor = 1 #cursor or arrow position
turn = 1 # 1 - player 1's turn, etc
update = 0 # need to update??

def printline(x):
    if x == 1 or x == 8:
        print("  ━╋━━━━━━━━━━━━━━━━━━━━━╋━")
    elif x >= 2 and x <= 7:
        line = [' ', ' ', ' ', '┃', ' ', '·', ' ', ' ', '·', ' ', ' ', '·', ' ', ' ', '·', ' ', ' ', '·', ' ', ' ', '·', ' ', ' ', '·', ' ', '┃', ' ']
        fline = []
        count = 0
        for i in range(0, len(line)):
            if line[i] == "·":
                fline.append(re.sub("(·)", array[x-2][count].replace("0", "·").replace("1", "●").replace("2", "○"), line[i], count=1, flags=0))
                count = count+1
            else:
                fline.append(line[i])
        print("".join(fline))
    elif x == 10:
        print("  "+"   "*cursor+"▲")
    elif x == 9:
        print("     1  2  3  4  5  6  7")
    else:
        if turn == 1:
            print("\nP1 - ● (P1's turn)\nP2 - ○")
        else:
            print("\nP1 - ● (P2's turn)\nP2 - ○")
        


while True:
    for i in range(1, 12):
        printline(i)
        
    update = 0
    while update == 0:
        pass

    