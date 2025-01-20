# savol 56

oylik = int(input("Oylik kiriting : "))

soliq = 0

if oylik >= 10000000:
    soliq = oylik / 100 * 15.5
elif oylik >= 7000000:
    soliq = oylik / 100 * 12.3
elif oylik >= 3000000:
    soliq = oylik / 100 * 5.6
else:
    soliq = oylik / 100 * 0

print(f"Sizning solig'ingiz {soliq}")
