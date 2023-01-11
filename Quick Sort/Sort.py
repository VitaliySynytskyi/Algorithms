import random


def Partition(arr,start,stop):
    pivot = start # pivot
      
    # a variable to memorize where the 
    i = start + 1 
      
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
          
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)


def RandomizedPartition(arr , start, stop):
  
    # Generating a random number between the 
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, stop)
  
    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return Partition(arr, start, stop)


def QuickSort(arr, start, stop):
    if(start < stop):
          
        # pivotindex is the index where 
        # the pivot lies in the array
        pivotindex = RandomizedPartition(arr,\
                             start, stop)
          
        # At this stage the array is 
        # partially sorted around the pivot. 
        # Separately sorting the 
        # left half of the array and the
        # right half of the array.
        QuickSort(arr , start , pivotindex-1)
        QuickSort(arr, pivotindex + 1, stop)




def RandomaizedSelect(arr, start, end, i):
    if arr is None:
        arr = []
    if start == end:
        return arr[start]
    q = RandomizedPartition(arr, start, end)
    k = q - start + 1
    if i == k:
        return arr[q]
    elif i < k:
        return RandomaizedSelect(arr, start, q - 1, i)
    else:
        return RandomaizedSelect(arr, q + 1, end, i-k)

def my_median(sample):
    n = len(sample)
    index = n // 2
    # Sample with an odd number of observations
    if n % 2:
        return sorted(sample)[index]
    # Sample with an even number of observations
    return sum(sorted(sample)[index - 1:index + 1]) / 2

