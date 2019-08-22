import math
import csv
import numpy as np
from kapRoutine import kr
from stepCount import stepCount
option = -1
steps = 1

while option != 0:
    print(' ______________________________________________________________ ')
    print('|                                                              |')
    print('| 1 - Create CSV of all 4-digit combos and Kaprekar step count |')
    print('| 2 - Enter a number                                           |')
    print('| 0 - EXIT                                                     |')
    print('|                                                              |')

    option = int(input('| >'))
    print('|______________________________________________________________|')


    if option == 1:
        print(' ______________________________________________________________ ')
        print('|                                                              |')
        print('| Creating CSV...                                              |')
        print('|                                                              |')

        digits = ('0','1','2','3','4','5','6','7','8','9')
        x = []
        y = []

        for a in digits:
            for b in digits:
                for c in digits:
                    for d in digits:
                        if not(a==b and a==c and a==d):
                            x.append(a+b+c+d)

        # for i in x:
        #     for j in x:
        #         if ''.join(sorted(i)) == ''.join(sorted(j)) and i != j:
        #             x.remove(i)
        #             break

        # Remove permutations from x
        i = 0
        while i < len(x):
            for j in x:
                if ''.join(sorted(x[i])) == ''.join(sorted(j)) and x[i] != j:
                    x.remove(x[i])
            i += 1 

        # Create step count in y
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
    
        print('| CSV created.                                                 |')
        print('|______________________________________________________________|')
        option = -1


    if option == 2:
        ########ENTER ONE AT A TIME:
        print(' ______________________________________________________________ ')
        print('|                                                              |')
        print('| Input a four digit number where all digits are not the same  |')

        option = 0
        while option == 0:
            x = input('| >')
            digits = int(math.log10(int(x))+1)
            if digits != 4:
                print('| This is',digits,'digits. This number is needs to be 4 digits.')

            if digits != 1:
                if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
                    print('| These digits are not unique')

            if digits == 4 and not(x[0] == x[1] and x[1] == x[2] and x[2] == x[3]):
                option = 2
  
        if option == 2:
            result = kr(x)
            print('|\t\t\t',steps,'\t',result,'\t\t\t|')
            while result != '6174':
                result = kr(result)
                steps = steps + 1
                print('|\t\t\t',steps,'\t',result,'\t\t\t|')
            steps = 1
        
        print('|______________________________________________________________|')
        option = -1






