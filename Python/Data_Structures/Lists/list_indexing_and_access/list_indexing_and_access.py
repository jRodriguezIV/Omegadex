# 📋 PYTHON LIST INDEXING & ACCESS CHEAT SHEET

# ✅ Create a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# 🔹 Access by index (0-based)
print(my_list[0])  # 'apple' (1st element)
print(my_list[2])  # 'cherry' (3rd element)

# 🔹 Negative indexing (from the end)
print(my_list[-1])  # 'elderberry' (last element)
print(my_list[-2])  # 'date' (2nd last)

# 🔹 List slicing: [start:stop] → (stop is exclusive)
print(my_list[1:4])  # ['banana', 'cherry', 'date']
print(my_list[:3])   # ['apple', 'banana', 'cherry']
print(my_list[2:])   # ['cherry', 'date', 'elderberry']

# 🔹 Slicing with steps: [start:stop:step]
print(my_list[::2])  # ['apple', 'cherry', 'elderberry']
print(my_list[::-1]) # ['elderberry', 'date', 'cherry', 'banana', 'apple'] (reversed)

# 🔹 Modify an item
my_list[1] = 'blueberry'
print(my_list)  # ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# 🔹 List length
print(len(my_list))  # 5

# 🔹 Check if value exists in list
print('cherry' in my_list)     # True
print('banana' in my_list)     # False

# 🔹 Looping through list
for item in my_list:
    print(item)

# 🔹 Enumerate with index
for index, item in enumerate(my_list):
    print(index, item)

# 🧠 NOTE: my_list['hello'] is NOT valid.
# That type of access is for dictionaries only.

# ✅ Dictionary example for comparison:
my_dict = {'hello': 'world', 'foo': 'bar'}
print(my_dict['hello'])  # 'world'
