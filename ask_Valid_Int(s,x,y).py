

'''
    
    Sometimes we need to take integer as input from the user but user might not give an integer as an input.
    This function will ask and ask until they enter integer within given range (if the range is given, otherwise any integer).

    Here, 
            s = the 'prompt' statement/question given by the programmer.
            x = the lower-limit of the range
            y = the upper-limit of the range

    I will show you examples for both with range and without range:

        With Range:
                    *suppose you are asking user to choose an option from 1 to 4. that means any input other than 1 or 2 or 3 or 4 would be INVALID*
                    *At this situation you can ask "Choose an option: " then get input from user within the range*

                    user_input = ask_Valid_Int("Choose an option: ", 1, 4)

        Without Range:
                    *suppose you want to get the value of "P" from user. it can be any integer*

                    user_input = ask_Valid_Int("Enter the value of P : ")



===========================================================================================================================================
'''





def ask_Valid_Int(s, x=None, y=None):  # this function will retrun when user input is integer and also in the range of x <= input <= y
    while True:
        temp = input(s)
        try:
            if not is_Digit(temp) or y < int(temp) or int(temp) < x:    # to use this function you have to add "is_Digit(n)" function, that's given below
                print("\t **Invalid Input !!\n") 
            else:
                return int(temp)
        except TypeError:
            if not is_Digit(temp):    # to use this function you have to add "is_Digit(n)" function, that's given below
                print("\t **Invalid Input !!\n") 
            else:
                return int(temp)
        






#===========================================================================================================================================
#===========================================================================================================================================








# it's "is_Digit(n)" function, this function takes any type of variable and checks if thats digit or not. 

def is_Digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False




