def print_kwargs (**kwargs):
    for x in kwargs:
        print(f'name: {x}, pet: {kwargs[x]}')

print_kwargs(Any='dog', Katty='cat')