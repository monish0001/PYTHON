from loguru import  logger
from  math import ceil, floor

#operator

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Monish"
labour_mistri2 = "Karan"
is_home = False


total_area=length_of_land*breadth_of_land

logger.info(f"Total Area : {total_area} ")

perimter=2*(length_of_land+breadth_of_land);

logger.info(f"Perimter is : {perimter}")



# floor ceil

print(5/2)
print(5//2)


print(ceil(5/2))

print(floor(5/2))

# type cast

# implicit

a=1.9
b=6

print(a+b)


#explicit

a="123"
b="12"

print(int(a)+int(b))



Length = int(input("Length : "))
Breadth = int(input("Breadth : "))

# Calculating area
Area = Length * Breadth

# Logging output
logger.info(f"Total Area is : {Area}.")





