import math
from kr import kr

# counts the number of iterations of Kaprekar's routine it takes to get to 6174

def stepCount(x):
    count = 1
    result = kr(x)
    while result != '6174':
        result = kr(result)
        count += 1
    return count
