print("What kind of Project do you want to create?")
print("0: Empty (default)")
print("1: Flutter")
kind = input("Number: ")
print("'" + kind + "'")

if kind == "":
    # Create an empty project by default
    kind = 0


