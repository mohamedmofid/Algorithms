from typing import Sequence

def insertion_sort(L: Sequence,des: bool=False) -> Sequence:
  cmp= '<' if des else '>'
  for i in range(1,len(L)):
    key=L[i]
    j=i-1
    while j>=0:
      if eval(f"L[j] {cmp} key"):L[j+1]=L[j]
      else:break # because we sure for now that every item on the left 
      j-=1       # is sorted
    L[j+1]=key
  return L
l=[7,3,5,6,2]
print(insertion_sort(l,des=True))    