n = int(input("n sonini kiriting: "))

power_of_3 = 1
is_power_of_3 = False
while power_of_3 <= n:
    if power_of_3 == n:
        is_power_of_3 = True
        break
    power_of_3 *= 3

if is_power_of_3:
    print("3 ning darajasi")
else:
    print("3 ning darajasi emas")
