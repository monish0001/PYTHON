from loguru import logger

# arr=[]

# for i in range(1,101):
#     arr.append(i)

# # by for loop
# for item in arr:
#     print(item)
    
# # list comprehension only IF

# even_list=[even for even in arr if even%2==0]
# print(even_list)

# odd_list=[odd for odd in arr if odd%2!=0]
# print(odd_list)


# # list comprehension with ELSE IF


# even_odd_list=["EVEN" if item%2==0 else "ODD"  for item in arr]

# print(even_odd_list)


#Question

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = [matrix[j][i] for i in range(3) for j in range(3) if (i + j) % 2 == 0]
print(result)


nums = [1, 2, 3, 4, 5, 6]

result = [x*y for x in nums if x % 2 == 0 for y in range(x) if y % 3 == 0]
print(result)



words = ["apple", "banana", "cherry", "date", "fig", "grape"]


ans=[w[::-1].upper()  for w in words if len(w)%2==0 and w[1] not in "aeiou"]

logger.info(ans)








