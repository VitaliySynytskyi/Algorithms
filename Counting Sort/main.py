import copy
import random
from sort import *


def readFromReady():
    res = [54,76,34,99,87,43,2,5]
    items = [random.randint(0, 9) for i in range(100)]
    return items


def readFrominput():
    res = input('Please, input your array: ')
    res = [int(item) for item in res.strip().split()]
    return res


func = {
    1: readFromReady,
    2: readFrominput,
}


try:
    # while True:
    answer = input('Please, write way which do you want to use\n 1) Read from ready array\n 2) Read from terminal\n'
                'Your answer: ')
    try:
        answer = int(answer)
    except ValueError:
        print('Please, write number\n')
    else:
        if answer not in func.keys():
            print('Please, write correct number\n')
        else:
            array = func[answer]()
            array_1 = copy.copy(array)
            array_1.sort()
               
            print(f"Your array is:", *array, sep=' ')

            RadixSort(array)
            print(f"Sorted array is:", *array, sep=' ')
            print(f"Is sorted right? {array == array_1}\n", )
except:
    print("Ви десь там цей во помилились")