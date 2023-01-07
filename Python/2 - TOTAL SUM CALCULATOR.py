#The function will sum all the numbers given by the user, until the number zero - the flag - is written. It DOES NOT recognizes alphabetic characters, and will not work if the user inputs it. A more refined program is available at the next file: "Average Value Calculator"

def Sum(n = float, list = []):      #Definition of the variable n for receiving the user numbers, and the list to store them
    print('Write as many numbers as you want to sum. When you decide to stop, just write the number "0".')
    while n != 0:       #Constraint to the flag-element
        n = float(input('Number: '))        #User input for the desired numbers to sum
        list.append(n)      #Appending the numbers to the previously defined list

    s = sum(list)       #Summing all elements of the list for the desired result
    return(
        print('The sum of the given numbers equals to {}'.format(s))
    )
Sum()