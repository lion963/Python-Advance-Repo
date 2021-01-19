countries = [x for x in input().split(', ')]
cities = [x for x in input().split(', ')]
country_city = {countries[i]: cities[i] for i in range(len(countries))}
[print(f'{key} -> {value}') for key, value in country_city.items()]
