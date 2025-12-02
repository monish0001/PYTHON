# exception handling? What is
# why do we need?
# when to (raise) exception and when not to?
# Some real time use cases
# Write a program to open file is empty then raise a  exception  it's not the unique then find out all of unique names in the file


from loguru import logger

def cost(*args,discount=.10):
    try:
        sum=0
        for item in args:
            sum+=item
        sum=sum-discount*sum
        logger.info(f"Total cost is : {sum}")
    except Exception as e:
        print(e)
    logger.info("After exception")
    
    
def cost(*args,discount=.10):
    try:
        sum=0
        for item in args:
            sum+=item
        sum=sum-discount*sum
        logger.info(f"Total cost is : {sum}")
    except Exception as e:
        logger.info(e)
    logger.info("After exception")
    
def cost1(*args,discount=.10):
    try:
        sum=0
        for item in args:
            sum+=item
        sum=sum-discount*sum
        logger.info(f"Total cost is : {sum}")
    except TypeError as e:
        logger.info("type error.....")
        raise Exception("type error prvided values are not integer.......")
    except ValueError as e:
        logger.info("ValueError error.....")
        raise Exception("ValueError error..... some values is not defined")
    except Exception as e:
        logger.info("We can process this amount.....")
        raise e
    logger.info("After exception")
    
    


# cost(10,20,30,40,'50',60,discount=.10)

try:
    cost1(10,20,30,40,'50',60,discount=.10)
except Exception as e:
    logger.info(e)
    