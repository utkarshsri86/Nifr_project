import logging

## logging settings
logging.basicConfig(
    level =logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("Arithmatic app")

def add(a,b):
    result =a+b
    logger.debug(f"Adding {a} +{b},result")
    return result


def substraction(a,b):
    result =a-b
    logger.debug(f"substraction {a} -{b},result")
    return result


def multiplication(a,b):
    result =a*b
    logger.debug(f"multiply {a}*{b},result")
    return result


def divide(a,b):
    try:
        result =a / b
        logger.debug(f"divide {a} /{b},result-")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None


print(add(10,15))
print(substraction(5,2))
print(multiplication(6,7))
print(divide(54,6))


from concurrent.futures import ThreadPoolExecutor
import time
def print_number(number):
    time.sleep(1)
    return f"numbee : {number}"

numbers =[1,2,3,4,5]
if __name__=="__main__":
    with ThreadPoolExecutor(max_workers=3)as executor:
     results=executor.map(print_number)

    for result in results:
     print(result)
  
   
