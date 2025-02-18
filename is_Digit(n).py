
# it's "is_Digit(n)" function, this function takes any type of variable and checks if thats digit or not. 

def is_Digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False