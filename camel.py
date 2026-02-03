import re
name = input("Please enter your name. ")
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)
