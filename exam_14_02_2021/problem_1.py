from collections import deque


def check_positive(num):
    return num > 0


def check_palm(effect, power):
    return (effect + power) % 3 == 0 and not (effect + power) % 5 == 0


def check_willow(effect, power):
    return not (effect + power) % 3 == 0 and (effect + power) % 5 == 0


def check_crossette(effect, power):
    return (effect + power) % 3 == 0 and (effect + power) % 5 == 0


def check_win(dict1):
    for key, value in dict1.items:
        if value >= 3:
            return True
    return False


def print_result(win, firework_effects, firework_explosive, fireworks):
    if win:
        print(f'Congrats! You made the perfect firework show!')
        if firework_effects:
            print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
        if firework_explosive:
            print(f'Explosive Power left: {", ".join(map(str, firework_explosive))}')
        for firework, value in fireworks.items():
            print(f'{firework}: {value}')
    else:
        print(f'Sorry. You can’t make the perfect firework show.')
        if firework_effects:
            print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
        if firework_explosive:
            print(f'Explosive Power left: {", ".join(map(str, firework_explosive))}')
        for firework, value in fireworks.items():
            print(f'{firework}: {value}')


effects = list(map(int, input().split(', ')))
firework_explosive = list(map(int, input().split(', ')))

firework_effects = deque(effects)
fireworks = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
is_win = False

while firework_effects and firework_explosive and not is_win:
    while firework_effects:
        if check_positive(firework_effects[0]):
            break
        else:
            firework_effects.popleft()
    while firework_explosive:
        if check_positive(firework_explosive[-1]):
            break
        else:
            firework_explosive.pop()

    if firework_effects and firework_explosive:
        if check_palm(firework_effects[0], firework_explosive[-1]):
            fireworks['Palm Fireworks'] += 1
            firework_effects.popleft()
            firework_explosive.pop()

        elif check_willow(firework_effects[0], firework_explosive[-1]):
            fireworks['Willow Fireworks'] += 1
            firework_effects.popleft()
            firework_explosive.pop()

        elif check_crossette(firework_effects[0], firework_explosive[-1]):
            fireworks['Crossette Fireworks'] += 1
            firework_effects.popleft()
            firework_explosive.pop()
        else:
            firework_effects.append(firework_effects.popleft() - 1)

    if check_win(fireworks):
        is_win = True

print_result(is_win, firework_effects, firework_explosive, fireworks)
