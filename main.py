import heapq

# Input number of items
n = int(input("Enter n: "))

# Initial power
initial_power = int(input("Enter initial power: "))

# Read power list
power = []
print("Enter power values:")
for _ in range(n):
	power.append(int(input()))

# Read bonus list
bonus = []
print("Enter bonus values:")
for _ in range(n):
	bonus.append(int(input()))

# Pair (required_power, bonus)
monsters = list(zip(power, bonus))

# Sort by required power
monsters.sort(key=lambda x: x[0])

current = initial_power
i = 0
killed = 0

# max-heap for bonuses (Python has min-heap so we push negative)
available = []

while True:
	# Add all monsters we can currently kill
	while i < n and monsters[i][0] <= current:
            heapq.heappush(available, -monsters[i][1])
            i += 1

	# If no available monsters, we are stuck
	if not available:
    	    break

	# Kill the available monster with the maximum bonus
	best_bonus = -heapq.heappop(available)
	current += best_bonus
	killed += 1

print("Maximum monsters killed:", killed)
print("Final power:", current)

