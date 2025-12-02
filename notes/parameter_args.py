def sum(*values,):
    sum=0
    for item in values:
        sum+=item
    print(f"Total Sum is : {sum}")


sum(10,20,30,40,50,60)


def cost(*args,discount=.10):
    sum=0
    for item in args:
        sum+=item
    sum=sum-discount*sum
    print(f"Total cost is : {sum}")


cost(10,20,30,40,50,60,discount=.10)