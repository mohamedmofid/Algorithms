# input - procceses - output
# x, y  - calc sum of xi2,yi2,xiyi - r of x, y
          # calc the r fo x,y
# input the x set and y set
# loop on x,y by index
# calc the sum of xi2,yi2,xiyi,xi,yi
# calc r by 
# print(r)
import keyboard
def correlation(x,y) -> float:
  xi2,yi2,xyi,xi,yi= 0, 0, 0, 0, 0
  n=len(x)
  for _xi,_yi in zip(x,y):
    xi2+=_xi**2
    yi2+=_yi**2
    xyi+=_xi*_yi
    xi+=_xi
    yi+=_yi
  numerator= n * xyi - xi * yi
  denominator= ((n * xi2 - xi**2) * (n * yi2 - yi**2))**0.5
  if denominator==0:
    return 0
  corr=numerator/denominator
  return corr
# x=list(range(3))
# y=list(range(3))
i=0
x,y=[],[]
print('enter c when done writing')
while True:
  temp=input(f"x{i+1},y{i+1}= ")
  if temp=='c':break
  temp=temp.split(',')
  try:
    x.append(int(temp[0]))
    y.append(int(temp[1]))
  except ValueError:
    print('bad input enter a valid number')
    continue
  i+=1
corr=correlation(x,y)
print(f"x= {x}")
print(f"y= {y}")
print(f'r(x,y)  = {corr}')
