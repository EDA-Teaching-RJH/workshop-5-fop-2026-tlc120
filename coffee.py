while True:
    coins1 = int(input("Please insert a coin. "))
    coins2 = input(f"You have insert {coins1}. Is that the right amount coins? ")
    if coins2 == "NO":
        continue
    elif coins2 == "Yes":
        break
match coins3:
    case "Picard" | "Riker" | "La Forge":
        print("Command Division")
    case "Data" | "Worf":
        print("Operations Division")
    case "Crusher" | "Troi":
        print("Sciences Division")
    case _:
        print("Character not found. Please enter a main TNG character.")
