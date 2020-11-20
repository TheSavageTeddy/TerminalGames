import os, re, time, random, keyboard, math

os.system("stty -echo") #makes text entered in terminal invisible

try:
    height = int(re.search("(\d+)\)", str(os.get_terminal_size())).group(1))-1 #the terminal needs -1 because uh
    width = int(re.search("(\d+),", str(os.get_terminal_size())).group(1))
except OSError:
    print("This game should be played in the terminal.")
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


speed = 0.4
starx = random.randint(0, width)
stary = random.randint(0, height)

px = round(width/2)
py = round(height/2)
plength = 1
pdir = "right" #possible dir: right left up down


while True:
    for i in range(0, height):
        if i == stary:
            if i == py:
                if starx > px:
                    print("·"*(width-px) + "●" + "·"*(starx - px)+"✡"+"·"*(width-starx-2))
                else:
                    print("·"*(width-starx) + "✡" + "·"*(((width-(width-px)-1))-px)+"●"+"·"*(((width-(width-px)-1))-px))
            else:
                print("·"*(width-starx) + "✡" + "·"*(width-(width-starx)-1))
        elif i == py:
            print("·"*(width-px) + "●" + "·"*(width-(width-px)-1))
        else:
            print("·"*width)
    print(starx, stary, px, py)

    time.sleep(speed)
    