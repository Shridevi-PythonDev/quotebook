my_list = [100, ' python', 99, 54, 'learn']

def list_compr(my_list):
    return [temp if not isinstance(temp, str) else 0 for temp in my_list]

print(list_compr(my_list))
