
# ----- 1 ------

# for i in range(1,6):
#     for j in range(1,5):
#         print("*", end=" ")
#     print()

# ----2-------

# for i in range(1,6):
#     for j in range(1,5):
#         if j == 1:
#             print("#", end=" ")
#         else:
#             print("*", end = " ")
#     print()

# -----3------

# for i in range(1,6):
#     for j in range(1,5):
#         if j == 1 or i == 1:
#             print("#", end=" ")
#         else:
#             print("*", end = " ")
#     print()


# -----4-------

# for i in range(1,6):
#     for j in range(1,5):
#         if j == 1 or i == 1 or j == 4:
#             print("#", end=" ")
#         else:
#             print("*", end = " ")
#     print()

# -----5-------

# for i in range(1,5):
#     for j in range(1,5):
#         if j == 1 or i == 1 or j == 4 or i == 4:
#             print("#", end=" ")
#         else:
#             print("*", end = " ")
#     print()

# -----6-----

# for i in range(1,6):
#     for j in range(1,5):
#         if j == 1 or i == 1 or j == 4 or i == 5 or i == 3:
#             print("#", end=" ")
#         else:
#             print("*", end = " ")
#     print()

# -----7------

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 2 and j == 2 or i == 2 and j == 4 or i == 4 and j == 2 or i == 4 and j == 4:
#             print("0", end=" ")
#         else:
#             print("#", end = " ")
#     print()

# ------ 8 ---------

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 and j == 1 or i == 2 and j == 2 or i == 3 and j == 3 or i == 4 and j == 4 or i == 5 and j == 5:
#             print("0", end=" ")
#         else:
#             print("#", end = " ")
#     print()

# ------ 9 --------

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 and j == 1 or i == 2 and j == 1 or i == 2 and j == 2 or i == 3 and j == 1 or i == 3 and j == 2 or i == 3 and j == 3 or i == 4 and j == 1 or i == 4 and j == 2 or i == 4 and j == 3 or i == 4 and j == 4 or i == 5 and j == 1 or i == 5 and j == 2 or i == 5 and j == 3 or i == 5 and j == 4 or i == 5 and j == 5:
#             print("0", end=" ")
#         else:
#             print("#", end = " ")
#     print()

# ------ 10 -------

# for i in range(1,6):
#     for j in range(1,6):
#         if (i + j) % 2 == 0:
#             print("0", end=" ")
#         else:
#             print("1", end=" ")
#     print()

# ----- 11 -----

# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 and j == 1 or i == 1 and j == 5 or
#             i == 2 and j == 2 or i == 2 and j == 4 or
#             i == 3 and j == 3 or
#             i == 4 and j == 2 or i == 4 and j == 4 or
#             i == 5 and j == 1 or i == 5 and j == 5):
#             print("0", end=" ")
#         else:
#             print("1",end=" ")
#     print()

# ------ 12 ------
# for i in range(1,6):
#     for j in range(1,6):
#         if (i==2 and j==3 or i==3 and j==2 or i==3 and j==4 or i==4 and j==3):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()

# ----- 13 -------

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1:
#             print("A" ,end=" ")
#         elif i == 2:
#             print("B",end=" ")
#         elif i == 3:
#             print("C", end=" ")
#         elif i == 4:
#             print("D", end=" ")
#         elif i == 5:
#             print("E", end=" ")
#     print()

# -----14-----
# summa = 1
# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{summa}",end=" ")
#         summa = summa + 1
#     print()

# ----- 15 ------

# summa = 1
# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{summa}",end=" ")
#         summa = summa + 2
#     print()

# ----- 16 -----

# summa = 1
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{summa}",end=" ")
#         summa = summa + 1
#     print()

# ---- 17 -----

# ----22-----

# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 and j == 1 or i == 2 and j ==1 or i == 2 and j ==2 or i == 3 and j == 1 or i == 3 and j == 2 or i == 3 and j == 3 or i == 4 and j == 1 or i == 4 and j==2 or i == 4 and j == 3 or i == 4 and j == 4 or i == 5 and j == 1 or i == 5 and j == 2 or i == 5 and j == 3 or i == 5 and j == 4 or i == 5 and j == 5):
#             print("*",end = " ")
#         else:
#             print(" ",end=" ")
#     print()

# ---- 23 -----

# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 and j == 1 or i == 2 and j ==1 or i == 2 and j ==2 or i == 3 and j == 1 or i == 3 and j == 2 or i == 3 and j == 3 or i == 4 and j == 1 or i == 4 and j==2 or i == 4 and j == 3 or i == 4 and j == 4 or i == 5 and j == 1 or i == 5 and j == 2 or i == 5 and j == 3 or i == 5 and j == 4 or i == 5 and j == 5):
#             print(j ,end = " ")
#         else:
#             print(" ",end=" ")
#     print()

# ------ 24 -------

# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 and j == 1 or i == 2 and j ==1 or i == 2 and j ==2 or i == 3 and j == 1 or i == 3 and j == 2 or i == 3 and j == 3 or i == 4 and j == 1 or i == 4 and j==2 or i == 4 and j == 3 or i == 4 and j == 4 or i == 5 and j == 1 or i == 5 and j == 2 or i == 5 and j == 3 or i == 5 and j == 4 or i == 5 and j == 5):
#             print(i ,end = " ")
#         else:
#             print(" ",end=" ")
#     print()

# ----- 25 ------


# row = int(input("Row: "))
# col = int(input("Column: "))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (j == 1 or j == col
#             or (i == j and i <= ortaRow)
#             or (i + j == col + 1 and i <= ortaRow)
#         ):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')


#     print()