import json
# import re
import bcrypt
special_characters = "[!@#$%^&*()_<>?\/{}|`~]"
print("---------------Login/Sign in---------------------")
option = input("Login/Sign up ")
option.lower() # convert option variable, value into lower case
dictionary ={"user":" "} #main dict
user_pass={} # inner dict 
if option == "sign up": 
    username = input("Enter username: ")
    # username.isdigit
    while not((username.isalpha()) and (6<=len(username)<30)):
        username=input("username shoud be contain 6 to 30 character atleast(no space)\nEnter username: ")
    password1 = input("Enter password: ")
    while not((any(char in special_characters for char in password1)) and (any(char.isdigit() for char in password1))):# checking special char and integer in password
        password1=input("At least password should contain one special character and one number\nEnter password: ")
    password2 = input("Confirm your password: ")
    if password1!=password2:
        print("Both password are not same!")
    else:
        try:
            with open('userdetails.json', 'r') as file:
                python_dict = json.load(file)
                print(type(python_dict))
                username_key = python_dict['user'][0]['username']
        except FileNotFoundError:
            username_key = "username"
        if(username_key!=username):#username is exists or not
                salt = bcrypt.gensalt()
                passwoed_bytes=password1.encode('utf-8') #convert to bytes
                bytes_hashed_password = bcrypt.hashpw(passwoed_bytes, salt)
                str_hash_password = bytes_hashed_password.decode('utf-8') 
                user_pass["username"]=username
                user_pass["password"]=str_hash_password
                json_array = [user_pass,user_pass] # converting user_pass into json array formate
                dictionary["user"]=json_array # appending 'json_array' into 'user' key
                print(f"Congrats {username} you are signed up sucessfully!🎉")
                description = input("Tell Something about you: ")
                dob = input("Enter your DOB: ")
                hobbies = input("Your Hobbies!: ")
                gender = input("Gender: ")
                profile = {"description": description, "dob": dob, "hobbies": hobbies, "gender": gender}
                dictionary["user"][0]["profile"] = profile
                with open("userdetails.json", "w") as file: #Opening the json file in writing mode 
                    json.dump(dictionary, file, indent = 4)  #convering python dict to json str
        else:
            print("Username Already exists.")
else:
    if option == "login":
        username = input("Enter username: ")
        password = input("Enter your password: ") 
        hash_value = password.encode('utf-8')
        with open('userdetails.json', 'r') as file: #opening the json file reading mode
            python_dict = json.load(file) #converting json str into python dict
            username_key = python_dict['user'][0]['username']
            keypasswordv = python_dict['user'][1]['password']
            byte_pssword = keypasswordv.encode('utf-8')
            if bcrypt.checkpw(hash_value,byte_pssword):
                print(f"{username_key} You are Loged in successfully!🎉")
                user_profile= python_dict["user"][0]["profile"]
                input("press any key to see your profile: ")
                if True:
                    print("---------------YOUR PROFILE--------------------")
                    print("username:", python_dict["user"][0]["username"])
                    print("password:", python_dict["user"][0]["password"])
                    for x, y in user_profile.items():
                        print(f"{x} : {y}")
                else:
                    printf("Thank you!")
            else:
                print("Invalid username and password")
    else:
        print("Invalid!")
