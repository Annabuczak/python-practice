# FOR loop: repeat a known number of times
print("FOR loop: 1 to 5")
for i in range(1, 6):
    print(i)

print("\nFOR loop: say hello 3 times")
for _ in range(3):
    print("Hello")

# WHILE loop: repeat while a condition is true
print("\nWHILE loop: count 1 to 5")
count = 1
while count <= 5:
    print(count)
    count += 1