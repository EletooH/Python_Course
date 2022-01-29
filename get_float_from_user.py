def get_float_from_user(msg):
    user_input = float(input(msg))
    return user_input

try:        
    user_height = get_float_from_user("I need to know your height in centimetres: ")
    user_weight = get_float_from_user("And your weight in kilograms: ")


except ValueError as e:
    print('***Enter a number, please!')

except:
    print("***Oops, something went wrong! Try again!")  

print("Your height is: {:5.2f}cm. and you weight {:.2f}kg.".format(user_height, user_weight))
