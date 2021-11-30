import copy
import numpy
import time

from algorithms.BubbleSort import *
from algorithms.BucketSort import *
from algorithms.CountingSort import *
from algorithms.HeapSort import *
from algorithms.QuickSort import *

sortedArr = numpy.arange(0, 1000000)
sortedRevArr = sortedArr[::-1]
baseRandomArr = numpy.random.randint(1000000, size=1000000)
copyRandomArr1 = copy.deepcopy(baseRandomArr)
copyRandomArr2 = copy.deepcopy(baseRandomArr)
copyRandomArr3 = copy.deepcopy(baseRandomArr)
copyRandomArr4 = copy.deepcopy(baseRandomArr)


def BubbleSortTimeTest(arr):
    start = time.time()
    bubblesort(arr)
    end = time.time()
    return round(end - start, 6)


def BucketSortTimeTest(arr):
    start = time.time()
    bucketsort(arr)
    end = time.time()
    return round(end - start, 6)


def CountingSortTimeTest(arr):
    start = time.time()
    countingsort(arr)
    end = time.time()
    return round(end - start, 6)


def HeapSortTimeTest(arr):
    start = time.time()
    heapsort(arr)
    end = time.time()
    return round(end - start, 6)


def QuickSortTimeTest(arr):
    start = time.time()
    quicksort(arr)
    end = time.time()
    return round(end - start, 6)


# print(copyRandomArr1)
print("------------------------------------------------------------")
print("HeapSort")
print("------------------------------------------------------------")
print(HeapSortTimeTest(copyRandomArr1))
print("random arr\n")
print(HeapSortTimeTest(sortedArr))
print("sorted arr\n")
print(HeapSortTimeTest(sortedRevArr))
print("reverse sorted arr\n")
print("------------------------------------------------------------")

# print(copyRandomArr2)
print("CountingSort")
print("------------------------------------------------------------")
print(CountingSortTimeTest(copyRandomArr2))
print("random arr\n")
print(CountingSortTimeTest(sortedRevArr))
print("sorted arr\n")
print(CountingSortTimeTest(sortedArr))
print("reverse sorted arr\n")
print("------------------------------------------------------------")

# print(copyRandomArr3)
print("QuickSort")
print("------------------------------------------------------------")
print(QuickSortTimeTest(copyRandomArr3))
print("random arr\n")
print(QuickSortTimeTest(sortedArr))
print("sorted arr\n")
print(QuickSortTimeTest(sortedRevArr))
print("reverse sorted arr\n")
print("------------------------------------------------------------")

# print(copyRandomArr4)
print("BucketSort")
print("------------------------------------------------------------")
print(BucketSortTimeTest(copyRandomArr4))
print("random arr\n")
print(BucketSortTimeTest(sortedRevArr))
print("sorted arr\n")
print(BucketSortTimeTest(sortedArr))
print("reverse sorted arr\n")
