#This program returns the average, variance and standard deviation of the given numbers. It also returns a distribution plot, with Seaborn and MatPlotLib. The program only accepts numerical values, and ends the count when an string value is given.

import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
from collections import Counter
import os

#Defining the plotting function
def plot(l = np.array([]), a = float, v = float, d = float, m = float, M = float):
    y = list(Counter(l).values())                                   #Finding the number of occurrences of the most common number
    sns.set_theme(style = "ticks", palette = 'pastel')              #Seaborn themes
    sns.histplot(data = l,              
                 color = 'blue',
                 discrete = True,                                   #The "discrete" parameter will separate the bars for each value
                 kde = True,                                        #Plot of an estimated probability density
                 legend = False,            
                 edgecolor = 'black')
    plt.yticks(np.arange(min(y), max(y)+2, 1))                      #Setting the scale for the y-axis
    plt.title(f'NUMBERS DISTRIBUTION\n  $\overline{{x}} = {round(a, 4)}$  ${{\sigma^2}} = {round(v, 4)}$  ${{\sigma}} = {round(d, 4)}$')
    plt.ylabel('OCCURRENCE')
    plt.xlabel(f'NUMBERS')

    plt.minorticks_on()                                             #Turning on the minor ticks for better visualization
    plt.tight_layout()
    plt.autoscale()
    plt.grid()

    return plt.show()


#Determining the size of the terminal with the library OS
c = os.get_terminal_size().columns                          

#Defining the user input list and a Numpy array for storage.  
#Numpy is needed for later use with MatPlotLIb                                        
def calculator(n = [], ar = np.array([])):                   
    print('******************** STATISTICS CALCULATOR :) ********************'.center(c))
    print('This program calculates the average, variance and standard deviation of all the given numbers.'.center(c))

    #Showing the ending mechanism to the user    
    print('Instructions:  Input one number at a time. To stop the count, just press ENTER without writing anything'.center(c)), 
    print(''.center(c, '-'))

    try :                                                   #try/except construction for continuous storage, until a string value is given 
        while True:
            k = float(input('Input number = '))             #Only float types are stored inside the list
            n.append(k)                                     #Appending to the list
    except ValueError:                                      #Constraint to string values
        print(''.center(c, '-'))
        print('{}'.format('Results :D\n').center(c))

    #After the exception is achieved, the elements of the list are appended to a Numpy array                           
    for i in range(len(n)):                                 
        ar = np.append(ar, n[i])

    s = np.sum(ar)                                          #Sum of all the numbers                 
    a = s/(len(ar))                                         #Average value
    M = np.max(ar)                                          #Biggest number
    m = np.min(ar)                                          #Smallest number

    v = 0                                                   #Calculus for the variance
    for i in range(len(ar)):
        v += ((ar[i]-a)**2)/(len(ar)) 

    d = math.sqrt(v)                                        #Standard deviation

    return plot(ar, a, v , d, m, M)

        
calculator()
