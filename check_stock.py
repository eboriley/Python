item = 'Feeding Bootle'
item_stock = 0
unit_price = 12.3


def check_limited_stock():
    if item_stock == 0:
        print(item+" is out of stock")
    elif item_stock < 10:
        print(str(item_stock)+" "+item + "(s) please restock")
    else:
        pass


def check_out():
    check_limited_stock()
    if item_stock == 0:
        pass
    else:
        item_price = float(unit_price) * 3
        item_stock - 1
        rounded_price = float(round(item_price))
        print(item + ": " + str(rounded_price))


check_out()
