"""
class Node:
    def __init__(self, left, center, right):
        self.left = left
        self.center = center
        self.right = right

    def set_right(self, right):
        self.right = right
    
    def set_left(self, left):
        self.left = left
    
    def set_center(self, center):
        self.center = center

    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left

    def get_center(self):
        return self.center
"""

def recursive_propagater(num, step):
    remainder = num % 10
    if (num == 1):
        print(step)
        
    elif (is_two_expo(num)):
        recursive_propagater(num / 2, step + 1)
        #print ("Passed in num case 1: " + (num+1))
    
    elif (is_two_expo(num + 1)):
        recursive_propagater(num + 1, step + 1)
        #print ("Passed in num case 2: " + (num+1))
    
    else:
        recursive_propagater(num - 1, step + 1)
        #print ("Passed in num case 3: " + (num+1))
    

def is_two_expo(num):
    remainder = num % 10

    if ((remainder == 2
    or remainder == 4
    or remainder == 6
    or remainder == 8)
    and num % 2 == 0):
        return True
    else:
        return False

def main():
    recursive_propagater(int("15005"), 0)

if __name__ == "__main__":
    main()