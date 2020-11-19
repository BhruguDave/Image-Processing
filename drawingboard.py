#kaik banavano try

import cv2 as cv
import numpy as np


flag = 0
draw = False
ix, iy = -1,-1
mode = 0
array_string = []

#file = open("Drawing.txt","w")

#Drawing Action
def draw_action(event,x,y,flags,param):
    global draw,ix,iy,mode
    #print("Step 1")
    if event == cv.EVENT_LBUTTONDOWN:
        #print("Button Down")
        draw = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        #print("Mouse move")
        if draw == True:
            if mode == 0:
                #print("Circle if")
                cv.circle(board, (x,y),5,(255,0,0),-1)
                board_data("c" + " " + str(x) + " " + str(y)) # saving circles
                #file.write("\n")
            elif mode == 1:
                #print("Rect if")
                cv.rectangle(board, (ix,iy),(x,y),(0,255,0),-1)
            elif mode == 2:
                #print("Line if")
                cv.line(board, (x,y),(ix,iy),(0,0,255),5)
    elif event == cv.EVENT_LBUTTONUP:
        #print("Button up")
        draw = False
        if mode == 0:
            cv.circle(board, (x,y),5,(255,0,0),-1)
            #file.write("c" + " " + str(x) + " " + str(y))
            #file.write("\n")
            board_data("c" + " " + str(x) + " " + str(y))
        elif mode == 1:
            cv.rectangle(board, (ix,iy),(x,y),(0,255,0),-1)
            board_data("r"+ " " + str(ix) + " "+ str(iy) + " "+ str(x) + " "+ str(y))
            #file.write("r"+ " " + str(ix) + " "+ str(iy) + " "+ str(x) + " "+ str(y) +" ") # saving rectangles
            #file.write("\n")
        elif mode == 2:
            cv.line(board, (x,y),(ix,iy),(0,0,255),5)
            board_data("l"+ " " + str(ix) + " "+ str(iy) + " "+ str(x) + " "+ str(y))
            #file.write("l"+ " " + str(ix) + " "+ str(iy) + " "+ str(x) + " "+ str(y) +" ") # saving lines
            #file.write("\n")
    else:
        print("Unknown event")


#Saving Process (Brute Force)
#def write_file(workspace):

#    print("Filed Opened")
#    file = open("Drawing.txt","w")
#    print("Starting Printing")
#    file.write("[")
#    for i in range(512):
#        for j in range(512):
#            a = np.array(workspace[i][j])
#            str = np.array2string(a)
#            file.write(str)
#
#    file.write("]")
#    print("File Closing")
#    file.close()
#


# Collecting Data from Drawing Board
def board_data(str):
    array_string.append(str)


#Writing File That Contains Drawing Board Properties
def write_to_file(workspace):
    file = open("drawing.txt","w")
    for s in array_string:
        file.write(s)
        file.write("\n")

    file.write("]")
    file.close()


# Driver Code

if(flag == 0):
    board = np.zeros((512,512,3), np.uint8)

    for i in range(3):
        for j in range(512):
            for k in range(512):
                board[j,k,i] = 255

    cv.namedWindow("Drawing Board")
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(board,"c->Circle r->Rectangle l->Straight Line esc->Exit",(10,25),font,0.5,(0,0,0),2,cv.LINE_AA)


cv.setMouseCallback("Drawing Board",draw_action)

while(1):
    cv.imshow("Drawing Board",board)
    k = cv.waitKey(1) & 0xFF
    if k == ord('c'):
        mode = 0
        cv.putText(board,"circle Mode",(10,35),font,1,(0,0,0),1,cv.LINE_AA)
    elif k == ord('r'):
        mode = 1
        cv.putText(board,"Rectangle Mode",(10,35),font,1,(0,0,0),1,cv.LINE_AA)
    elif k == ord('l'):
        mode = 2
        cv.putText(board,"Line Mode",(10,35),font,1,(0,0,0),1,cv.LINE_AA)
    elif k == 27:

        #file.write("]")
        #print("Saving............")
        #file.close()
        #print("Saved")
        
        #print(array_string)

        print("...........SAVING...........")
        write_to_file(board)
        print("...........SAVED............")
        flag = 1

        break
cv.destroyAllWindows()