def custom_print(*args, **kwargs):
    sep_0 = ' '
    end_0 = '\n'
    true_list = []
    for x in kwargs:
        if x == 'end':
            end_0 = kwargs[x]
        elif x == 'sep':
            sep_0 = kwargs[x]
        else:
            true_list.append(f'{x}={kwargs[x]}')
    print(*args, *true_list, sep=sep_0, end=end_0)
