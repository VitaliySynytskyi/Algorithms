from Sort import *

try:
    print("Стандартний масив чи ручками заповнити??? 1-готовий 2-ручками ")
    n = int(input())

    if (n==1):
        fd = [54,43,76,34,8734,87,43,2]
        print(fd)
        print(merge_sort(fd))
    else:
        s_inp = []
        print("Ведіть кількість елементів масиву для сортування: ")
        a = int(input())

        for i in range(0, a):
            print("Елемент масиву №" + str(i+1) + " ")
            ele = int(input())
            s_inp.append(ele) # adding the element
        print("Не відсортований масив")
        print(s_inp)
        print("Відсортований масив")
        print(merge_sort(s_inp))
except:
    print("до побачення")