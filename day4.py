from sys import argv

from sympy import Line3D
#1
def func():
    print("Hello World")
#2
def func1(name):
    print("Hi, {}. My name is Google".format(name))
#3
def func3(x, y, z):
    if z:
        return x
    else: 
        return y
#4
def func4(x, y):
    return x * y
#5
def is_even(x):
    return(x % 2 == 0)
#6
def greaterThan(x, y):
    return(x > y)
#7
def add(*argv):
    ans = 0
    for arg in argv:
        ans += arg
    return ans
#8
def evenFilter(*argv):
    return [arg for arg in argv if arg % 2 == 0]
#9
def sarcasmCase(s):
    l = [c.lower() for c in s]
    for i in range(0,len(l),2):
        l[i] = l[i].upper()
    return ''.join(l)
#10
def func10(x, y):
    if x % 2 == 0 and y % 2 == 0:
        print("The lower number is {}".format(min(x, y)))
    else:
        print("The greater number is {}".format(max(x, y)))
#11
def func11(s1, s2):
    return(s1[0].lower() == s2[0].lower())
#12
def func12(x):
    diff = 7 - x
    return(7 + 2 * diff)
#13
def func13(s):
    l = [c for c in s]
    l[0] = l[0].upper()
    l[3] = l[3].upper()
    return(''.join(l))

print("Running #1")
func()
print("\nRunning #2 with the string 'Mike")
func1("Mike")
print("\nRunning #3 using 'yes', 'no', True followed by 'yes', 'no', False")
print(func3('yes', 'no', True))
print(func3('yes', 'no', False))
print("\nRunning #4 using 6 and 7")
print(func4(6,7))
print("\nRunning #5 using 6 followed by 7")
print(is_even(6))
print(is_even(7))
print("\nRunning #6 using 6,7, then 6,6, then 6,5")
print(greaterThan(6,7))
print(greaterThan(6,6))
print(greaterThan(6,5))
print("\nRunning #7 using 1,2,3,4,5,6")
print(add(1,2,3,4,5,6))
print("\nRunning #8 using 4,7,16,5,19,20")
print(evenFilter(4,7,16,5,19,20))
print("\nRunning #9 using the string 'This is an obnoxious way to type")
print(sarcasmCase("This is an obnoxious way to type"))
print("\nRunning #10 using 6, 7 followed by 4, 6")
print(func10(6,7))
print(func10(4,6))
print("\nRunning #11 using 'test1' and 'test2' followed by 'true' 'false'")
print(func11('test1', 'test2'))
print(func11('true', 'false'))
print("\nRunning #12 using 3 followed by 9")
print(func12(3))
print(func12(9))
print("\nRunning #13")
print(func13("this is a test"))

#coding exercise 9
bookOrders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

bookOrder = [6769, 
    (34587, 4, 40.95),
    (98762, 5, 56.80),
    (77226, 3, 32.95),
    (88112, 3, 24.99)]

orderTotal = lambda l: (l[0], round(l[2] * l[3] + 10, 2)) if l[2] * l[3] < 100 else (l[0], round(l[2] * l[3],2))
orderTotal2 = lambda l: (l[0], sum(t[1] * t[2] for t in l[1:]))
print("\nRunning Coding Exercise 9 part 1")
for order in bookOrders:
    print(orderTotal(order))
print("\nRunning Coding Exercise 9 part 2")
print(orderTotal2(bookOrder))
