shopping_list = ["bread", "Rice", "milk", "sugar", "soap"]
print("Shopping List Report:")

for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")
    long_items = 0

for item in shopping_list:
    if len(item) > 4:
        long_items += 1

print(f"Items with more than 4 characters: {long_items}")

longest_item = shopping_list[0]

for item in shopping_list:
    if len(item) > len(longest_item):
        longest_item = item

print(f"Longest item: {longest_item}")