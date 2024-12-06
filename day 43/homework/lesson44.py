def count_items(item_list, item):
    return item_list.count(item)

item= ["audi", "bmw", "toyota", "audi", "mitsubishi", "audi"]
item_to_count = "audi" 
result = count_items(item, item_to_count)
print(f"{item_to_count}  {result} ")