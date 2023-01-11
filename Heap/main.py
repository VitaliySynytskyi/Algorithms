from Heap import Heap as Heap
arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]


a = Heap(arr)
print(f"1. {a.heap_arr = }")
a.BuildMinHeap()
print(arr == a.heap_arr)
a.ShowHeap()

print(f"Min value - {a.HeapMin()}")
print(f"Max value - {a.HeapMax()}")
# print(a.ExtractMin())
# a.ShowHeap()
a.HeapDecreaseKey(index=3, data=0)
a.ShowHeap()
