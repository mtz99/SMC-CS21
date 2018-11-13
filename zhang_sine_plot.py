# Matthew Zhang
# CS 21, Fall 2018
# Program: sine plot

"""
    Module description:
    
    This program allows the user to select how they would like
    to have the sine wave graphed. Either as a vertical or horizontal axis
    and also either between 0 and pi or 0 and 2pi.
"""

# Bring in libraries to get access to functions.
import math
import sys

#Define the main function.
def main():
    # Set the number of lines used to plot the sine function between 0 and pi.
    x_resolution = 32

    # Set a value that helps to determine the height of the "bump".
    y_resolution = 25

    while(True):
        # Ask the user for a solution choice.
        print("\n")
        print("The following graphs of the sine function are available: ")
        print("1. Graph between 0 and pi using a vertical x-axis")
        print("2. Graph between 0 and 2*pi using a vertical x-axis")
        print("3. Graph between 0 and pi using a horizontal x-axis")
        print("4. Graph between 0 and 2*pi using a horizontal x-axis")    
        print("5. Quit the program")
        print("\n")
        num_soln = int(input("Enter the number of the solution you want: "))
        print("\n")
       
        if num_soln == 1:
        
            # Print out the sine curve between 0 and pi
            # using a vertical x-axis.
            
            # For each line...
            for n in range(x_resolution):
                # ... find the x-value for this line and corresponding y-value.
                x = (n * math.pi) / x_resolution
                y = math.sin(x)

                # Create and print dots that represent the area between the
		# x-axis and the height of function. 
                bar = ''
                for m in range(int((y * y_resolution)-1)):
                    bar += ' '
                print (bar + '*')
            
        elif num_soln == 2:
            # Print out the sine curve between 0 and 2pi
            # using a vertical x-axis.
            
            # For each line...
            for n in range(x_resolution):
                # ... find the x-value for this line and corresponding y-value.
                x = (2 * (n * math.pi)) / x_resolution
                y = math.sin(x) + 1.5

                # Create and print dots that represent the area between the
		# x-axis and the height of function.
                bar = ''
                for m in range(int((y * y_resolution)-1)):
                    bar += ' '
                print (bar + '*')
            
        elif num_soln == 3:
            # Print out the sine curve between 0 and pi
            # using a horizontal x-axis.

            # For each line...
            for n in range(y_resolution):
                # ... find the x-value for this line and corresponding y-value.
                x = (n * math.pi) / x_resolution
                y = math.sin(x)

                # Create and print dots that represent the area between the
		# x-axis and the height of function.
                bar = ''
                for m in range(int((x * x_resolution)-1)):
                    bar += ' '
                print (bar + '*')
            
        elif num_soln == 4:
            # Print out the sine curve between 0 and 2pi
            # using a horizontal x-axis.
            
            # For each line...
            for n in range(y_resolution):
                # ... find the x-value for this line and corresponding y-value.
                x = (2 * (n * math.pi)) / x_resolution
                y = math.sin(x) + 1.5

                # Create and print dots that represent the area between the
		# x-axis and the height of function.
                bar = ''
                for m in range(int((x * x_resolution)-1)):
                    bar += ' '
                print (bar + '*')
                  
        elif num_soln == 5:

            # Quit the program

            exit()
            
# Run the main function.
main()
