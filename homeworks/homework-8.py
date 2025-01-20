balans = int(input("Sizda bor summani kiriting : "))
masofa = float(input("Manzilgacha bolgan masofani kiriting : "))
taxi = int(input("taxi 1 km uchun narxni kiriting : "))
avtobus = int(input("Avtobus yol xaqqini kiriting : "))
metro = int(input("Metro yol xaqqini kiriting : "))

check = ((taxi + avtobus + metro) <= balans)

print(check)