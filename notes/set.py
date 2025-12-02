from loguru import logger

#  unorderdred does not contain duplicate values

set_1={1,1,1,1,1,2,2,2,4,4,4,47,8,9,0,2,3,45,6,6,7,8,8}

# why ouput of above list is {0, 1, 2, 3, 4, 6, 7, 8, 9, 45, 47}

logger.info(set_1)
logger.info(set_1)


new_set={} # this will craete dictionary 

new_set=set()
new_set.add(100)
new_set.add(1)
new_set.add(890)
new_set.add(23)
new_set.add(45)
new_set.add(100)
new_set.add(100)
new_set.add(100)
# new_set.remove(1)
logger.info(new_set)

for item in set_1:
    print(item)


# Properties of a Python Set
# 1. Unordered
# A set does not maintain any specific order of elements.
# 2. Unique Elements Only
# A set automatically removes duplicates.
# 3. Mutable
# The set itself can be changed (you can add or remove items)
# 4.Elements Must Be Immutable (Hashable)
# You cannot put mutable types (like lists or dictionaries) inside a set.
# Valid elements:
# integers
# strings
# tuples
# floats
# 5. No Indexing or Slicing
# Since sets are unordered, you cannot access elements by index.
# 6. Supports Mathematical Set Operations

# 7.Python sets support classic set operations:
#     Union
# a | b
# • Intersection
# a & b
# • Difference
# a - b
# • Symmetric difference
# a ^ b
# 8.Fast Lookup (based on hashing)

# Checking membership (in) is O(1) on average.