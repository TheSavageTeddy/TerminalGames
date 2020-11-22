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

P1 - ●
P2 - ○
'''



