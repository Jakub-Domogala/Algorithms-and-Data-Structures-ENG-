# Computing complexity  = O(nlogn)
# Memory complexity     = O(nlogn) could also be O(n) if implemented differently
# n - number of elements
# Stable

from random import randint


#-----------------------------------------------------------------------------------------------------------------------
def divide(T, b, e):
  if b < e:
    mid = (b + e) // 2
    divide(T, b, mid)
    divide(T, mid+1, e)
    return merge(T, b, mid, mid+1, e)


def merge(T, bl, el, br, er):
  temp = []
  start_index = bl
  for i in range (er - bl + 1):
    if bl > el:
      while br <= er:
        temp.append(T[br])
        br += 1
      break
    if br > er:
      while bl <= el:
        temp.append(T[bl])
        bl += 1
      break

    if T[bl] > T[br]:
      temp.append(T[br])
      br += 1
    else:
      temp.append(T[bl])
      bl += 1
  j = 0
  for i in range(start_index, er + 1):
    T[i] = temp[j]
    j += 1
  return T

def mergesort(T): 
  divide(T, 0, len(T)-1)
#-----------------------------------------------------------------------------------------------------------------------

A = []
for i in range(0,10):
    A = A + [randint(0,13)]

print("przed: \t",A)
mergesort(A)
print("po: \t",A)