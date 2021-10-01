# -----TRUE AND FALSE------
#           or
# ------TIC TAC TOE--------
# Project by: Dhanesh Gauri


import random
ls = [0,1,2,3,4,5,6,7,8,9]
win = False
class Figure:
    def fig(self):
        self.fi = print(f'''\n\n\n
                    {ls[7]}  ||   {ls[8]}  ||   {ls[9]}
                             
                 ========================   
                             
                    {ls[4]}  ||   {ls[5]}  ||   {ls[6]}
                             
                 ========================   
                             
                    {ls[1]}  ||   {ls[2]}  ||   {ls[3]}  
                    ''')

figure = Figure()
class Choice(Figure):
    def o_mark(self):
        ch = int(input("Enter your position: "))
        position = False
        for i in range(1,10):
            if ch == ls[i]:   
                ls[i] = "O" 
                position = True       
            i+=1
        if position == False:
            print("Due to invalid position entered by player their chance is lost ")
    def x_mark(self):
        ch = int(input("Enter your position: "))
        position = False
        for i in range(1,10):
            if ch == ls[i]:   
                ls[i] = "X"
                position = True 
            i+=1
        if position == False:
            print("Due to invalid position entered by player their chance is lost ")
choice = Choice()
        

class Result(Choice):
    def play(self):

        if (ls[1]==ls[2]==ls[3])or(ls[4]==ls[5]==ls[6])or(ls[7]==ls[8]==ls[9])\
            or(ls[7]==ls[4]==ls[1])or(ls[8]==ls[5]==ls[2])or(ls[9]==ls[6]==ls[3])\
                or(ls[7]==ls[5]==ls[3])or(ls[1]==ls[5]==ls[9]):
                figure.fig()
                global win
                win = True

        else:
            draw = True
            for i in range(1,10):
                if i in ls:
                    draw = False
                i+=1
            if draw == True:
                print("Match is draw")
                exit()
result = Result()


class With_Computer():

    def play_comp(self):
        while(True):
            position = True
            if (ls[4]==ls[7]) or (ls[5]==ls[9]) or (ls[2]==ls[3]):
                if ls[1] == 1:
                    ls[1]="O"
                    print("Computer choose position 1")
                    position = False
                    break

            if (ls[1]==ls[3])or(ls[5]==ls[8]):
                if ls[2] == 2:
                    ls[2]="O"
                    print("Computer choose position 2")
                    position = False
                    break
                    
            if (ls[1]==ls[2])or(ls[6]==ls[9])or(ls[5]==ls[7]):
                if ls[3] == 3:
                    ls[3]="O"
                    print("Computer choose position 3")
                    position = False
                    break
                
            if (ls[1]==ls[7])or(ls[5]==ls[6]):
                if ls[4] == 4:
                    ls[4]="O"
                    print("Computer choose position 4")
                    position = False
                    break
                    
            if (ls[9]==ls[3])or(ls[4]==ls[5]):
                if ls[6] == 6:
                    ls[6]="O"
                    print("Computer choose position 6")
                    position = False
                    break
                    
            if (ls[8]==ls[9])or(ls[4]==ls[1])or(ls[5]==ls[3]):
                if ls[7] == 7:
                    ls[7]="O"
                    print("Computer choose position 7")
                    position = False
                    break
                    
            if (ls[5]==ls[2])or(ls[7]==ls[9]):
                if ls[8] == 8:
                    ls[8]="O"
                    print("Computer choose position 8")
                    position = False
                    break
                    
            if (ls[7]==ls[8])or(ls[6]==ls[3])or(ls[5]==ls[1]):
                if ls[9] == 9:
                    ls[9]="O"
                    print("Computer choose position 9")
                    position = False
                    break
                    
            if position == True:
                ls2 = []
                for i in range(1,10):
                    if i == ls[i]:
                        ls2.append(i)
                    i+=1
                ch = random.choice(ls2)
                int(ch)
                ls[ch]="O"
                print(f"Computer choose position {ch}")
                break
                
        figure.fig()

with_computer = With_Computer()


if __name__ == "__main__":
    print("\t\tWELCOME TO TRUE AND FALSE GAME\n\n")
    
    while(True):
        print('''
        ========  GAME RULES  =======

        +. Any player put their 3 mark in a straight line win
        +. Put your mark in place of positioned number,number has been replaced with your mark
        +. Player 1 get "O" mark and player 2 get "X" mark, if you play with computer your mark will be "X"
        +. If player put any invalid number in their chance, their chance have been missed


            1. Play with another player
            2. Play with Computer \n\n 
            ''')
        ch = int(input("Enter your choice: "))
        if ch == 1:
            figure.fig()
            while(True):
                print("Player 1 Turn")
                choice.o_mark()
                result.play()
                if win == True:
                    print("player 1 win")
                    exit()
                figure.fig()
                print("player 2 Turn")
                choice.x_mark()
                result.play()
                if win == True:
                    print("player 2 win")
                    exit()
                figure.fig()  

        elif ch == 2:
            ls[5] = "O"
            print("Computer choose position 5")
            figure.fig()
            while(True):
                choice.x_mark()
                result.play()
                if win == True:
                    print("player win")
                    exit()
                figure.fig()
                with_computer.play_comp()
                result.play()
                if win == True:
                    print("Computer win")
                    exit()
        else:
            print("Invalid Choice")