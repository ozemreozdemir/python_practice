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

#Human Readable Time
def make_readable(seconds):
    """
    ARGS : seconds (int)
    RETURNS : time (string)

    Write a function, which takes a non-negative integer (seconds) as input
    and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
    The maximum time never exceeds 359999 (99:59:59)

    You can find some examples in the test fixtures.
    """
    HH=seconds//3600
    MM=(seconds-HH*3600)//60
    SS=(seconds-MM*60-HH*3600)
    time= str(HH).zfill(2) + ":" + str(MM).zfill(2) +":" + str(SS).zfill(2)
    return time

    #Where my anagrams at?

def anagrams(word, words):
    """
    ARGS : word :(int) word that will be searched to have an anagram
           words: (list) list of integers
    RETURNS: anagrams_list(list) list of strings that are anagrams of given word

    Write a function that will find all the anagrams of a word from a list.
    You will be given two inputs a word and an array with words.
    You should return an array of all the anagrams or an empty array if there are none.
    For example:
    anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
    """
    anagrams_list=[]
    for w in words:
        if w not in anagrams_list and sorted(word)==sorted(w):
            anagrams_list.append(w)
    return anagrams_list

def move_zeros(array):
    """
    ARGS: list of ints and strings
    RETURNS: list of ints and strings having the zeros as the last elements

    Write an algorithm that takes an array and moves all of the zeros to the end,
    preserving the order of the other elements.
    move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

    """
    result_list=[]
    zero_list=[]
    for i in mylist:
        if type(i)!=bool and i==0:
            zero_list.append(0)
        else:
            result_list.append(i)
    return result_list+zero_list

def dirReduc(arr):
    """
    ARGS : arr (list) list of strings (directions)
    RETURNS : directions (list) list of strings

    Once upon a time, on a way through the old wild west, a man was given
    directions to go from one point to another. The directions were
    "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite,
    "WEST" and "EAST" too. Going to one direction and coming back the opposite
    direction is a needless effort. Since this is the wild west, with dreadfull
    weather and not much water, it's important to save yourself some energy,
    otherwise you might die of thirst!
    """
    directions=[]

    ns = arr.count('NORTH')-arr.count('SOUTH')
    ew =  arr.count('EAST')-arr.count('WEST')

    if ns > 0:
        directions+=['NORTH']*(ns)
    elif ns < 0:
        directions += ['SOUTH']*(-ns)

    if ew > 0:
        directions+=['EAST']*(ew)
    elif ew < 0:
        directions+=['WEST']*(-ew)

    return directions

#Maximum subarray sum
def maxSequence(arr):
    """
    Return the maxumym subarray

    ARGS : arr (list) list of integers
    RETURNS : result_list (list) list of integers

    The maximum sum subarray problem consists in finding the maximum sum of a
    contiguous subsequence in an array or list of integers:

    Example:
    maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    should be 6: [4, -1, 2, 1]
    """
def maxSequence(arr):
    sumdict={}
    if len(arr) > 0:
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)+1):
                sumdict[(i,j)]=sum(arr[i:j])
#        ii= max(sumdict,key=sumdict.get)[0]
#        jj= max(sumdict,key=sumdict.get)[1]
        return max(sumdict.values())
    else:
        return 0

def palindrome_chain_length(n):
    """
    ARGS : n (int) an integer
    RETURN : steps (int) number of steps

    Number is a palindrome if it is equal to the number with digits in reversed order.
    For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.

    Write a method palindrome_chain_length which takes a positive number and
    returns the number of special steps needed to obtain a palindrome.
    The special step is: "reverse the digits, and add to the original number".
    If the resulting number is not a palindrome, repeat the procedure with the sum
    until the resulting number is a palindrome.
    """
    if  int(''.join(str(n)[::-1])) == n:
        steps = 0
    else :
        steps = 1
        m = int(''.join(str(n)[::-1]))+n
        while int(''.join(str(m)[::-1]))!=m:
            steps+=1
            m=int(''.join(str(m)[::-1]))+m
    return steps

def nbr_of_laps(x, y):
    from fractions import Fraction
    """
    ARGS : x (int) as Bob's lenght (larger than 0)
           y (int) as Charle's lenght (larger than 0)

    RETURNS : lap_list : (list of int) list of Bob's and Charle's laps


    Bob and Charles are meeting for their weekly jogging tour.
    They both start at the same spot called "Start" and they each run
    a different lap, which may (or may not) vary in length.
    Since they know each other for a long time already, they both run
    at the exact same speed.

    """
    if x > y :
        laprate=float(y)/x
        int_ratio=Fraction(laprate).limit_denominator()
        laplist=[int_ratio.numerator,int_ratio.denominator]
    else :
        laprate=float(x)/y
        int_ratio=Fraction(laprate).limit_denominator()
        laplist=[int_ratio.denominator,int_ratio.numerator]
    return laplist
