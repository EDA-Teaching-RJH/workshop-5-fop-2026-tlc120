#Statement of Requirements
#Functional Requirements: The system accept: 50, 20, 10, 5. The exact output is the total value of user input
#Non-Functional Requirements: It will print("Invalid input")

while True:
    x = int(input("Please insert a coin. "))

    if x <= 75:
        print(f"You have owe {x}p. ")

        y = (input("Is the amount is right? ")) 
        if y == "yes":
            print(f"You have owe {x}p. ")
            break

        elif y == "no":
            u = int(input("Please insert a coin. "))
            x = u + x
            print(f"You have owe {x}p. ")
        else:
            print("Invalid input")
            continue
    else:
       print(f"You have owe {x}p. ") 
       break


#Implementation Challenge:
x = (input("Please insert a coin. "))
while x.isnumeric == True:
    if x <= 75:
        print(f"You have owe {x}p. ")
        y = (input("Is the amount is right? ")) 
        
        if y == "yes":
            print(f"You have owe {x}p. ")
            break

        elif y == "no":
            u = int(input("Please insert a coin. "))
            x = u + x
            print(f"You have owe {x}p. ")
else:
    print("Invalid input")
    
        



