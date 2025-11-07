from loguru import logger

# immutable unorderdred does not contain duplicate values

set_1={1,1,1,1,1,2,2,2,4,4,4,47,8,9,0,2,3,45,6,6,7,8,8}

logger.info(set_1)
logger.info(set_1)


new_set={} # this will craete dictionary 

new_set=set()

for item in set_1:
    print(item)
