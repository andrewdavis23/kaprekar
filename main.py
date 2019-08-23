import math
import csv
import numpy as np
from kapRoutine import kr
from stepCount import stepCount
option = -1
steps = 1

while option != 0:
    print(' _______________________________________________________________ ')
    print('|                                                               |')
    print('| 1 - Create CSV                                                |')
    print('| 2 - Enter a number                                            |')
    print('| 0 - EXIT                                                      |')
    print('|                                                               |')

    option = int(input('| >'))

    if option == 1:
        print('Creating CSV...')

        digits = ('0','1','2','3','4','5','6','7','8','9')
        x = []
        y = []

        # Create all four digit combos in x
        for a in digits:
            for b in digits:
                for c in digits:
                    for d in digits:
                        if not(a==b and a==c and a==d):
                            x.append(a+b+c+d)

        # Remove permutations from x
        i = 0
        while i < len(x):
            for j in x:
                if ''.join(sorted(x[i])) == ''.join(sorted(j)) and x[i] != j:
                    x.remove(x[i])
            i += 1 

        # Create step count in y = stepCount(x)
        for i in x:
                y.append(stepCount(i))
                i = int(i)

        # # Stips padded zeroes from x
        # i = 0
        # while i < len(x):
        #         x[i] = x[i].lstrip('0')
        #         i += 1

        # Write to CSV
        csvData = np.concatenate((np.array([x]),np.array([y])),axis=0)
        csvData = csvData.transpose()
        with open('stepCount.csv','w') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(csvData)
    
        print('CSV created.')
        option = -1


    if option == 2:
        print('| Input a four digit number where all digits are not the same')

        option = 0
        while option == 0:
            inNum = input('| >')
            digits = int(math.log10(int(inNum))+1)
            if digits != 4:
                print('| This is',digits,'digits. This number is needs to be 4 digits.')

            if digits != 1:
                if inNum[0] == inNum[1] and inNum[1] == inNum[2] and inNum[2] == inNum[3]:
                    print('| These digits are all the same. At least one needs to be different.')

            if digits == 4 and not(inNum[0] == inNum[1] and inNum[1] == inNum[2] and inNum[2] == inNum[3]):
                option = 2
  
        if option == 2:
            print('|\t\t\t','Step','\t','Result','\t\t\t|')
            print('|\t\t\t','0','\t',inNum,'\t\t\t\t|')
            result = kr(inNum)
            print('|\t\t\t',steps,'\t',result,'\t\t\t\t|')
            while result != '6174':
                result = kr(result)
                steps = steps + 1
                print('|\t\t\t',steps,'\t',result,'\t\t\t\t|')
            steps = 1
        
        option = -1






