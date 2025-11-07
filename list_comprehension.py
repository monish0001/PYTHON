arr=[]

for i in range(1,101):
    arr.append(i)

# by for loop
for item in arr:
    print(item)
    
# list comprehension only IF

even_list=[even for even in arr if even%2==0]
print(even_list)

odd_list=[odd for odd in arr if odd%2!=0]
print(odd_list)


# list comprehension with ELSE IF


even_odd_list=["EVEN" if item%2==0 else "ODD"  for item in arr]

print(even_odd_list)




