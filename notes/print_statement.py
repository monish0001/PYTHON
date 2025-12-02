# Why do we need the print() statement in Python?

# How can we print line numbers using the print() statement?

# What are escape sequences and how can we use them?

# What is string formatting in Python?


length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Monish"
labour_mistri2 = "Karan"
is_home = False

print(length_of_land, breadth_of_land, bricks_cost_per_piece, labour_mistri1, labour_mistri2, is_home)

print("lenght is : ",length_of_land)
print('lenght is : ',length_of_land)

# print("Hi my name is monish i'm 
#       DE at Genpact..............")

print("Hi my name is monish i'm \nDE at Genpact..............")


print("Hi my name is 'monish' i'm DE at Genpact..............")
print('Hi my name is "monish" i am DE at Genpact..............')

print("Hi my name is \"monish\" i am DE at Genpact..............")

# To check data types correctly:
print(type(length_of_land))
print(type(breadth_of_land))
print(type(bricks_cost_per_piece))
print(type(labour_mistri1))
print(type(labour_mistri2))
print(type(is_home))


# string formating  f-string,.format()

print(f"Lenght is : {bricks_cost_per_piece} .")

print("values are : {} {} {}.".format(length_of_land,bricks_cost_per_piece,labour_mistri1))




from loguru import logger

logger.info(f"Hiii i'm logger",length_of_land)


