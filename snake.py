import os, re, time, random, keyboard

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
#    ●
#
#    SNAKE EXAMPLE
#
#    ━━━━━━┓
#        ┃
#        ┃
#        ●
#        ✡
#        ·


speed = 0.4
starx = random.randint(1, width)
stary = random.randint(1, height)

while True:
    for i in range(0, height):
        if i == stary:
            print("·"*(width-starx) + "✡" + "·"*(width-(width-starx)-1))
        else:
            print("·"*width)

    time.sleep(speed)
    