def check_pouch(pouch):
    count = 0
    for bomb, value in pouch.items():
        if value >= 3:
            count += 1
    if count == 3:
        return True
    else:
        return False


from collections import deque

bombs = {'Datura Bombs': 40, 'Cherry Bombs': 60, 'Smoke Decoy Bombs': 120}
bomb_pouch = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

bomb_effect = deque(list(map(int, input().split(', '))))
bomb_casing = list(map(int, input().split(', ')))

while bomb_effect and bomb_casing:
    match = False
    for bomb, value in bombs.items():
        if bomb_effect[0] + bomb_casing[-1] == value:
            bomb_effect.popleft()
            bomb_casing.pop()
            bomb_pouch[bomb] += 1
            match = True
            break
    if not match:
        bomb_casing[-1] -= 5
        if bomb_casing[-1] < 0:
            bomb_casing.pop()
    if check_pouch(bomb_pouch):
        break

if check_pouch(bomb_pouch):
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effect))}")
else:
    print('Bomb Effects: empty')

if bomb_casing:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casing))}")
else:
    print('Bomb Casings: empty')

for bomb, value in dict(sorted(bomb_pouch.items(), key=lambda x: x[0])).items():
    print(f'{bomb}: {value}')
