#Matthew Zhang
#CS 21, Fall 2018
#archery.py

#Recieved help from: Jennifer Courter

'''This program is a simple target game which functions as a real life dartboard.
Each ring awards the player a different amount of points with the yellow awarding
9, red awards 7, blue awards 5, black awards 3, white awards 1, and anything
outside those rings awards the player no points. To quit this game, the player
must press "q".'''

#Imports necessary graphics and math files for the program to use.
from graphics import *
from math import *

#This function creates the window which displays the target.
def create_target_window():
    #Creates the window, sets its background color and the central coord point.
    mywin = GraphWin("target", 500, 600)
    mywin.setBackground("gray")
    p = Point(250, 250)

    #Draws all the circles for the target.
    c1 = Circle(p, 250)
    c1.setFill("white")
    c1.draw(mywin)
    c2 = Circle(p, 200)
    c2.setFill("black")
    c2.draw(mywin)
    c3 = Circle(p, 150)
    c3.setFill("blue")
    c3.draw(mywin)
    c4 = Circle(p, 100)
    c4.setFill("red")
    c4.draw(mywin)
    c5 = Circle(p, 50)
    c5.setFill("yellow")
    c5.draw(mywin)

    #Returns the "mywin" variable for use in the main function. (It is renamed
    #"win" in the main function).
    return mywin

'''This function takes in the parameter which represents the location of
where the player clicked on the target, and awards the player a certain amt. of
points corresponding to the location of the target that was hit.'''
def get_score(p):

    #Calculates the distance between the center point and where you clicked on
    #the target.
    X = p.getX()
    Y = p.getY()
    distance = abs(sqrt((250-X)**2 + (250-Y)**2))

    #Initializes the variable for the score.      
    arrow_score = 0

    #Awards the player the appropriate amt of points for where the dart hits
    #the board.
    if (distance <= 50):
        arrow_score += 9
    elif (distance <= 100):
        arrow_score += 7
    elif (distance <= 150):
        arrow_score += 5
    elif (distance <= 200):
        arrow_score += 3
    elif (distance <= 250):
        arrow_score += 1
    elif (distance <= 300):
        arrow_score += 0

    #Returns the awarded points to the main function.
    return arrow_score

def main():
    #Creates a graphics window object named win which displays the archery target.
    win = create_target_window()

    #Creates the initial variable for the player points.
    user_p = 0

    #Creates the score display in the target window.
    score = Text(Point(250, 550), 'Current score: 0')
    score.draw(win)
    
    #This loop is necessary in order to allow the program to work without
    #interruptions.
    while True:
        #Checks if you've pressed 'q' to quit the game, then quits the game.
        keystroke =  win.checkKey()
        if keystroke == "q":
            break
        
        #Checks if you've clicked inside the target window.
        p = win.checkMouse()
        if p:
            
            '''Calls the function which calculates the player's score then
            increments the user's score based on the amount of points
            awarded determined by the algorithm in the get_score() function.'''
            user_p += get_score(p)
            #Draws the point where you clicked on the target.
            p.draw(win)

            #Updates the text in target window to show current score.
            score.setText("Current score: " + str(user_p))
    
    #Closes the target window (when the while loop has been broken).
    win.close()
    
