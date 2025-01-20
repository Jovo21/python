# hafta1 = ["Dushanba", 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']

# for h in range(1,5):
#     print(f"{h} Hafta")
#     for k in hafta1:
#         print(f"\t{k}")
        


# for i in range(1,6):
#     for j in range(1,6):
#         if j == 1:
#             print('1', end = ' ')
#         else:
#             print('*', end=' ')
#     print()

row = int(input("i ni kiriting: "))
col = int(input("j ni kiriting: "))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if i == 1:
            print(j, end=' ')
        elif j == 1:
            print(i, end=' ')
        else:
            print("*", end=' ')
    print()