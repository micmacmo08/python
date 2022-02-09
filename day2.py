class InputOutString(object): #used for day_2_b question 5
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input()
    
    def printstring(self):
        print(self.s.upper())

def palindrome(s): #used for day_2_a
    s = ''.join(c for c in s if c.isalnum()) #remove special characters and spaces
    for i in range(len(s)//2 + 1):
        if s.lower() != s[::-1].lower():
            return 'N'
    return 'Y'

def factorial(n): #used for day_2_b question 2
    if n == 0:
        return 1
    return n * factorial(n-1)

def mobOrCrowdTest(l): #used for day_2_c
    mob = 6
    crowd = 3
    if len(l) >= mob:
        print("There are a lot of people here. I think this qualifies as a mob...")
    elif len(l) >= crowd:
        print("There are a few people here, so this is quite the crowd")
    elif len(l) > 0 :
        print("This room is not crowded at all")
    else: 
        print("The room is empty")

def main():
    #day_2_a
    i = int(input("How many strings would you like to check as palindromes? "))
    responses = ['' for n in range(i)]
    for n in range(i):
        responses[n] = (input(f"Please enter string #{n+1}:\n"))
    answers = [palindrome(s) for s in responses]
    print(' '.join(answers))

    #day_2_b question 1
    div7not5 = []
    low = 2000
    high = 3201
    for n in range(low, high):
        if n % 7 == 0 and n % 5 != 0:
            div7not5.append(n)
    print(", ".join(str(c) for c in div7not5))

    #day_2_b question 2
    fact = int(input("For what number would you like the factorial? "))
    print(factorial(fact))

    #day_2_b question 3
    n = int(input("How many numbers would you like to include in the dictionary of squares? "))
    squares = {x: x*x for x in range(1, n+1)}
    print(squares)

    #day_2_b question 4
    vals = input("Please enter a list of comma separated numbers:\n")
    l = vals.split(",")
    t = tuple(l)
    print(l)
    print(t)

    #day_2_b question 5 (class found at the top)
    strObj = InputOutString()
    print("Please enter a string:")
    strObj.getString()
    strObj.printstring()

    #day_2_c
    room = ["Alice", "Billy", "Charlie", "Dave"]
    print(f"The people in the room are {room}")
    mobOrCrowdTest(room)
    room.remove("Dave")
    room.remove("Charlie")
    print(f"Charlie and Dave have been removed from the room")
    mobOrCrowdTest(room)
    room.append("Charlie")
    room.append("Dave")
    room.append("Frank")
    room.append("George")
    print("Adding Charlie and Dave back in the room, as well as Frank and George")
    mobOrCrowdTest(room)
    room.clear()
    print("Removing everybody in the room")
    mobOrCrowdTest(room)


main()