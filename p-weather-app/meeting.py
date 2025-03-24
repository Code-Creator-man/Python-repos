print("Hi, what is your name ?")
name = input("Me:")
while name == "":
    print("Dont you tell your name?")
    name = input("Me:")
    print(f"Nice to meet you {name}!")