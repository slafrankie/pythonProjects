#How tell to if your fat, skinny, or fit using the BMI program

weight = float(input("Enter exact weight in pounds: "))
height = float(input("Enter exact height in inches: "))

BMI = (weight * 703) // (height**2)

print("BMI is: ", BMI)

if BMI <= 18.4:
    print("Underweight")
elif BMI == 18.5 and BMI == 25:
    print("Optimal weight, good job")
else:
    print("Overweight")
