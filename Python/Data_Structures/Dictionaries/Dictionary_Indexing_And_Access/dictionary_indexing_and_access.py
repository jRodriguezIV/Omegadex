# ================================
# 🔍 PYTHON DICTIONARY ACCESS & INDEXING CHEATSHEET
# ================================

# ▶ Basic Dictionary Setup
person = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL"],
    "contact": {"email": "alice@example.com", "phone": "123-456-7890"}
}

# ----------------------------------------
# 📌 Accessing Values by Key
# ----------------------------------------

# Use square brackets to get a value directly
print(person["name"])     # Alice

# If the key doesn't exist, it raises a KeyError
# print(person["salary"])  ❌ KeyError!

# Use get() to avoid KeyError
print(person.get("salary"))           # None
print(person.get("salary", 0))        # Default value: 0

# ----------------------------------------
# 🧩 Accessing Nested Dictionary Values
# ----------------------------------------

# Access nested dictionaries
print(person["contact"]["email"])     # alice@example.com

# Use get() to safely access nested keys
print(person.get("contact", {}).get("phone"))  # 123-456-7890

# ----------------------------------------
# 🔁 Looping Through Keys & Values
# ----------------------------------------

# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# ----------------------------------------
# 🔍 Check Key Existence
# ----------------------------------------

# Use 'in' to check if key exists
print("name" in person)         # True
print("salary" in person)       # False

# ----------------------------------------
# 🧠 Dictionary Views vs Lists
# ----------------------------------------

# dict.keys(), dict.values(), dict.items() return dynamic "view" objects
# Convert them to list for indexing or display
print(list(person.keys())[0])   # name
print(list(person.values())[-1])  # Nested contact dict

# ----------------------------------------
# ✅ End of Dictionary Access Cheatsheet
# ----------------------------------------
