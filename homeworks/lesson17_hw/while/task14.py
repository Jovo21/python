a = float(input("a sonini kiriting (a > 1): "))

k = 1
summa = 0
while summa + 1 / k <= a:
    summa += 1 / k
    k += 1

print("Natija:", k - 1)
print("Yig'indi:", summa)
