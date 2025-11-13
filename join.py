# list =["A","B","C","D","E","F","G"]


# result="";


# for item in list:
#     result=result+item
    
# print(result)


# join    -> ="sparater".join(iterable) iterable element should be string

# result ="".join(list)
# print(result)



# list =[1,2,3,4,5,6,78,9,0]
# result ="".join(str(list))
# print(result)


# dict={
#     "Monsih":2050,
#     "Ajay":4098,
#     "Danish":8631
# }
# result =" * ".join(dict)
# print(result)


# 1 of the main use of join

state_dept_info = [{"state": "Bihar", "department":"IT"}
,{"state": "Delhi", "department":"Marketing"}]


# Find out all the employee name who are available in the above condition.
# You don't know the exact number of filter condition
# which will come in the above list. It can change in each run.

Query="""select * from(
select e.employee_name, e.state, e.zip, e.salary, d.department
from employee_tbl e
inner join department d
ON e.emp_id = d.emp_id
)a
where salary>100000 """



# select * from(
# select e.employee_name, e.state, e.zip, e.salary, d.department
# from employee_tbl e
# inner join department d
# ON e.emp_id = d.emp_id
# )a
# where salary > 100000 AND state = 'Bihar'
# AND department = 'IT' AND state = 'Delhi'
# AND department = 'Marketing'


# but we cant hard code 



# SOLUTION

# filter_condition =[]

# for condition in state_dept_info:
    
#     for key,value in condition.items():
        
#         filter_condition.append(f"{key}={value}")


# print(filter_condition)
        
    

# result=" OR ".join(filter_condition)

# print(result)

# # NOW FINAL QUERY

# print(Query + " AND " + result)





# Q1. Secure the PII data.
input_list = ["mverma6250@gmail.com","ramesh02@hotmail.com",
         "sohansingh@gmail.com","swatirahane@outlook.com"]

# Input = ["m********0@gmail.com","r******2@hotmail.com",
#         "s********h@gmail.com","s*********e@outlook.com"]

emails=[]
for email in input_list:
    emails.append(email.split('@'))
    

# print(emails)

# masked_email=[]
# for email_list in emails:
#     length=len(email_list[0])
#     start=email_list[0][0]
#     end=email_list[0][length-1]
#     mid='*'*(length-2);
#     post_fix=email_list[1]
#     masked_email.append(start+mid+end+"@"+post_fix)
    
    
# print(masked_email)





Input=["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2"
]

path_list=[]
for str in Input:
    path_list.append(str.split('/'))
    
# print(path_list)
correct_path=[]
for path in path_list:
    for section in path:
        if len(section)==0:
            path.remove(section)
    correct_path.append(path)
    
unique_ips=set()

for path in correct_path:
    unique_ips.add(path[8])

print(unique_ips)  
    


