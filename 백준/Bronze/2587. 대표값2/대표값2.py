numbers = []

for i in range(5):
    numbers.append(int(input()))

print(sum(numbers) // 5)
print(sorted(numbers)[2])