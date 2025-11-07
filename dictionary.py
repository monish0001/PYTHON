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





    
