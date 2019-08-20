import math
import csv
import numpy as np
from kr import kr
from stepCount import stepCount

digits = ('0','1','2','3','4','5','6','7','8','9')
x = []
y = []

for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                if not(a==b and a==c and a==d):
                    x.append(a+b+c+d)

for i in x:
        y.append(stepCount(i))

csvData = np.concatenate((np.array([x]),np.array([y])),axis=0)
print(csvData.shape)
print(csvData)

i = 0
while i < len(x):
        csvData.append(x[i] + ',' + str(y[i]))
        i += 1

with open('stepCount.csv','w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)


# Kaprekar's Routine:
# result = kr(x)
# stepCount = 1
# print(stepCount,"\t",result)
# while result != '6174':
#         result = kr(result)
#         stepCount = stepCount + 1
#         print(stepCount,"\t",result)


#########ENTER ONE AT A TIME:

# print('Input a four digit number\nWhere all digits are not the same')
# x = input()

# digits = int(math.log10(int(x))+1)

# if digits != 4:
#     print('This is',digits,'digits. This number is needs to be 4 digits.')
#     quit()

# if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
#     print('These digits are not unique')
#     quit()

# result = kr(x)
# print(result)
# while result != '6174':
#         result = kr(result)
#         print(result)






