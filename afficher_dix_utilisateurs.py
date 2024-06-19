
numbers = range(0, 10)
numbers = list(numbers)

for number in numbers:
    number += 1
    print(f"Utilisateur {number}")

# Solution  # 1

for i in range(10):
    print(f"Utilisateur {i + 1}")
# Solution  # 2

for i in range(1, 11):
    print(f"Utilisateur {i}")