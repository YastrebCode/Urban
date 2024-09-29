def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)
print_params()

value_list = [5, 'data', True]
value_dict = {'a': False, 'b': 7, 'c': 'saved'}
print_params(*value_list)
print_params(**value_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)