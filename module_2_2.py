first=5
second=7
third=2
numbers = str(input('Нужное число'))
print(numbers)
if str(first) in numbers and str(second) in numbers and str(third) in numbers:
    print(3)
elif str(first) in numbers and str(second) in numbers or str(second) in numbers and str(third) in numbers or str(first) in numbers and str(third) in numbers:
    print(2)
else:
    print(0)

