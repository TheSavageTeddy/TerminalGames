import os, re, time, random, keyboard, math

os.system("stty -echo") #makes text entered in terminal invisible

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

#variables and lists
array = [
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
]
# 0 - nothing

cursor = 1 #cursor or arrow position
turn = 1 # 1 - player 1's turn, etc
update = 0 # need to update??
xoffset = " "*(math.floor((width - 29) / 2))
yoffset = math.floor((height - 13) / 2)-1


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

def place(x):
    global turn, array, cursor, update
    
    if array[0][cursor-1] == "0": #if the thing isnt full
        for i in range(0, 6):
            if array[5-i][cursor-1] == "0":
                array[5-i][cursor-1] = str(turn).replace("1", "●").replace("2", "○")
                break
            if i == 6:
                no = True
                break

        if turn == 1:
            turn = 2
        else:
            turn = 1
        checkwin()
        update = 1

def checkwin():
    global array, update

    #vertical
    for i in range(0, 3):
        for ii in range(0, 7):
            if array[i][ii] + array[i+1][ii] + array[i+2][ii] + array[i+3][ii] == "●●●●":
                print("Player 1 wins")
            if array[i][ii] + array[i+1][ii] + array[i+2][ii] + array[i+3][ii] == "○○○○":
                print("Player 2 wins")
    
    #horizontal
    for i in range(0, 4):
        for ii in range(0, 6):
            if array[ii][i] + array[ii][i+1] + array[ii][i+2] + array[ii][i+3] == "●●●●":
                print("Player 1 wins")
            if array[ii][i] + array[ii][i+1] + array[ii][i+2] + array[ii][i+3] == "○○○○":
                print("Player 2 wins")
    
    # diagonal (left up to right down)
    # diagonal (right up to left down)
    


keyboard.on_press_key("right arrow", keyright)
keyboard.on_press_key("left arrow", keyleft)
keyboard.on_press_key("space", place)



def printline(x):
    if x == 1 or x == 8:
        print(xoffset + "  ━╋━━━━━━━━━━━━━━━━━━━━━╋━")
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
        print(xoffset + "".join(fline))
    elif x == 10:
        print(xoffset + "  "+"   "*cursor+"▲")
    elif x == 9:
        print(xoffset + "     1  2  3  4  5  6  7")
    else:
        if turn == 1:
            print("\n"+xoffset+"P1 - ● (P1's turn)"+"\n"+xoffset+"P2 - ○")
        else:
            print("\n"+xoffset+"P1 - ●"+"\n"+xoffset+"P2 - ○ (P2's turn)")
        
# main thing

while True:
    for i in range(0, yoffset+2):
        print("\n")
    for i in range(1, 12):
        printline(i)
    for i in range(0, yoffset-2):
        print("\n")
        
    update = 0
    while update == 0:
        pass

    