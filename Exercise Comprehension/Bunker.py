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

for item, value in items_dict.items():
    sum_quantity += value['quantity']
    sum_quality += value['quality']

category_count = 0
for category, value in category_dict.items():
    if value:
        category_count += 1

print(f'Count of items: {sum_quantity}')
print(f'Average quality: {sum_quality / category_count:.2f}')
for category, items in category_dict.items():
    print(f"{category} -> {', '.join(items)}")

# categories={category:[] for category in input().split(', ')}
#
# quantity=0
# quality=0
#
# for _ in range(int(input())):
#     data=input().split(' - ')
#     categories[data[0]].append(data[1])
#
#     information_data=data[2].split(';')
#     quantity+=int(information_data[0].split(':')[1])
#     quality+=int(information_data[1].split(':')[1])
#
# print(f'Count of items: {quantity}')
# print(f'Average quality: {quality/len(categories):.2f}')
# [print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]
