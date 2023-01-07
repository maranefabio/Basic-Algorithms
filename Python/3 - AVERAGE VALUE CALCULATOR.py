#This program, with the help of Numpy, returns the average of the given numbers. It also returns the sum of the numbers, the biggest and smallest ones, the variance, the standard deviation and a plot of the numbers, with matplotlib. The program only accepts numerical values, and ends the count when an string value is given.

import numpy as np
import matplotlib.pyplot as plt
import math
from termcolor import cprint, colored
import os


#Defining functions for stylized printing with the termcolor library
print_yellow = lambda x: cprint(x, 'yellow', attrs = ['blink'])
print_cyan = lambda x: cprint(x, 'cyan', attrs = ['bold'])    
print_green = lambda x: cprint(x, 'green')
print_blue = lambda x: cprint(x, 'blue')
print_red = lambda x: cprint(x, 'red', attrs = ['bold'])

#Determining the size of the terminal with the library OS
c = os.get_terminal_size().columns                          

#Defining the user input list and a Numpy array for storage                                        
def Avg(n = [], a = np.array([])):                   
    print_red('******************** STATISTICS CALCULATOR :) ********************'.center(c))
    print_cyan('This program calculates the average, variance and standard deviation of all the given numbers.'.center(c))
    #Showing the ending mechanism to the user    
    print_yellow('Instructions:  Input one number at a time. To stop the count, just press ENTER without writing anything'.center(c)), 
    print(''.center(c, '-'))

    try :                                                   #try/except construction for continuous storage, until a string value is given 
        while True:
            k = float(input('Input number = '))             #Only float types are stored inside the list
            n.append(k)                                     #Appending to the list
    except ValueError:                                      #Constraint to string values
        print(''.center(c, '-'))
        print_red('{}'.format('Results :D\n').center(c))

    #After the exception is achieved, the elements of the list are appended to a Numpy array                           
    for i in range(len(n)):                                 
        a = np.append(a, n[i])

    s = np.sum(a)                                           #Sum of all the numbers                 
    avg = s/(len(a))                                        #Average value
    b = np.max(a)                                           #Biggest number
    l = np.min(a)                                           #Smallest number

    #Calculus for the variance
    v = 0
    for i in range(len(a)):
        v += ((a[i]-avg)**2)/(len(a)) 

    #Standard deviation
    d = math.sqrt(v)

    #Separate printing for avoiding color deformatting
    return(
        print_yellow('{:>70} - Given numbers:  {}\n'.format('', n)),
        print_green('{:>70} - Sum of all given numbers =  {}'.format('', s)), 
        print_blue('{:>70} - Average value =  {}'.format('', avg)),
        print_green('{:>70} - Variance =  {}'.format('', v)),
        print_blue('{:>70} - Standard Deviation =  {}'.format('', d)),
        print_green('{:>70} - Smallest given number =  {}'.format('', l)),
        print_blue('{:>70} - Biggest given number =  {}'.format('', b))
        )
        
Avg()