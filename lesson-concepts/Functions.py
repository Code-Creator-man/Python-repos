def collect_names(attempts=3):
    names_list = []
    names_dict = {}
    for attempt in range(1, attempts + 1):
        entry = input(f"Attempt {attempt} - Enter your name: ")
        names_list.append(entry)
        names_dict[attempt] = entry
    return names_list, names_dict
names_list = []
names_dict = {}
attempts = 3

for attempt in range(1, attempts + 1):
    entry = input(f"Attempt {attempt} - Enter your name: ")
    names_list.append(entry)
    names_dict[attempt] = entry

print("List of names:", names_list)
print("Dictionary of names:", names_dict)