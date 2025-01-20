A = int(input("A kesmasi uzunligini kiriting (A > B): "))
B = int(input("B kesmasi uzunligini kiriting: "))

count = 0
while A >= B:
    A -= B
    count += 1

print("Joylashtirilgan B kesmalari soni:", count)
