#Multiples of 3 and 5

def sum_mutiple_5and3(number):
    """
    ARGS: (int) integer number
    RETURNS: (int) sum of all the integer numbers that are multiples of 3 and 5

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Finish the solution so that it returns the sum of all
    the multiples of 3 or 5 below the number passed in.
    """
    numberlist=[]
    for n in range(number):
        if n%3 == 0 and n not in numberlist:
            numberlist.append(n)
        elif n%5 == 0 and n not in numberlist:
            numberlist.append(n)
    return sum(numberlist)

#Descending Order
def Descending_Order(num):
    """
    Your task is to make a function that can take any non-negative integer
    as a argument and return it with it's digits in descending order. Essentially,
    rearrange the digits to create the highest possible number.
    """
    return int(''.join(sorted(list(str(num)),reverse=True)))
