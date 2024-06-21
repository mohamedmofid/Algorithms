// input - procceses - output

// (a,b,h) - (.5*(a+b)*h) - area

// input - procceses - output

// (m,h) - (m*h) - area


#include <iostream>
using namespace std;

float trape_area(float a,float b,float h){
  return 0.5 * (a+b) * h;
}

int main(){
  float a,b,h, area;
  cout << "enter the first base a = ";
  cin >> a;
  cout << "enter the 2nd base b = ";
  cin >> b;
  cout << "enter the height h = ";
  cin >> h;
  area=trape_area(a,b,h);
  cout << "area = h * (a+b) / 2\n";
  cout << "     = " << area << "\n";
  return 0;
}
