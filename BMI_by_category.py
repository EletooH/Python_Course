W = float(input ('Please, enter your weight in kilograms:'))
H = float(input ('Please, enter height in meters:'))
BMI = W / (H*H)
if BMI <= 18.5:
    category = 'Underweight'
elif 18.5 < BMI <= 24.9:
    category = 'Normal'
elif 25 <= BMI <= 29.9:
    category = 'Overwieght'
elif BMI >= 30:
    category = 'Obesity'
print(round(BMI,2), category)
