list_categories = [x for x in input().split(', ')]

n = int(input())
category_dict = {x: [] for x in list_categories}
items_dict = {}
sum_quantity = 0
sum_quality = 0

for i in range(n):
    category, items, qq = input().split(' - ')
    if category in category_dict:
        category_dict[category].append(items)

        quantity_data, quality_data = qq.split(';')
        quantity, value = quantity_data.split(':')
        quality, valu = quality_data.split(':')
        if items not in items_dict:
            items_dict[items] = {quantity: int(value), quality: int(valu)}
        else:
            items_dict[items] = {quantity: int(value), quality: int(valu)}

for item, value in items_dict.items():
    sum_quantity += value['quantity']
    sum_quality += value['quality']

print(f'Count of items: {sum_quantity}')
print(f'Average quality: {sum_quality / len(category_dict):.2f}')
for category, items in category_dict.items():
    print(f"{category} -> {', '.join(items)}")
