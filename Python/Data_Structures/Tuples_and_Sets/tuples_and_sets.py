# 📦 Python Tuples & Sets Cheat Sheet
# Covers tuple immutability, creation, and access + set creation, uniqueness, and operations

# -------------------- TUPLES --------------------
# Tuples are immutable ordered collections that can hold heterogeneous data.

# ✅ Creating Tuples
empty = ()                          # Empty tuple
t1 = (10, 20, 30)                   # Tuple of ints
t2 = (10, 20.2, 'thirty')           # Mixed types
t3 = ((1, 2), ('a', 'b'))           # Nested tuple
t4 = (10, (20.2, ("thirty", 40)))   # Deep nesting

# 🔒 Tuples are immutable (no append/edit/delete)
t = (1, 2, 3)
print(t[0])         # 1 (can access)
# t[0] = 10         ❌ TypeError
# t.append(4)       ❌ AttributeError

# 📏 Tuple Length
len(t)              # 3

# -------------------- SETS --------------------
# Sets are mutable, unordered collections with no duplicate elements.

# ✅ Creating Sets
s = {'Neo', 'Trinity', 'Neo'}       # Duplicates auto-removed
print(s)                            # {'Neo', 'Trinity'}
s2 = set('THEMATRIX')               # Unique characters only
print(s2)                           # {'T', 'H', 'E', 'M', 'A', 'I', 'X', 'R'}

# ❗ Empty curly braces create a dict, not a set
# s = {} → type(s) = dict

# 🔄 Set Operations
x = set('ABCDE')
y = set('CDEFG')

x | y          # Union → all elements
x & y          # Intersection → common
x - y          # Difference → x only
x ^ y          # Symmetric difference

# 🔧 In-place Set Updates
x.difference_update(y)     # Removes common elements from x
x = set('ABCDE'); y = set('CDEFG')
x = x - y                  # Same as above

# 🔍 Set Relationships
x.isdisjoint(y)            # True if no overlap
y.issubset(x)              # True if y ⊆ x
x.issuperset(y)            # True if x ⊇ y

# 🧪 Subset/Superset Shortcuts
y < x       # y is subset of x
x > y       # x is superset of y

# ✏️ Modifying Sets
x.add('Z')                 # Add item
x.discard('Z')             # Remove item (no error if missing)
x.pop()                    # Remove random item
x.copy()                   # Shallow copy
x.clear()                  # Remove all items
