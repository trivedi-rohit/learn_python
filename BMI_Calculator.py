#BMI
weight = int(input("Enter your weight (in KG) = "))
height = float(input("Enter you height (in Meters) ="))
BMI = int(weight/(height**2))
if BMI <= 18.4:
    print(f"Your BMI is {BMI} and you are 'Underweight'")
elif BMI <= 25:
    print(f"Your BMI is {BMI} and you are 'Normal'")
elif BMI <= 30:
    print(f"Youe BMI is {BMI} and you are 'Overweight'")
elif BMI <= 35:
    print(f"Youe BMI is {BMI} and you are 'Obese Class -1'")
else:
    print(f"Youe BMI is {BMI} and you are 'Obese Class -2'")