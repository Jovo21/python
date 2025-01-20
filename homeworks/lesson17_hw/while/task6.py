n = int(input("n sonini kiriting: "))

if n % 2 == 0:
    n -= 1

product = 1
while n > 0:
    product *= n
    n -= 2

print("Natija:", product)
