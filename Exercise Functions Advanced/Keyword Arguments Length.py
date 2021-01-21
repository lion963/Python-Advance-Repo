def kwargs_length(**kwargs):
    count = 0
    for el in kwargs:
        count += 1
    return count


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
