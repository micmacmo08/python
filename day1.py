from math import ceil

def paymentCalculator(p, r, l):
    m = ceil(p * (r/12 * (1 + r/12)**l)/((1 + r/12)**l - 1))
    return m

def main():
    p = int(input("What is the initial loan amount? "))
    r = float(input("What is the annual interest rate? "))
    r = r / 100
    l = int(input("How many months to pay off the loan? "))
    print(f"The monthly payment amount is ${paymentCalculator(p, r, l)}")

main()