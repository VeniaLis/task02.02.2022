#№4
def my_cleanfunc():
    a = int(input('введите число: '))
    b = int(input('введите число: '))
    result = a * 2 + b * 3
    return result

print(my_cleanfunc())

my_list = [1,2,3,4,5,6,7]

def my_dirtyfunc(my_list):
    my_list.append(100)
    return my_list

print(my_dirtyfunc(my_list))

#№5
def my_minfunc():
    my_list1 = [input('Введите числа').split()]
    result = min(my_list1)
    return result

print(min(my_minfunc()))


def my_maxfunc():
    my_list2 = [1,2,3,45,6,8,74,99,66,666,5]
    result = max(my_list2)
    return result

print(int(my_maxfunc()))

#№6
def my_brainfunction(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

my_year = my_brainfunction(int(input("Введите год: ")))
print(my_year)