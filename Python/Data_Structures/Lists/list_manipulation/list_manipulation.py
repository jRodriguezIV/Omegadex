# 📋 LIST MANIPULATION CHEAT SHEET

# ✅ Creating a list
my_list = [10, 20, 30, 40]
print(my_list)  # [10, 20, 30, 40]

# 🔹 Append
# Add a single item to the end
my_list.append(50)
print(my_list)  # [10, 20, 30, 40, 50]

# 🔹 Extend
# Add multiple items to the end
my_list.extend([60, 70, 80, 90])
print(my_list)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 🔹 Insert
# Insert an item at a specific index
my_list.insert(0, 0)         # At beginning
my_list.insert(10, 100)      # At index 10 (end here)
my_list.insert(6, 55)        # At index 6
print(my_list)  # [0, 10, 20, 30, 40, 50, 55, 60, 70, 80, 90, 100]

# 🔹 Remove
# Remove first occurrence of value
my_list.remove(0)
print(my_list)  # [10, 20, 30, 40, 50, 55, 60, 70, 80, 90, 100]

# 🔹 Pop
# Remove by index or remove last if no index is given
my_list.pop(5)   # Removes 55
my_list.pop()    # Removes 100
print(my_list)   # [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 🔹 Index
# Return index of first occurrence of value
print(my_list.index(50))  # 4
print(my_list.index(10))  # 0

# 🔹 Count
# Count how many times a value occurs
new_list = [10, 10, 10, 20, 30, 40, 50]
print(new_list.count(10))  # 3

# 🔹 Reverse
# Reverse the list in place
my_list.reverse()
print(my_list)  # [90, 80, 70, 60, 50, 40, 30, 20, 10]

# 🔹 Sort
# Sort the list in ascending order
new_list = [12, 35, 76, 20, 56, 34, 65]
new_list.sort()
print(new_list)  # [12, 20, 34, 35, 56, 65, 76]

# 📚 Coming Up in Advanced Topics:
# Lists used as:
# - Stacks (LIFO structure)
# - Queues (FIFO structure)
# - Graphs (Adjacency lists)
# - Trees (Nested list nodes)
