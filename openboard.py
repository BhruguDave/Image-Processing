# Opening Saved File Drawn in drawingboard.py

import cv2 as cv
import numpy as np

array_string = []

#Fetching Saved Progress
def opening_file():
    file = open("drawing.txt","r")
    data = file.readlines()
    for line in data:
        word = line.rstrip()
        word = word.split(' ')
        for ele in word:
            if(ele != ' '):    
                if(ele.isnumeric() == False):
                    array_string.append(ele)
                else:
                    array_string.append(int(ele))


# Creating Saved Drawing Board
def creating_board():
    for i in range(len(array_string)):
        if(array_string[i] == "]"):
            break
        elif(array_string[i] == "c"):
            cv.circle(board, (array_string[i+1], array_string[i+2]),5,(255,0,0),-1)
        elif(array_string[i] == "r"):
            cv.rectangle(board, (array_string[i+1],array_string[i+2]),(array_string[i+3],array_string[i+4]),(0,255,0),-1)
        elif(array_string[i] == "l"):
            cv.line(board, (array_string[i+1],array_string[i+2]),(array_string[i+3],array_string[i+4]),(0,0,255),5)



#Creating New Board
board = np.zeros((512,512,3), np.uint8)

for i in range(3):
    for j in range(512):
        for k in range(512):
            board[j,k,i] = 255

cv.namedWindow("Drawing Board")

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(board,"c->Circle r->Rectangle l->Straight Line esc->Exit",(10,25),font,0.5,(0,0,0),2,cv.LINE_AA)

opening_file()
creating_board()

#Displaying Board
cv.imshow("Drawing Board",board)
cv.waitKey(0)


cv.destroyAllWindows()