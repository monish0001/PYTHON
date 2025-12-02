from loguru import logger

student= {
    "name": "Monish",
    "age": 23,
    "course": "Python",
    "is_graduated": True
}


# logger.info(student)

# logger.info(student.keys())
# logger.info(student.values())
# logger.info(student.items())

# for key in student:
#     print(key)


# for key in student:
#     print(key,student[key])


# for key,value in student.items():
#     logger.info(f"{key} : {value}")


# print(student.get("name"))

# print(student.get("gender"))

# print(student["gender"])

student.update({"name":"Karan"})

logger.info(student)

course= {
    "sub_name": "Python",
    "no_of_chapter": 10
}


final_dict={**student,**course}



logger.info(final_dict.pop("name"))

logger.info(final_dict)

logger.info(final_dict.popitem())

logger.info(final_dict)


final_copy=final_dict.copy()

logger.info(id(final_dict))
logger.info(id(final_copy))

logger.info(final_copy.clear())



# dict comperehension


labour_with_cost = {
    "Mahesh": 500,
    "Ramesh": 400,
    "Mithilesh": 400,
    "Sumesh": 300,
    "Jagmohan": 1000,
    "Rampyare": 800
}
labour_with_cost ={ key: labour_with_cost.get(key)+100  for key in labour_with_cost
    
}

logger.info(labour_with_cost)



labour_with_cost = {
    key: (value + 100 if key != "Jagmohan" else value)
    for key, value in labour_with_cost.items()
}

logger.info(labour_with_cost)



# IN dictionary

# diffrence b/w IN dictionary and list


name="Mohd Monish"

letter_count={}


for ch in name:
    if ch in letter_count:
        letter_count[ch]+=1
    else:
        letter_count[ch]=1
        
logger.info(letter_count)





    
# 1. Supports Useful Methods
# dict.keys()
# dict.values()
# dict.items()
# get()
# update()
# pop()
# clear()
# 2.Fast Lookups (Hash Table)
# Accessing or checking a key is O(1) on average
# 3.No Indexing by Position
# You cannot access items by integer index (like lists).
# 4.Ordered (Python 3.7+)
# Dictionaries preserve insertion order.
# 5.Mutable
# You can change a dictionary by adding, updating, or deleting items.
# 6.Keys Must Be Immutable (Hashable)
# You can use:
# strings
# numbers
# tuples
# But not:
# lists
# sets
# dictionaries
# 7.Values Can Be Any Type
# Values can be:
# lists
# other dictionaries
# functions
# objects
# any Python type
# 8.Stores Data as Key–Value Pairs
# A dictionary maps each key to a value.
# 9.Keys Must Be Unique
# No two keys in a dictionary can be the same.