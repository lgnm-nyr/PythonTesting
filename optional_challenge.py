#create two syntax errors, a runtime error and a logic error

customer_type = gorilla #syntax error - missing quotation marks means variable is not defined properly
normal_price = 6.50
scam_price = 9.85

print('=' *50)
print("A gorilla walks into the bar and says \"I would like a scotch on the rocks please\"")
print('=' *50)
print("The bartender, thinking that the gorilla doesn't know the price of a drink, says that the price is £" + normal_price)
#runtime error above - variable normal_price needs to be converted into a string to be printed correctly
#logic error above as well - For the joke to work, normal_price above should be scam_price
print"The gorilla hands over a £10 note" #syntax error - missing parenthesis
print('=' *50)
print("The bartender, after handing back 15p as change, says that they don't get too many gorillas in his bar")
print('=' *50)
print("The gorilla replies that at £" + scam_price + " a drink, he won't be coming back either")
#runtime error above - same as previous runtime error
#logic error above - same explanation as previous logic error
print('=' *50)