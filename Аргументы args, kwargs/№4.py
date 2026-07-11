def calculate_total_price(arg, **sails):
    sum_sails=sum([ sails[s] for s in sails])
    final_price=arg - arg/100*sum_sails
    return final_price

print(calculate_total_price(100, student=5, cupon=5))