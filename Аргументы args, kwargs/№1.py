def sum_numbers(*nums):
    sum=0
    for x in nums:
        sum+=x
    return sum

print(sum_numbers(1,2,3,4,5))