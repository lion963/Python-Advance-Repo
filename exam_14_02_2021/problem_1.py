from collections import deque

effects = list(map(int, input().split(', ')))
firework_explosive = list(map(int, input().split(', ')))

firework_effects = deque(effects)
fireworks = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
is_win = False

while firework_effects and firework_explosive and not is_win:
    while firework_effects:
        if firework_effects[0] <= 0:
            firework_effects.popleft()
        else:
            break
    while firework_explosive:
        if firework_explosive[-1] <= 0:
            firework_explosive.pop()
        else:
            break

    if firework_effects and firework_explosive:
        if (firework_effects[0] + firework_explosive[-1]) % 3 == 0 and not (firework_effects[0] + firework_explosive[-1]) % 5 == 0:
            fireworks['Palm Fireworks'] += 1
            firework_effects.popleft()
            firework_explosive.pop()

        elif not (firework_effects[0] + firework_explosive[-1]) % 3 == 0 and (firework_effects[0] + firework_explosive[-1]) % 5 == 0:
            fireworks['Willow Fireworks'] += 1
            firework_effects.popleft()
            firework_explosive.pop()

        elif (firework_effects[0] + firework_explosive[-1]) % 3 == 0 and (firework_effects[0] + firework_explosive[-1]) % 5 == 0:
            fireworks['Crossette Fireworks'] += 1
            firework_effects.popleft()
            firework_explosive.pop()
        else:
            firework_effects.append(firework_effects.popleft() - 1)

    if fireworks['Palm Fireworks'] >= 3 and fireworks['Willow Fireworks'] >= 3 and fireworks[
        'Crossette Fireworks'] >= 3:
        is_win = True

if is_win:
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
