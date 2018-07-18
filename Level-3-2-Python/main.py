from fractions import Fraction

def main(m):
    dimension = len(m)
    matrix, num_absorbing_state = preprocess_matrix(m)
    matrix = convert_canonical(matrix)
    identity = generate_identity(dimension - num_absorbing_state)
    
    result = matrix_subtract(identity, get_Q(matrix, dimension - num_absorbing_state))
    result = getMatrixInverse(result)
    result = multiply(result, get_R(matrix, dimension - num_absorbing_state))
    result = sum_column(result)
    
    result = convert_fraction(result)
    return result

def convert_fraction(matrix):
    result = []
    for element in range(len(matrix)):
        result[element] = Fraction(matrix[element].as_integer_ratio())
    return result

def preprocess_matrix(matrix):
    num_absorbing_state = 0;

    for row in range(len(matrix)):
        if not if_all_zero(matrix[row]):
            denominator = sum_array(matrix[row])
            for element in range(len(matrix[row])):
                if element != 0:
                    row[element] = matrix[row][element] / denominator
        else:
            num_absorbing_state = num_absorbing_state+1
    return matrix, num_absorbing_state

def convert_canonical(matrix):
    for row in range(len(matrix)):
        if if_all_zero(matrix[row]):
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

def matrix_subtract(matrixA, matrixB):
    for row in range(len(matrixA)):
        for element in range(len(row)):
            matrixA[row][element] = matrixA[row][element] - matrixB[row][element]
    return matrixA

def generate_identity(dimension):
    matrix = [[0 for x in range(dimension)] for y in range(dimension)] 
    for row in range(len(dimension)):
        for element in range(len(row)):
            if row == element:
                matrix[row][element] = 1
            else:
                matrix[row][element] = 0
    return matrix

def multiply(a, b):
    m = []
    rows = len(a)
    cols = len(b[0])
    iters = len(a[0])

    for r in range(rows):
        mRow = []
        for c in range(cols):
            sum = 0
            for i in range(iters):
                sum += a[r][i]*b[i][c]
            mRow.append(sum)
        m.append(mRow)
    return m

def getMatrixInverse(m):
    d = getMatrixDeternminant(m)

    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/d, -1*m[0][1]/d],
                [-1*m[1][0]/d, m[0][0]/d]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/d
    return cofactors

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))

    return d

def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def get_Q(matrix, num_transient):
    result = []
    for row in range(len(num_transient)):
        for element in range(len(num_transient)):
            result[row][element] = matrix[row][element]
    return result

def get_R(matrix, num_transient):
    result = []
    for row in range(len(num_transient)):
        for element in range(num_transient, len(matrix[0])):
            result[row][element] = matrix[row][element]
    return result

def sum_column(matrix):
    result = []
    for row in range(len(matrix)):
        for element in range(len(matrix[0])):
            result[element] = result[row][element] + matrix[row][element]
    return result