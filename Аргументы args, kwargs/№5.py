def custom_print(*args, **kwargs):
    sep0 = " "
    end0 = "\n"
    true_list = []
    
    for key, value in kwargs.items():
        if key == "end":
            end0 = value
        elif key == "sep":
            sep0 = value
        else:
            true_list.append(f"{key}={value}")
            
    print(*args, *true_list, sep=sep0, end=end0)