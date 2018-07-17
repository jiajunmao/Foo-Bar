class fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def add(self, target):
        common_denom = self.denominator * target.denominator
        
        # Adding them together
        self.numerator = self.numerator * common_denom / self.denominator
        self.denominator = common_denom
        
        target.numerator = target.numerator * common_denom / target.denominator
        target.denominator = common_denom

        # Simplifying the fraction
        divisor = gcd(self.denominator, self.numerator)
        if (divisor != 1):
            self.denominator = self.denominator/divisor
            self.numerator = self.numerator/divisor
        
        divisor = gcd(target.denominator, target.numerator)
        if(divisor != 1):
            target.denominator = target.denominator/divisor
            target.numerator = target.numerator/divisor
    
    def multiply(self, target):
        self.denominator = self.denominator * target.denominator
        self.numerator = self.numerator * target.numerator

        divisor = gcd(self.denominator, self.numerator)
        if(divisor != 1):
            self.denominator = self.denominator/divisor
            self.numerator = self.numerator/divisor
        

def main(m):
    matrix = preprocess_matrix(m)
    

def preprocess_matrix(matrix):
    for row in range(len(matrix)):
        if not if_all_zero(matrix[row]):
            denominator = sum_array(matrix[row])
            for element in range(len(matrix[row])):
                if element != 0:
                    row[element] = fraction(row[element], denominator)
        else:
            matrix[row][row] = 1
    return matrix
    
def if_all_zero(array):
    for i in array:
        if i != 0:
            return False
    return True

def sum_array(array):
    sum = 0
    for element in array:
        sum = sum + element
    return sum

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a%b)
    return a