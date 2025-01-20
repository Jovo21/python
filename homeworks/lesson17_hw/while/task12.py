n = int(input("n sonini kiriting: "))

k = 1
summa = 0
while summa + k <= n:
    summa += k
    k += 1

print("Natija:", k - 1)
print("Yig'indi:", summa)
