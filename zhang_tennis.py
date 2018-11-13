#Matthew Zhang
# CS 21, Oct 2018
#tennis.py

#Recieved help from: Trevor Cardoza & Jennifer Courter

'''This program allow the user to play as many games of tennis against the PC as
desired and lets the user decide how much of a winning advantage they want over
the PC.'''

#Imports random to stand in as the "player_b".
from random import random

#This function prints the intro and basic info of the program.
def print_intro():
    print("Welcome to tennis. This program allows you to play as many games of")
    print("tennis against the PC as you want and lets you decide how much of a")
    print("winning advantage you want over it.")

#This function scores the points for each round of tennis played.
def play_game(prob_a):
    #This list is used as a reference for the amount of points in tennis.
    points = ["0", "15", "30", "40", "Win"]
    points_deuce = ["deuce", "advantage", "Win"]
    #Scores A & B are intialized here.
    A = 0
    B = 0
    #This loop keeps playing the tennis games until a winner has been decided.
    while True:
        #If player A or B wins, then the while true loop is broken.
        if(A == 4 or B == 4):
            break
        #If both players reach the score of 40, then the score is a deuce.
        if(A == 3 and B == 3):
            print("Current score: deuce")
            #Resets the player scores.
            A = 0
            B = 0
            #This while loop plays deuce for both players.
            while True:
                if(A == 2 or B == 2):
                    if A == 2:
                        return "A"
                    if B == 2:
                        return "B"
                if(prob_a > random()):
                    A += 1
                    print("Current score:", points_deuce[A], "Player A")
                else:
                    B += 1
                    print("Current score:", points_deuce[B] ,"Player B")
            break
        #If the PC wins.
        if(random() < prob_a):
            A += 1
            #Prints the current score after each round of the game is played.
            print("Current score:", points[A], "-", points[B])
        #If your probability wins.
        else:
            B += 1
            #Prints the current score after each round of the game is played.
            print("Current score:", points[A], "-", points[B])
    #If you win the game, then A as the "win" value in the play games function.
    if(A == 4 or A == 2):    
        return "A"
    #If the PC wins the game, then A as the "win" value in the play games function.
    elif(B == 4 or B == 2):
        return "B"
    

def play_games(num_games, prob_a):
    #Intializes the variable which counts the number of games that've
    #been played.
    g = 0
    #These 2 variables initialize the counter for the games player A
    #or B have won.
    num_a_wins = 0
    num_b_wins = 0
    #This loop will keep running for the amount of games you want to play
    #and will return the value for the number of times each player has won.
    while True:
        #Counts the number of times the game has been played.
        if (g < num_games):
            win = play_game(prob_a)
            print("Winner:", win)
            if(win == "A"):
                num_a_wins += 1
            elif(win == "B"):
                num_b_wins += 1
            g += 1
        #Once the program reaches the amt. of games the user wants to play.
        elif (g == num_games):
            #Stops the while loop.
            break
    #Returns the values for the amount of times players A & B have won.
    return num_a_wins, num_b_wins


#This function gets all necessary inputs from the user.
def get_inputs():
    #This loop asks the user how many games they want to play and ensures
    #that only an integer value is entered.
    while True:
        try:
            num_games = int(input("Enter the number of games you'd like to play: "))
            #If there's no problems with your number and it's positive.
            if (num_games > 0):
                break
            #If your number is negative, then an error message pops up.
            else:
                print("ERROR: YOUR NUMBER OF GAMES IS LESS THAN 1")
        #If the entered value is not an integer, then an error message pops up.
        except ValueError:
            print("ERROR: YOUR PLAY GAMES IS NOT AN INT")
    #This loop asks the user the percentage of winning luck they'd like and ensures
    #that only an float value is entered.
    while True:
        try:
            prob_a = float(input("Enter the probability that you'd win against the PC: "))
            #If there's no problems with your number and it's between or equal to
            #0 and 1.
            if (prob_a >= 0 and prob_a <= 1):
                break
            #If your value is not equal to or between 0 and 1, then an error
            #pops up.
            else:
                print("ERROR: YOUR PROBABILITY VALUE IS EITHER LESS THAN 0 OR GREATER THAN 1")
        #If your entered value is not a float, then an error msg pops up.
        except ValueError:
            print("ERROR: YOUR PROBABILITY IS NOT A FLOAT")
    #Returns the values for the number of games and the user's chance of winning
    #to the main function.
    return num_games, prob_a

#This function prints the summary of the user's wins, the PC's wins, and the
#percentage of games the player won.
def print_summary(num_a_wins, num_b_wins):
    #Prints the number of games won by the user and PC.
    print("Player A won", num_a_wins, "games.")
    print("Player B won", num_b_wins, "games.")

    #Calculates the percentage of games won by the user.
    percentage_won = ((num_a_wins) / (num_a_wins + num_b_wins)) * 100
    print("Player A won", percentage_won, "% of the games")

#This function calls all necessary functions and organizes the values which it
#recieves from those functions in order to push those values to any other
#necessary functions.
def main():
    print_intro()
    num_games, prob_a = get_inputs()
    num_a_wins, num_b_wins = play_games(num_games, prob_a)
    print_summary(num_a_wins, num_b_wins)

#This executes the main function when the program starts.
main()
