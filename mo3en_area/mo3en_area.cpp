#include <iostream>
using namespace std;

int mo3en_area(int r1, int r2)
{
  return (r1+r2)/2;
}

int main()
{
  int r1,r2,a;
  cout << "enter r1: ";
  cin >> r1; 
  cout << "enter r2: ";
  cin >> r2 ;
  a=mo3en_area(r1,r2);
  cout << a << '\n';
  return 0;
}