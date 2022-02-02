#№1
import random
my_list = [random.randint(1,50) for i in range(random.randint(1,50))]

number = tuple(map(lambda n: int(n % my_list[2]), my_list))
print(number)

#№2
def decorator1(func):
    def wrapped():
        return '<3' + func() + '<3'

    return wrapped

def decorator2(func):
    def wrapped():
        return '()()()....' + func() + '....()()()'

    return wrapped

@decorator1
@decorator2
def function():
    return 'Holly shit'
print(function())

#№3
def my_littlefunction1(a):
    return (a * 2)
def my_littlefunction2(b):
    return (b + 10)

funcs = [my_littlefunction1, my_littlefunction2]
for i in range(10):
    numbers = list(map(lambda n: n(i), funcs))
    print(numbers)

my_list = range(1, 100)
numbers = list(filter(lambda n: n % 2 == 0, my_list))
print(numbers)