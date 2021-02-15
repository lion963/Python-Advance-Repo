def stock_availability(delivery_list, *args):
    if args[0] == 'delivery':
        if len(args) > 1:
            for box in args[1:]:
                delivery_list.append(box)

    elif args[0] == 'sell':
        if len(args) == 1:
            if delivery_list:
                delivery_list.pop(0)
        elif len(args) > 1:
            for el in args[1:]:
                if type(el) == int:
                    if delivery_list:
                        for i in range(el):
                            delivery_list.pop(0)
                elif type(el) == str:
                    while el in delivery_list:
                        delivery_list.remove(el)

    return delivery_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
