def get_len(var, var_len=0):
    if type(var) ==int:
        var_len = var_len + var
        return var_len
    if type(var) ==str:
        var_len= var_len + len(var)
        return var_len
    if len(var) == 0:
        return 0
    if type(var) == dict:
        for key, value in var.items():
            var_len = var_len + get_len(key)
            var_len = var_len + get_len(value)
        return var_len
    if type(var) == tuple or type(var) == set:
        var=list(var)
    if type(var) ==list:
        for value in var:
            var_len = var_len + get_len(value)
        return var_len
    return var_len

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = get_len(data_structure)
print(result)