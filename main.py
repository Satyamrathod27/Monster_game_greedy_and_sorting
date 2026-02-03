# Number of monsters
n = int(input())


# Bonus power gained after defeating each monster
bonus = []
for _ in range(n):
    bonus.append(int(input()))


for req_power, gain in monsters:
    if current_power >= req_power:
        current_power += gain  # gain bonus power
        defeated += 1
    else:
        break  # can't defeat further monsters

print(defeated)

