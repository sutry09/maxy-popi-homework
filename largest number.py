number1 = input('please enter a number: ')
number1 = int(number1)
number2 = input('please enter a second number: ')
number3 = input('please enter a third number: ')
number3 = int(number3)
number2 = int(number2)
if number1 >= number2 and number1 >= number3:
    print ('The largest number is: ', number1)
elif number2 >= number1 and number2 >= number3:
    print ('The largest number is: ', number2)
else:
    print ('The largest number is: ', number3)
