user_name = str(input('Please, enter your name: '))
user_height = float(input ('Please, enter height in meters: '))
user_weight = float(input ('Please, enter your weight in kilograms: '))

def get_user_data(name, weight, height):
    if len(user_name)<3:
        print("Please, enter a name with minimum 3 characters!")
        exit(0)
    if user_height < 0.50:
        print("Please, enter a height between o.50 and 2.50 meters!")
        exit(0)
    elif user_height > 2.50:
        print("Please, enter a height between o.50 and 2.50 meters!")
        exit(0)
    if user_height < 50:
        print("Please, enter a weight between 50 and 300 meters!")
        exit(0)
    elif user_height > 300:
        print("Please, enter a weight between 50 and 300 meters!")
        exit(0)
    user_data = dict()
    user_data ['name'] = name
    user_data ['weight'] = weight
    user_data ['height'] = height
    return user_data
print (get_user_data(user_name, user_weight, user_height))

def calc_BMI(W, H):
    bmi = W / H ** 2
    return bmi
user_BMI = calc_BMI (user_weight, user_height)

if user_BMI <= 18.5:
    print(f"Your BMI is {user_BMI:.2f} - 'Underweight'")
elif 18.5 < user_BMI <= 24.9:
    print(f"Your BMI is {user_BMI:.2f} - 'Normal'")
elif 25 <= user_BMI <= 29.9:
    print(f"Your BMI is {user_BMI:.2f} - 'Overwieght'")
elif user_BMI >= 30:
    print(f"Your BMI is {user_BMI:.2f} - 'Obesity'")
