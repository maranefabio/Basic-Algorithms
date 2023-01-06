#The function will sum all the numbers given by the user, until the number zero - the flag - is written. It DOES NOT recognizes alphabetic characters, and will not work if the user inputs it. A more refined program is available at the next file: "Average Value Calculator"

def Sum(n = float, list = []):
    print('Write as many numbers as you want to sum. When you decide to stop, just write the number "0".')
    while n != 0:
        n = float(input('Number: '))
        list.append(n)

    s = sum(list)
    return(
        print('The sum of the given numbers equals to {}'.format(s))
    )
Sum()