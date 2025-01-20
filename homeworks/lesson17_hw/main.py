yigindi = 0

# # Foydalanuvchidan son so'rab davomiy ravishda kiritilgan sonni yig'indiga qo'shamiz
# while True:
#     raqam = int(input("Iltimos, raqam kiriting (yoki to'xtatish uchun 0 kiriting): "))
    
#     # Agar raqam 0 bo'lsa, siklni to'xtatamiz
#     if raqam == 0:
#         break
    
#     # Aks holda, raqamni yig'indiga qo'shamiz
#     yigindi += raqam

# # Yig'indini chiqaramiz
# print("Kiritilgan raqamlar yig'indisi:", yigindi)

# vazifa 2

# a = int(input("A ni kiriting"))
# b = int(input("B ni kiriting!"))

# while a <= b:
#     a += 1
# print(a)

# vazifa 3

# raqamlar = []

# Foydalanuvchidan raqam kiritishni davom ettiramiz
# while True:
#     raqam = input("Iltimos, raqam kiriting (to'xtatish uchun 'stop' kiriting): ")
    
#     # Agar foydalanuvchi 'q' kiritgan bo'lsa, siklni to'xtatamiz
#     if raqam.lower() == 'stop':
#         break
    
#     # Aks holda, raqamni butun son (int) ko'rinishiga o'tkazamiz va ro'yxatga qo'shamiz
#     raqamlar.append(int(raqam))

# # Natijada hosil bo'lgan ro'yxatni chiqaramiz
# print("Kiritilgan raqamlar ro'yxati:", raqamlar)

# x = [1, 2, 3, 14, 5, 6, 6, 7]
# number = 0

# while number < len(x):  
#     if max(x) == x[number]:  
#         print(f"{x[number]} listning eng kattasi")
#     number += 1

# vazifa 5

# while number < len(x):  
#     if max(x) == x[number]:  
#         print(f"{x[number]} listning eng kattasi")
#     number += 1
# print(f"{number} shu indexda")

# vazifa 6

# son = int(input("Sonni kiriting: "))

# 
# if son < 0:
#     son = -son

# xonalar_soni = 0
# while son > 0:
#     son //= 10  
#     xonalar_soni += 1  

# print(f"Kiritilgan son {xonalar_soni} xonali.")

# vazifa 7
# x = [1,2,0,14,5,-6]
# number = 0

# while number < len(x):  
#     if max(x) == x[number]:  
#         print(f"{x[number]} listning eng kattasi")
#     if min(x) == x[number]:
#         print(f"{x[number]} kichik elementi")
#     number += 1
# vazifa 8
# x = [-2,31,104,51,19,7]
# number = 0
# a = 0
# b = 0

# while number < len(x):  
#     if max(x) == x[number]:  
#         a= x[number]
#     if min(x) == x[number]:
#         b = x[number]
#     number += 1

# print(f"kichik {b} , katta {a}")




# vazifa 9:



# a = int(input("Son kiriting: "))
# b = 0
# x = [-2,31,104,51,19,7]
# n = 0



# while n < len(x):
#     if a == x[n]:
#         b = 1
#     n += 1
# if b == 1:
#     print("Bu son bor listda!")
# else:
#     print("Bu son yoq listda")
    

# vazifa 10



# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))

# while B != 0:
#     A, B = B, A % B

# print(f"{A} va {B} sonlarning EKUBi: {A}")



