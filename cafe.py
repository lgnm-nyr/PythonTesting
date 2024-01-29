#defining menu with stock and prices
menu = ["coffee", "tea", "cake", "sandwich"]

stock = {"coffee": 1000,
         "tea": 1000,
         "cake": 500,
         "sandwich": 500
         }

price = {"coffee": 3.5,
         "tea": 3,
         "cake": 5,
         "sandwich": 4
         }

#defining variable to setup calculate total stock value
total_stock_value = 0

#loop to go calculate value of all items on menu
for items in menu:
    
    item_value = stock[items] * price[items]
    print(items, "£" + str(item_value)) #checking value of individual items
    total_stock_value += item_value #adding each item value to total value

print('=' * 50)
print("Total stock is worth: £" + str(total_stock_value))
print('=' * 50)
