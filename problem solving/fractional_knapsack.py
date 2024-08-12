from typing import Union

class Item:
  def __init__(self, name:str,weight:float,value:float) -> None:
    
    self.name=name
    self.weight=weight
    self.value=value
    self.ratio=value/weight
  
  @property
  def data(self) -> list:
    return [self.name,self.weight,self.value,self.ratio]
  
  def __str__(self) -> str:
    return f"{self.name} {self.weight} {self.value} {self.ratio}"
  
  
class Knapsack:
  def __init__(self, max_weight:int) -> None:
    self.max_weight = max_weight
    self.items = []
    self.current_weight = 0
    self.total_value = 0
  
  def add_item(self, item:Item) -> None:
    diff=self.max_weight - self.current_weight
    if item.weight>diff:
      adjusted_item = Item(item.name, diff, diff * item.ratio)
    else:
      adjusted_item=item

    self.items.append(adjusted_item)
    self.current_weight+=adjusted_item.weight
    self.total_value+=adjusted_item.value
  
  def __str__(self) -> str:
    message = (f"Total Value: {self.total_value}\n"
               f"Current Weight: {self.current_weight}\n"
               f"Items: {len(self.items)}\n"
               "n w v\n") + " \n".join([f"{item.name} {item.weight} {item.value}" for item in self.items])
    return message
  

if __name__ == "__main__":
  values=[4,9,12,11,6,5]
  weights=[1,2,10,4,3,5]
  items=[Item(i,weights[i],values[i]) for i in range(len(weights))]
  items_str="\n".join([str(item) for item in items])+'\n'
  print("n w v r\n"+items_str)

  items_sorted = sorted(items, key=lambda item: item.ratio, reverse=True)
  
  bag=Knapsack(12)

  while bag.current_weight<bag.max_weight:
    if items_sorted==[]:break
    bag.add_item(items_sorted.pop(0))

  print(bag)
