def calc_area(a: float, b: float, h: float):
  return 0.5*(a+b)*h

if __name__== "__main__":
  a=float(input('enter the first base a = '))
  b=float(input('enter the 2nd base b = '))
  h=float(input('enter the height h = '))
  area=calc_area(a,b,h)
  print(f'area = h * (a+b) / 2\n',f'    = {area}')
  