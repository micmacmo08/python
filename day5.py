def bmiCalc(w, h):
    bmi = w / h**2
    underWeightLimit = 18.5
    normalWeightLimit = 25.0
    overWeightLimit = 30.0
    if bmi < underWeightLimit:
        return 'under'
    elif bmi < normalWeightLimit:
        return 'normal'
    elif bmi < overWeightLimit:
        return 'over'
    else:
        return 'obese'

results = []
lines = int(input("Please enter the number of people for whom you'd like to calculate the BMI. Then enter the weight and height, separated by a space, on the following lines for each person:\n"))
for i in range(lines):
    measurements = [float(x) for x in input().split()]
    results.append(bmiCalc(measurements[0],measurements[1]))
print(' '.join(results))