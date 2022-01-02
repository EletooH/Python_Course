from random import randint
machine_number = randint(1,10)
user_guess = float (input("Please enter your gues: "))
if user_guess < machine_number:
    print ('Your guess is less than my number. Try again!')
elif user_guess > machine_number:
    print ('Your guess is greater than my number. Try again!')
elif user_guess == machine_number:
    print ('Congratulations! You succeeded')
print("machine_number={}".format(machine_number))
