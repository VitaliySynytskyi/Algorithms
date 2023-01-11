import copy
from Sort import *


def readFromReady():
    res = [54,76,34,99,87,43,2,5]
    return res

def readFrominput():
    res = input('Please, input your array: ')
    res = [int(item) for item in res.strip().split()]
    return res


func = {
    1: readFromReady,
    2: readFrominput
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
            array_2 = copy.copy(array)
            answer = int(input("Which element do you want to find (from 1): "))
            if answer > len(array):
                print("Please, write correct number")
            else:
                print(f"Your array is:", *array, sep=' ')
                QuickSort(array, 0, len(array)-1)
                print(f"Sorted array is:", *array, sep=' ')
                print(f"Is sorted right? {array == array_1}\n====================", )
                print(f"Your element = ", RandomaizedSelect(array_2, 0, len(array_2)-1, answer))
                print(f"Min element = {array[0]}\nMax element = {array[-1]}")
                print(f"Mediana = {my_median(array)}")
except:
    print("Ви десь там цей во помилились")
