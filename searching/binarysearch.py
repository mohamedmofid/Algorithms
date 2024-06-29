from typing import Sequence,TypeVar

T=TypeVar('T')

def binary_search(arr: Sequence,key: T) -> int:
  left=0
  right=len(arr)-1
  while left <= right:
    mid = (left+right) // 2
    if arr[mid]==key:return mid
    if arr[mid]>key: 
      right = mid-1
    else: 
      left = mid+1
  return -1
  
if __name__ == '__main__':
  items=[1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 16, 17, 18, 19]
  keys=[1,10,19,13]
  for key in keys:
    r=binary_search(items,key)
    print(r)