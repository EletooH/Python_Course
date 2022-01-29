class UserDataError(Exception):
    pass

def get_string_from_user(msg):
    user_input = input(msg)
    return user_input

try:        
    user_name = get_string_from_user("Enter your name, please: ")
    user_place = get_string_from_user("Where are you from?: ")
    
except KeyboardInterrupt:
    print("Oops! Something went wrong!")  

print("Hello {}! How is the weather in {} today?".format(user_name, user_place))
