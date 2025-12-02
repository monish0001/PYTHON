# from loguru import logger

# def generic_logging(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)


# logger.info("first function call : ")

# generic_logging(status="sucess", staus_code=200, message="successfully")

# logger.info("second function call : ")

# generic_logging(status="fail", staus_code=501, error="db connection fail")



# from loguru import logger

# def generic_logging(**kwargs):
    
#     log_message = " | ".join([f"{key}={value}" for key, value in kwargs.items()])
#     logger.info(log_message)


# logger.info("first function call :")
# generic_logging(status="success", status_code=200, message="successfully")

# logger.info("second function call :")
# generic_logging(status="fail", status_code=501, error="db connection fail")




from loguru import logger


logger.add("log_file.txt")



def generic_logging(**kwargs):
    
    log_message = " | ".join([f"{key}={value}" for key, value in kwargs.items()])
    logger.info(log_message)


logger.info("first function call :")
generic_logging(status="success", status_code=200, message="successfully")

logger.error("second function call :")
generic_logging(status="fail", status_code=501, error="db connection fail")









