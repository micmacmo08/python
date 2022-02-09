from random import randint

def div7And5():
    low = 1500
    high = 2701
    ans = [i for i in range(low, high) if i % 5 == 0 and i % 7 ==0]
    print(", ".join(str(c) for c in ans))

def cToF(c):
    return((9/5) * c + 32)


def fToC(f):
    return((f - 32) * 5 / 9)

def guesser():
    ans = randint(1,9)
    guess = int(input("I'm thinking of a number between 1 and 9. Can you guess what it is? "))
    while guess != ans:
        guess = int(input("That is incorrect. Guess again: "))
    else:
        print("Well guessed!")

def starTriangle():
    for i in range(-4, 5):
        star = "*"
        for j in range(5 - abs(i)):
            print(star, end=" ")
        print("\n")

def stringReverse(s):
    print(s[::-1])

def oddsAndEvens(l):
    odds = 0
    evens = 0
    for n in l:
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("Number of even numbers: {}\nNumber of odd number: {}".format(evens, odds))

def printListWithTypes(l):
    for item in l:
        print("{}: {}".format(item, type(item)))

def main():
    print("These are the numbers between 1500 and 2700 inclusive that are divisible by both 5 and 7:")
    div7And5()
    print("\n")
    f = cToF(int(input("Please enter temperature to convert from C to F: ")))
    print("That is {}F".format(f))
    c = fToC(int(input("Please enter temperature to convert from F to C: ")))
    print("That is {}C".format(c))
    guesser()
    starTriangle()
    stringReverse(input("Please enter a string to be reversed: \n"))
    vals = input("Please enter a list of comma separated numbers:\n")
    l = vals.split(",")  #split entry into a list
    l = [int(i) for i in l] #convert all the strings in the list to ints
    oddsAndEvens(l)
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    printListWithTypes(datalist)
    nums = []
    for n in range(0, 7):
        if n == 3 or n == 6:
            continue
        nums.append(n)
    print(" ".join(str(n) for n in nums))

main()