def print_params1(a = 1, b = 'строка', c = True):
    print(a, b, c)

def print_params2(*args, **kwargs):
    print(*args, kwargs)

def print_params3(*args):
    print(*args)


values_list = [13, 'poem', True]
values_dict = {'a' : 1, 'b' : 2, 'c' : 3}
values_list_2 = [25.123, 'street']

print_params1()
print_params1(b = 25, c = [1, 2, 3])
print_params2(*values_list, **values_dict)
print_params3(*values_list_2, 42)