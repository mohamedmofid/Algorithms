import random
from typing import Sequence
# merge
def merge(arr: Sequence, start:int, mid:int, end:int):
  left_length=mid-start+1
  right_length=end-mid
  left_arr=[]
  right_arr=[]
  i,j,k=0,0,start

  while i < left_length:
    left_arr.append(arr[k])
    i+=1
    k+=1
  while j < right_length:
    right_arr.append(arr[k])
    j+=1  
    k+=1
  
  i,j,k=0,0,start
  while i < left_length and j < right_length:
    if left_arr[i] <= right_arr[j]:
      arr[k]=left_arr[i]
      i+=1
    else:
      arr[k]=right_arr[j]
      j+=1
    k+=1

  while i<left_length:
    arr[k]=left_arr[i]
    i+=1
    k+=1
  while j<right_length:
    arr[k]=right_arr[j]
    j+=1
    k+=1

def merge_sort(arr:Sequence, start: int,end: int) -> None:
  if start>=end:return
  mid = start + ((end-start) // 2)
  merge_sort(arr,start,mid)
  merge_sort(arr,mid+1,end)
  merge(arr,start,mid,end)


if __name__ == '__main__':
  array= random.sample(range(1,20),15)
  print(array)
  merge_sort(array,0,len(array)-1)
  print(array)