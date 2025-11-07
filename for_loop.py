from loguru import logger
# names =["Monish","Karan","Ajay","Salu","Kalu"]


# for name in names:
#     print(name)
    

# logger.info("Mathod 2 :")

# for i in range(len(names)):
#     print(names[i])
    
# # output
    
# for name in names:
#     logger.info(name)

# logger.info("Method 2 :")

# for i in range(len(names)):
#     logger.info(names[i])




# for i in range(11):
#     print((i+1)*'*')
    
# logger.info("Odd Even")

# for i in range(101):
#     if i%2==0:
#         print(i)
    
    
# for i in range(2,101,2):
#     print(i)
    
    
    
    
# for i in range(1,101):
#     if i%2==0:
#         print(i)



paragraph = """ Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University """

list=paragraph.lower().split(' ');
print(list)


count=0;


for letter in list:
    if letter=="the":
        count=count+1
    

logger.info(f" count of the is : {count}")
