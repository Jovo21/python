N = int(input("N sonini kiriting: "))
K = int(input("K sonini kiriting: "))

quotient = 0
while N >= K:
    N -= K
    quotient += 1

print("Butun qismi:", quotient)
print("Qoldiq:", N)
