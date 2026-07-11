def filter_by_length(len_w, *strings):
    check_len=[]
    for x in strings:
        if len(x)>=len_w:
            check_len.append(x)
    return check_len

print(filter_by_length(2, 'THE WORLD', 'Санта', 'ку'))    