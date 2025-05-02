import re
import json
special_characters=re.compile('[!@#$%^&*()_<>?\/{}|`~]') 
print("---------------Login/Sign in---------------------")
option = input("Login/Sign up ")
option.lower() # convert option variable, value into lower case
dictionary ={"user":" "} #main dict
user_pass={} # inner dict 
if option == "sign up": 
    username = input("Enter username: ")
    password1 = input("Enter password: ")
    while(special_characters.search(password1) is None or not re.search("[0-9]",password1)):# checking special char and integer in password
        password1=input("At least password should contain one special character and one number\nEnter password: ")
    else:
        password2 = input("Confirm your password: ")
        if password1!=password2:
            print("Both password are not same!")
        with open('userdetails.json', 'r') as file:
            python_dict = json.load(file)
            key = python_dict['user'][0]['username']
            if(key!=username):#username is exists or not
                user_pass["username"]=username
                user_pass["password"]=password1
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
        with open('userdetails.json', 'r') as file: #opening the json file reading mode
            python_dict = json.load(file) #converting json str into python dict
            keyuserv = python_dict['user'][0]['username']
            keypasswordv = python_dict['user'][1]['password']
            if(keyuserv==username and keypasswordv==password):
                print(f"{keyuserv} You are Loogined successfully!🎉")
                user_profile= python_dict["user"][0]["profile"]
                # print(user_profile)
                print("---------------YOUR PROFILE--------------------")
                print("username:", python_dict["user"][0]["username"])
                print("password:", python_dict["user"][0]["password"])
                for x, y in user_profile.items():
                    print(f"{x} : {y}")
            else:
                print("Invalid username and password")
    else:
        print("Invalid!")