#This program, with the help of Numpy, returns the average of the given numbers. It also returns the sum of the numbers and the biggest and smallest ones. The program only accepts numerical values, and asks for retry if the input is alphabetic. The program recognizes the string "stop", with lower and upper cases, as a flag to stop the count and compute the needed values.

import numpy as np

def Avg(n = str, a = np.array([])):
    print('Write as many numbers as you wish. The program will give you the average of the numbers and show the biggest and smallest of them. To stop, just write "Stop".')
    while True:
        n = input('Number:')
        if n.isnumeric() == True:
            a = np.append(a, float(n))
        elif n.lower() == 'stop':
            break
        else:
            n = input('Only numbers accepted. Try again.\nNumber: ')
    A = a[:-1]
    s = np.sum(A)
    avg = s/(len(A))
    b = np.max(A)
    l = np.min(A)
    return print(
        'The sum of all given numbers is {}\nThe average is {}\nBiggest number: {}\nSmallest number:{}'
        .format(s, avg, b, l))
Avg()