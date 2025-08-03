### CSC6023 Module 07 - Programming Assignment
### Copyright Alexander Medeiros 03/01/2024

"""
This program is designed to determine a local maximum value within an array of values.

Methods:    
    generate_array(length): - arguments are a value for the length of the array to generate. The method will generate a list of 'x_values' using the length. 
        The function will call the method 'myFunction(x)' where x is each value in the array, and output a value y = myFunction(x). Each value y will be populated into a 
        list of 'y_values'. The values of each list are returned. 

    myFunction(x): - arguments are an integer value. A value is provided to the method, and based on conditions within the method, a value will be returned. This method is used by 
        the 'generate_array()' method to populate an array for the hill climbing algorithm.

    hillClub(arr, start_index): - arguments are an array of values and an integer starting value. The method will receive an array of values generated using myFunction(x) and a start
        index position. The program will loop and compare a value at a position in the array with its neighbors. Based on conditions within the method, the method will seek a maximum 
        value and update the index based on which direction the values are increasing relative to the compared current index value. When a maximum condition is met, 
        the loop will break and the program will return the local_maximum_index, and local_maximum_value. 

    main(): - method generates an array of 10000 x_values from 0-9999, provides those x_values to myFunction(x) to generate a list of y_values and store them in an variable called 
        'arr'. The program will generate a random number between 1-9998, and store that value in a variable called 'start_index'. The array 'arr' and value 'start_index' are provided
        to the 'hillClimb(arr,start_index)' method. The list is traversed and a local maximum is determined. The index of the local maximum and the value of the local maximum is the
        output. Both values are printed to display for the user. 


"""
# Import modules
from math import *
import matplotlib.pyplot as plt
import random
import numpy as np

# method to produce a value y=myFunction(x) given an x value as define dy the assignment
def myFunction(x):

    if ( x == 0 ):
        return 0
    
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x))**3
    
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2)**3
    
    else:
        return (log2(x)**2) - x

# method to generate an array of x_values from 0-9999, and compute the y-values using myFunction(x) and store them in an array
def generate_array(length):
    x_values = [] # empty list for x values

    for i in range(length): # for loop length of array
        
        x_values.append(i) # append the index values for length of the array

    y_values = [] # empty list for y values

    for x in x_values:
        y_values.append(myFunction(x)) # provide each x value in 'x_values' to myFunction and append the output to the list 'y_values'

    return x_values, y_values # return both lists

# method to find a local maximum value in a list of numbers, argument is an array and starting index
def hillClimb(arr, start_index):

    # initialize the local_max_index, local_max_value
    local_maximum_index, local_maximum_value, = start_index, arr[start_index]

    # initialize the climb_index 
    climb_index = start_index

    # initialize the previous_index
    previous_index = None

    # run while loop till condition is met to break out    
    while True:
                     
        # if left and right exist
        if climb_index - 1 >= 0 and climb_index + 1 <= len(arr)-1: # if there is a value within the array to both the left and the right of the current value
            
            left_slope = abs(arr[climb_index] - arr[climb_index-1]) # find the slope to the left of the current value

            right_slope = abs(arr[climb_index] - arr[climb_index+1]) # find the slope to the right of the current value

            # if in a valley
            if arr[climb_index - 1] > arr[climb_index] < arr[climb_index + 1]: # if the value to the left and to the right of the current value are larger....
                # print('valley')

                # if increase to the left is greater than increase to the right, move left
                if left_slope > right_slope:
                    previous_index = climb_index # set previous index to the current index
                    climb_index = climb_index - 1 # set the index to the left of the current
                    local_maximum_index, local_maximum_value, = climb_index, arr[climb_index] # return the index and the value

                # if increase to the left is smaller than increase to the right, move right
                elif left_slope < right_slope:
                    previous_index = climb_index # set previous index to the current index
                    climb_index = climb_index + 1 # set the index to the right of the current
                    local_maximum_index, local_maximum_value, = climb_index, arr[climb_index] # return the index and the value
                
                # otherwise default move right, happens the increase on both sides is equal
                else:
                    previous_index = climb_index
                    climb_index = climb_index + 1
                    local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]

            # if in a peak, return result
            if arr[climb_index - 1] < arr[climb_index] > arr[climb_index + 1]: # if the value to the left of the current value is smaller, and the value to the right is smaller, return current
                # print('max')

                local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]
                return local_maximum_index, local_maximum_value
            
            # if left is equal and right is less, move left
            if arr[climb_index-1] == arr[climb_index] > arr[climb_index+1]: # if the value to the left of the current value is equal, and the value to the right is larger, move right

                if previous_index is None: # if starting on a flat
                    previous_index = climb_index
                    climb_index -=1

                # if previous index is bouncing it back, return the result
                if previous_index < climb_index:
                    local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]
                    return local_maximum_index, local_maximum_value

                # print('left')
                previous_index = climb_index
                climb_index = climb_index - 1
                local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]

            # is right is equal and left is less, move right
            if arr[climb_index-1] < arr[climb_index] == arr[climb_index+1]:

                # if starting on a flat
                if previous_index is None: 
                    previous_index = climb_index
                    climb_index +=1

                # if previous index is bouncing it back, return the result
                if previous_index > climb_index:
                    local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]
                    return local_maximum_index, local_maximum_value
                
                # print('right')
                previous_index = climb_index
                climb_index = climb_index + 1
                local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]

            if arr[climb_index-1] == arr[climb_index] == arr[climb_index+1]: # if on a flat shoulder

                # print('equal')

                # if starting on a flat, default moving right
                if previous_index is None: 
                    previous_index = climb_index
                    climb_index += 1
                    
                # if the value left and right are equal, and previously moving to the right
                if previous_index < climb_index:
                    previous_index = climb_index
                    climb_index = climb_index + 1
                    local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]
                
                # if the value left and right are equal, and previously moving to the left
                if previous_index > climb_index:
                    previous_index = climb_index
                    climb_index = climb_index - 1
                    local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]

        # search right
        if climb_index + 1 <= len(arr)-1: # if index to the right of current value is within the length of the array

            # only if values are bigger going right
            if arr[climb_index] < arr[climb_index + 1]: # if the value at the climb index is less than the value to its right in the array
                # print('right')
                previous_index = climb_index
                climb_index = climb_index + 1
                local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]
                 

        # search left
        if climb_index - 1 >= 0: # if the index to the left of the current value is within the length of the array

            # only if values are bigger going left
            if arr[climb_index] < arr[climb_index - 1]: 
                # print('left')
                previous_index = climb_index
                climb_index = climb_index - 1
                local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]
          

        # if at the end of an array, this case is called last and will not be called if starting on the end of a list unless the end is a local max          
        if climb_index == 0 or climb_index == len(arr)-1:
            local_maximum_index, local_maximum_value, = climb_index, arr[climb_index]
            return local_maximum_index, local_maximum_value

        
        # return local_maximum_value, local_maximum_index, loop

# method to call primary functions of program 
def main():

    ### Test cases - for debugging ###
    #arr = [1,2,3,4,5,6,7] ## works ascending right
    #arr = [7,6,5,4,3,2,1] ## works ascending left
    #arr = [1,2,3,4,3,2,1] ## works with local max
    #arr = [4,3,2,1,2,3,4] ## works with local min, defaults right when starting at min with equal slopes
    #arr = [6,5,5,5,4,3,2]  # pass
    #arr = [2,5,5,5,4,3,2]  # pass, ends on index 3 when starting before index 3, ends on index 1 when starting after index 3
    #arr = [5,4,3,1,2,3,4] # valley with greater slope on left
    #arr = [4,3,2,1,3,5,6] # valley with greater slope on right
    # local_maximum_index, local_maximum_value = hillClimb(arr,1)
    # print(f'Index = {local_maximum_index},value = {local_maximum_value}')

    # generate an array of x_values from 0-9999, and use these values to compute y_value = myFunction(x) for each item in the x_values list
    x_values, y_values = generate_array(10000)

    # list of values generated by myFunction(x), this is provided to the hillClimb algorithm
    arr = y_values

    # pick a random starting index between 1-9998, this is provided to the hillClimb algorithm
    start_index = random.randint(1,9998)

    # run the hill climbing algorithm on array 'arr', using a random starting position 'start_index'
    local_maximum_index, local_maximum_value = hillClimb(arr,start_index)

    print(f'Local Maximum Index = {local_maximum_index}, Local Maximum Value = {local_maximum_value}')

    # #plot the array values, and the final selection from the hill climb algorithm, for debugging
    # plt.plot(np.array(x_values), np.array(y_values))
    # plt.plot(local_maximum_index,local_maximum_value,'ro')
    # plt.show()

    # plt.plot(np.array(x_values[(local_maximum_index-10):(local_maximum_index+10)]), np.array(y_values[(local_maximum_index-10):(local_maximum_index+10)]))
    # plt.plot(local_maximum_index,local_maximum_value,'ro')
    # plt.show()
    
if __name__=="__main__":
    main()
