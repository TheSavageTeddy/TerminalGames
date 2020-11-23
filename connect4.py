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
cursor = 1
#cursor or arrow position

def printline(x):
    if x == 1 or x == 8:
        print("  ━╋━━━━━━━━━━━━━━━━━━━━━╋━")
    elif x >= 2 and x <= 7:
        line = "   ┃ ·  ·  ·  ·  ·  ·  · ┃ "
        for i in range(0, 7):
            line = re.sub("(·)", array[x-2][i].replace("0", "·").replace("1", "●").replace("2", "○"), line, count=1, flags=0);
        print(line)
    elif x == 10:
        line = "e"
        print(line)
    elif x == 9:
        print("     1  2  3  4  5  6  7")
    else:
        print("P1 - ●\nP2 - ○")
        


while True:
    for i in range(1, 12):
        printline(i)
    break
    