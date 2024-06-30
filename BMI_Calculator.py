# BMI calculator:
wt = float(input('Enter your weight (in Kg) = '))
height = float(input('Enter your height (in meter) = '))
bmi = ((wt/(height**2)))
print (f'Your BMI is {bmi}.')
if bmi <= 16:
    print('Your are underweight (Severe thinness)')
elif bmi <=16.9:
    print('You are underweight (Moderate thinness)')
elif bmi <= 18.4:
    print('You are underweight (Mild thinness)')
elif bmi <= 24.9:
    print('Your are under Normal Range')
elif bmi <= 29.9:
    print('You are Overweight (Pre-obese)')
elif bmi <= 34.9:
    print('You are Obese (class -1)')
elif bmi <= 39.9:
    print('You are Obese (class -2)')
else:
    print('You are Obese (Class -3)')