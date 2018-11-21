#Matthew Zhang
#CS 21, Fall 2018
#number_tree.py

#Recieved help from: Jennifer Courter

'''This program includes a collection of functions which relate to the
structure of pascal's triangle and range from adding all the values of a row
in Pascal's triangle to printing astrisks in a pyramid/triangle shape.'''

'''This function is designed to easily search for a number in pascal's triangle
through means of a row and column value.'''
#((n6-1)/(k3-1))*((n5-1)/(k2-1))*((n4-1)/(k1-1))*1
def get_number(n, k):
    #Ensures that the column number entered is always less than the value of the
    #row number entered.
    if k > n:
        return None
    #When the function reaches the end of the recursion loop, all subsequent
    #values are multiplied by the value of pascal's triangle at column 0, row 0.
    if (k == 0) or (n == k):
        return 1
    #The recursive portion of the function which multiplies the last number
    #value by the next value which is always the last value decreased by 1.
    else:
        return int((n * get_number(n-1, k-1)) / k)

#This function allows users to input a row number from pascal's triangle in
#order to return a value which is the sum of all the numbers in the selected row.
def get_row_sum(i):
    #The num_sum variable is introduced to report the final value.
    num_sum = 0
    #Continuously adds each value in the row of the pascal's triangle by
    #repeatedly calling the get_number function to determine the values which
    #will be added.
    for j in range(i):
        num_sum += get_number(i-1, j)
    return num_sum

#For each row, this function alternates between additon and subtaction of the
#values in the row.
def get_alternating_sum(i):
    alt_sum = 0
    for j in range(i):
        final_val = 0
        if (alt_sum%i == 0):
            alt_sum += get_number(i-1, j)
            final_val += 1
        else:
            alt_sum -= get_number(i-1, j)
            final_val == 0
    return final_val

#Same as get_row_sum but all the added values are squared.
def get_sum_of_squares(i):
    #The sq_sum variable is introduced to report the final value.
    sq_sum = 0
    #Continuously adds each value (which is squared) in the row of the pascal's
    #triangle by repeatedly calling the get_number function to determine the
    #values which will be added.
    for j in range(i):
        sq_sum += (get_number(i-1, j))**2
    return sq_sum
