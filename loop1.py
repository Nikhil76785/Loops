m = int(input("Enter the number whose sum you want to find: "))
sum = 0

for i in range(1, m + 1):
    sum = sum + i
    print(f"Sum = {sum}")