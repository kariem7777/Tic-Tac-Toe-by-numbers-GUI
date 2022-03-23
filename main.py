#kariem gamal eid
#id: 20210523


import sys
import pygame as py
import numpy as np
import pygame.event

pygame.init()
table=np.full((3,3),16)
py.display.set_caption("Tic Tac Toe")
screen = py.display.set_mode((600, 600))

player1_choices=["1","3","5","7","9"]
player2_choices=["0","2","4","6","8"]
p1="1,3,5,7,9"
p2="0,2,4,6,8"
number1 = ""
number2 = ""
current_player=1
p1_color=(0,128,255)
p2_color=(255, 0,0)
line_color=(23, 145, 135)
background_color=(51, 51, 51)





keyboard_counter=0
mouse_counter=0




def display_board():

    screen.fill(background_color)
    py.draw.line(screen, line_color, (0, 200), (600, 200), 15)
    py.draw.line(screen, line_color, (0, 400), (600, 400), 15)
    py.draw.line(screen, line_color, (200, 0), (200, 600), 15)
    py.draw.line(screen, line_color, (400, 0), (400, 600), 15)

def turn(row,col,num):
    table[row][col] = int(num)

    if current_player==1:
        font=py.font.SysFont("Times New Roma",350,True,False)
        surface = font.render(num,True,p1_color)
        screen.blit(surface,(col*200,row*200))
    else:
        font = py.font.SysFont("Times New Roma", 350, True, False)
        surface = font.render(num, True, p2_color)
        screen.blit(surface, (col * 200, row * 200))

def check_valid(row,col):
    if table[row][col]==16:
        return True
    return False


def check_winner():
    global current_player
    #winner row
    for row in range(3):
        if (table[row][0]+table[row][1]+table[row][2]) == 15 and current_player == 1:
            py.draw.line(screen,p1_color,(15,(row*200+100)),(600-15,(row*200+100)),15)
            return True

        elif (table[row][0]+table[row][1]+table[row][2])== 15 and current_player == 2:
            py.draw.line(screen, p2_color, (15, (row * 200 + 100)), (600 - 15, (row * 200 + 100)), 15)
            return True
    #winner col

    for col in range(3):
        if (table[0][col] + table[1][col] + table[2][col])==15 and current_player==1:
            py.draw.line(screen,p1_color,((col*200+100),15),((col*200+100),600-15),15)
            return True
        elif (table[0][col] + table[1][col] + table[2][col])==15 and current_player==2:
            py.draw.line(screen, p2_color, ((col * 200 + 100), 15), ((col * 200 + 100), 600 - 15), 15)
            return True
    #winner diagonal

    if (table[0][0]+table[1][1]+table[2][2]==15) and current_player==1:
        py.draw.line(screen,p1_color,(15,15),(600-15,600-15),15)
        return True
    elif (table[0][0]+table[1][1]+table[2][2])==15 and current_player==2:
        py.draw.line(screen, p2_color, (15, 15), (600 - 15, 600 - 15), 15)
        return True
    elif (table[0][2]+table[1][1]+table[2][0]) ==15 and current_player==1:

        py.draw.line(screen,p1_color,(15,600-15),(600-15,15),15)
        return True
    elif (table[0][2]+table[1][1]+table[2][0]) ==15 and current_player==2:
        py.draw.line(screen, p2_color, (15, 600 - 15), (600 - 15, 15), 15)
        return True
    return False


display_board()
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()



        if event.type == py.KEYDOWN and keyboard_counter == mouse_counter: #keyboard code
            number1=""
            number2=""
            if current_player==1:
                if event.key == py.K_1 or event.key == py.K_3  or event.key == py.K_5  or event.key == py.K_7  or event.key == py.K_9:
                    if event.unicode in player1_choices:
                        player1_choices.remove(event.unicode)
                        number1 = event.unicode
                        keyboard_counter +=1
            else:
                if event.key == py.K_0 or event.key == py.K_2  or event.key == py.K_4  or event.key == py.K_6  or event.key == py.K_8 :
                    if event.unicode in player2_choices:
                        player2_choices.remove(event.unicode)
                        number2 = event.unicode
                        keyboard_counter += 1



        if event.type == py.MOUSEBUTTONDOWN and not check_winner()and keyboard_counter >mouse_counter: #click code
            row = event.pos[1] //200
            col = event.pos[0] //200
            if current_player == 1:
                if check_valid(row, col):
                    turn(row,col,number1)
                    if check_winner() :
                        print(table)
                        break

                    mouse_counter += 1
                    current_player = 2

            elif current_player == 2:
                if check_valid(row, col):
                    turn(row,col,number2)
                    if check_winner():
                        print(table)
                        break

                    mouse_counter += 1
                    current_player = 1
            print(table)



        if event.type==py.KEYDOWN:   #to restart the game
            if event.key== py.K_r:
                player1_choices = ["1", "3", "5", "7", "9"]
                player2_choices = ["0", "2", "4", "6", "8"]
                number1 = ""
                number2 = ""
                display_board()
                table = np.full((3, 3),16)
                current_player = 1

    py.display.update()