'''
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

if height < 14 or width < 30:
    print("The terminal size should be at least 30x14 (width x height)")
    time.sleep(2)

board = [
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
]

moves = []



'''
██  ██  ██  ██  
  ██  ██  ██  ██
██  ██  ██  ██  
  ██  ██  ██  ██
██  ██  ██  ██  
  ██  ██  ██  ██
██  ██  ██  ██  
  ██  ██  ██  ██
'''


'''
   ███   ███   ███   ███
███   ███   ███   ███
   ███   ███   ███   ███
███   ███   ███   ███
   ███   ███   ███   ███
███   ███   ███   ███
   ███   ███   ███   ███
███   ███   ███   ███
'''

'''
    8 ███   ███   ███   ███   
    7    ███   ███   ███   ███
    6 ███   ███   ███   ███   
    5    ███   ███   ███   ███
    4 ███   ███   ███   ███   
    3    ███   ███   ███   ███
    2 ███   ███   ███   ███   
    1    ███   ███   ███   ███
       a  b  c  d  e  f  g  h
'''

'''
    8 ███   ███   ███   ███   
    7    ███   ███   ███   ███
    6 ███   ███   ███   ███   
    5    ███   ███   ███   ███
    4 ███   ███   ███   ███   
    3    ███   ███   ███   ███
    2 █P█ P █P█ P █P█ P █P█ P 
    1  R ███   ███   ███   ███
       a  b  c  d  e  f  g  h
'''





'''