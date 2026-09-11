def new_user_code():
        
        users = ["David", "Davis", "Darrell", "Leon", "Shannel", "Kimberly", "Tasha"]

        for user in users:

                if user == "Leon":
           
                 continue
    

        print (f" welcome {user} ")

        age = int(input("Enter youre age: "))

        if age >= 18:

            print(f" welcome {user} you are eligible")

        else:

            print(f"welcome {user} you are not eligible")

new_user_code()
