def age_assignment(*args, **kwargs):
    name_age_dict = {}
    for el in args:
        for key, value in kwargs.items():
            if key == el[0]:
                name_age_dict[el] = value
    return name_age_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
