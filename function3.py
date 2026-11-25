def some_function(apples,bananas):
    total = apples - bananas
    return total
num1 = float(input('Enter a first number: '))
num2 = float(input('Enter a second number: '))
value = some_function(num1,num2)
print(value)