# Merge sort
import random


def mergesort(arr, i, j):
  mid = 0
  if i < j:
    mid = (i + j) / 2
    mergesort(arr, i, mid)
    mergesort(arr, mid + 1, j)
    merge(arr, i, mid, j)


def merge(arr, i, mid, j):

  N = len(arr)
  temp = [0] * N
  l = i
  r = j
  m = mid + 1
  k = l
  while l <= mid and m <= r:
    if arr[l] <= arr[m]:
      temp[k] = arr[l]
      l += 1
    else:
      temp[k] = arr[m]
      m += 1
    k += 1

  while l <= mid:
    temp[k] = arr[l]
    k += 1
    l += 1
  while m <= r:
    temp[k] = arr[m]
    k += 1
    m += 1
  for i1 in range(i, j + 1):
    arr[i1] = temp[i1]
  print ("After Merge: " + str(arr[i:j + 1]))

arr = [random.randint(0,100000)for i in range(1000)]
print("Initial Array: " + str(arr))
print(len(arr))
mergesort(arr, 0, len(arr) - 1)
