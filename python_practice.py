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
    ARGS: num (int)
    RETURNS : int() decending ordered num

    Your task is to make a function that can take any non-negative integer
    as a argument and return it with it's digits in descending order. Essentially,
    rearrange the digits to create the highest possible number.
    """
    return int(''.join(sorted(list(str(num)),reverse=True)))

# Take a Ten Minute Walk
def isValidWalk(walk):
    #determine if walk is valid
    """
    ARGS : walk (list) list of strings such as ["n","w","e","s"]
    RETURNS : boolean "True" if the given directions is 10 minutes walk

    You live in the city of Cartesia where all roads are laid out in a perfect grid.
    You arrived ten minutes too early to an appointment, so you decided to take
    the opportunity to go for a short walk. The city provides its citizens with
    a Walk Generating App on their phones -- everytime you press the button it
    sends you an array of one-letter strings representing directions to walk
    (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse
    one city block, so create a function that will return true if the walk
    the app gives you will take you exactly ten minutes (you don't want to be
    early or late!) and will, of course, return you to your starting point.
    Return false otherwise.

    """
    walkdict={"n":1,"s":-1,"e":2,"w":-2}
    walklist=[]
    if len(walk)!=10:
        return false
    else:
        for w in walk:
            walklist.append(walkdict[w])
        if sum(walklist)==0:
            return True
        else:
            return False
