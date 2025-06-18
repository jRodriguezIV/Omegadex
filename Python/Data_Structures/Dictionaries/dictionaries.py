# ================================
# 📘 PYTHON DICTIONARY CHEATSHEET
# ================================

# Sample dictionary
new_dict = {
    'Jack': 2563,
    'Rose': 8965,
    'Hockley': 7412,
    'Fabrizo': 9632,
    'Molly Brown': 4563
}

# ----------------------------------------
# 🔢 LENGTH OF DICTIONARY
# Get number of key-value pairs
len(new_dict)  # Output: 5

# ----------------------------------------
# 🔑 ACCESSING KEYS
# Returns all keys in the dictionary
dict_keys = new_dict.keys()  # Output: dict_keys(['Jack', 'Rose', 'Hockley', 'Fabrizo', 'Molly Brown'])

# ----------------------------------------
# 🔢 ACCESSING VALUES
# Returns all values in the dictionary
dict_values = new_dict.values()  # Output: dict_values([2563, 8965, 7412, 9632, 4563])

# ----------------------------------------
# ❌ DELETE BY KEY
# Removes a key-value pair by key

# Delete key 'Hockley'
del new_dict['Hockley']
# Output: {'Jack': 2563, 'Rose': 8965, 'Fabrizo': 9632, 'Molly Brown': 4563}

# ----------------------------------------
# 🎯 POP A VALUE BY KEY
# Returns and removes the value of the specified key

popped_value = new_dict.pop('Fabrizo')  # Output: 9632
# new_dict now: {'Jack': 2563, 'Rose': 8965, 'Molly Brown': 4563}

# ----------------------------------------
# 🔃 SORT DICTIONARY BY KEYS
# Returns keys sorted in alphabetical order (default sort)

sorted_keys = sorted(new_dict)  # Output: ['Jack', 'Molly Brown', 'Rose']

# ----------------------------------------
# 🧹 CLEAR DICTIONARY
# Removes all key-value pairs

new_dict.clear()  # Output: {}

# ================================
# ✅ END OF DICTIONARY CHEATSHEET
# ================================
