sales = input('enter sales for the month: ')
sales = int(sales)#
bonus = 0
if sales > 40000:
    bonus = sales / 100 * 15
bonus = int(bonus)
print ('Bonus earned is: ',bonus)
print ('End of program')