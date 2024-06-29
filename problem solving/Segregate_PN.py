# input: array of nums
# output: array of nums with Segregate positive in right and negative for left with respect to the order
# proccess ??? use merge sort techniqe
# but always start form left to be sure that we fill in order and ..

def merge(arr:list, left:int, mid:int, right:int) -> None:
  # clac subarrays len
  left_len=mid-left+1
  right_len=right-mid #..
  left_arr=[]
  right_arr=[]
  # create them
  i,j,k=0,0,left
  while i<left_len:
    left_arr.append(arr[k])
    i+=1
    k+=1
  while j<right_len:
    right_arr.append(arr[k])
    j+=1
    k+=1
    
  i,j,k=0,0,left
  # loop on left array 
  while i<left_len:
  # if face positive item break
    if left_arr[i]>=0:
      break
    arr[k]=left_arr[i]
    i+=1
    k+=1
  # loop on right array 
  while j<right_len:
  # if face positive item break
    if right_arr[j]>=0:
      break
    arr[k]=right_arr[j]
    j+=1
    k+=1
  # fill the remain left array
  while i<left_len:
    arr[k]=left_arr[i]
    i+=1
    k+=1
  # fill the remain right array
  while j<right_len:
    arr[k]=right_arr[j]
    j+=1
    k+=1

def segregate(arr: list, left:int, right:int) -> None:
# base case
  if left>=right:return
# calc mid
  mid=(left+right) // 2
# call your self twice for the left subarray and the right one
  segregate(arr,left,mid)
  segregate(arr,mid+1,right)
# start merge
  merge(arr,left,mid,right)

if __name__ == '__main__':
  array= [3,4,-2,5,-3,6,8,-10,-1]
  print(array)
  segregate(array,0,len(array)-1)
  print(array)
