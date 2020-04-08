import random
import array
import math
import string 


details = []
container = []


status = True

while status:
    def get_user_details():
        user_details = {
        "firstname": input("Enter firstname: "),
        "lastname": input("Enter lastname: "),
        "email": input("Enter email: ")
        }
        return user_details
    
    user_details = get_user_details()
    
    
    
    def randomString(stringLength=5):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    extract_first = user_details["firstname"][:2]
    extract_second = user_details["lastname"][-2:]

    random_5 = randomString(5)
    password = extract_first + extract_second + random_5

    
    print("Your suggested password is: ", password)
    user_answer = input("Are you okay with the password. True or False only?: ").lower().strip()
    if user_answer == "true":
        user_details['user_password'] = password
        details.append(user_details)
        print(container.append(details))
        status = False
    else:
        new_password = input("Enter your desired password: ")
        len_password = len(new_password)
        if len_password <= 7:
            newer_password = input("Please enter a 7 character password: ")
            user_details['user_password'] = newer_password
            details.append(user_details)
            print(container.append(details))
            status = False
        else:
            user_details['user_password'] = new_password
            details.append(user_details)
            print(container.append(details))
            status = False
            
#new user
    new_user = input('Would you like to enter a new user. Answer Yes or No?: ').lower()

    if new_user == 'no':
        status = False
        for item in container:
            print(item)
    else:
        status = True
    
# else:
#     print("Error: Answer must be True or False")

# print(user_details)
# container.append(user_details)