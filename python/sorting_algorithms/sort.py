import random

def generate_random_list(size):
    values = []

    for i in range(size):
        values.append(int(random.randint(0, 5000)))
    return values

def sort(values):
    sorted_values = []
    values.sort()
    return(values)

print(sort(generate_random_list(100)))
