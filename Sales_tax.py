# setting initial values (initializing variables)

cost = 1
totalCost = 0

# providing instructions to the user
print("Input prices. Enter 0 to indicate that you are done entering.")

# user will stay in the following loop until they enter the value 0
while cost != 0:
    strCost = raw_input("Enter the cost of the item: ")
    # raw input is a string, we are casting it to a float and saving the new value to cost
    cost = float(strCost)
    # this makes total cost equal to its current value plus the new cost value
    totalCost += cost
else:
    # when the user enters 0, the total will appear on screen
    print ("The running total is: $" + str(totalCost))

# the sales tax on the total is 6%
sales_tax = totalCost * .06
# tax on total
print "The sales tax on the running total is 6%, which is equal to: $" + str(round(sales_tax, 2))


# the sales tax + the total is the grand total
grandTotal = float(sales_tax) + totalCost

# we have to cast grandTotal to a string to be able to print it
print("The running total, with sales tax, equals the grand total of: $" + str(round(grandTotal, 2)))
