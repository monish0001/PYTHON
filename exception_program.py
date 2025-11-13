from loguru import logger

def find_unique_names(file_path):
    try:
        
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()] 

        
        if not lines:
            raise Exception("Error: The file is empty!")

        unique_names = set(lines)

        print("Unique names found in the file:")
        for name in unique_names:
            print(name)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(e)


file_path = "names.txt"
# find_unique_names(file_path)

def solve(path):
    
    try:
        
        with open(path,'r') as file:
            lines=[]
            for line in file:
                lines.append(line)
                
            unique_names = set(lines)
            
            
        if not  lines:
                raise Exception("Empty file.......")

        print("Unique names found in the file:")
        for name in unique_names:
            print(name)
                
            
            
    except FileNotFoundError:
        
        raise FileNotFoundError(f" {path} File does not present")
    except Exception as e:
        logger.error(e)
        raise e
            


file_path = "names1.txt"
try:
    solve(file_path)  # file does not exist
except Exception as e:
    logger.info(f"Handled in main: {e}")




   
