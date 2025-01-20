n = int(input("n sonini kiriting: "))

k = 0
power_of_3 = 1
while power_of_3 <= n:
    power_of_3 *= 3
    k += 1

print("Natija:", k)
