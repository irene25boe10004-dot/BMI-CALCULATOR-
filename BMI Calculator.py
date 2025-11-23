print("===BMI Calculator===")


height = float(input('Enter your height cm : /n'))
height = height / 100
weight = float(input('Enter your weight kg : /n'))

BMI = weight / height * height
print(f'Your body mass index (BMI) is {BMI}')
if(BMI<=18.5):
    print('You are underweight')
elif(BMI>=24.9):
    print('You are healthy')
elif(BMI>=29.9):
    print('You are overweight')
else:
    print('You are obese')
    
