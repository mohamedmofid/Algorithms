def mo3en_area(r1,r2) -> float:
  return (r1+r2)/2

if __name__=="__main__":
  r1=float(input('enter r1: '))
  r2=float(input('enter r2: '))
  area=mo3en_area(r1,r2)
  print(area)