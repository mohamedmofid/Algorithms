# input: text 
# output: the frequancey of each unique character 
# q: does it case sensitive?
# a: for genaric use we do not have to, because we can do like: w->3 + W->2 = 5

from typing import List, Tuple

class Charfreq:
  
  @staticmethod
  def ascii_methode(msg: str):
    """input: msg[ASCII only]"""
    freq= [0] * 127
    # get the char ascii code and count it
    for c in msg:
      char_ascii = ord(c)
      freq[char_ascii]+=1
    # print every non zero freq char and the crosponding freq
    for ascii,char_freq in enumerate(freq):
      if char_freq>0:
        print(chr(ascii),char_freq)
  
  # @staticmethod  
  def genaric_methode(self,msg):
    """input: msg[utf-8] or any"""
    freq={}
    for c in msg:
      if c not in freq:
        freq[c]=0
      freq[c]+=1

    # convert freq dict to 2d arry
    freq_array=[(key,value) for key,value in freq.items()]
    self.sort(freq_array,0,len(freq_array)-1)
    return freq_array
  
  # @staticmethod
  def sort(self,md_arr: List[Tuple[int,int]],start:int,end:int):
    """merge sort custumized to multi d arr"""
    if start>=end:
      return
    
    mid = (start+end) // 2
    self.sort(md_arr,start,mid)
    self.sort(md_arr,mid+1,end)    
    self._merge(md_arr,start,mid,end)
  
  def _merge(self,md_arr,start,mid,end):
    left_length=mid+1-start
    right_length=end-mid
    left_arr,right_arr=[],[]
    i,j,k=0,0,start

    while i<left_length:
      left_arr.append(md_arr[k])
      i+=1
      k+=1
      
    while j<right_length:
      right_arr.append(md_arr[k])
      j+=1
      k+=1
    
    i,j,k=0,0,start

    while i<left_length and j<right_length:      
      if left_arr[i][1]<=right_arr[j][1]:
        md_arr[k]=left_arr[i]
        i+=1
      else:
        md_arr[k]=right_arr[j]
        j+=1
      k+=1
    
    while i<left_length:
      md_arr[k]=left_arr[i]
      i+=1
      k+=1

    while j<right_length:
      md_arr[k]=right_arr[j]
      j+=1
      k+=1

if __name__ == '__main__':
  msg='hello world'
  cf=Charfreq()
  sorted_freq=cf.genaric_methode(msg)
  print(sorted_freq)