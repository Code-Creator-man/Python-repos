import random

print("Do you like Fruits?")
my_choice = input("Me: ").lower()
linux_choices = ('apple', 'banana', 'orange', 'grapes', 'mango', 'pineapple', 'watermelon', 'kiwi', 'papaya', 'guava')
linux_choice = random.choice(linux_choices)

if my_choice in linux_choices:
    if my_choice == linux_choice:
        print("I like it too")
    else:
        print(f"I prefer {linux_choice}")
else:
    print("That's not a fruit I know")

