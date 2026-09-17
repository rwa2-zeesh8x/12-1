while(True):
    username=input("Please enter your username ")#zee
    password=input("Please enter your password ")#1234

    if(username=='kunal' and password=="kunal@123"):
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
    
print("Outside loop")
