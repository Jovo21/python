# def raqammi(n):
#     if n >= '0' and n <= '9':
#         return True
#     return False

# x = input('Enter n: ')
# print(raqammi(x))



# def harftop(n):
#     k = 0
#     for i in matn:
#         if i == harf:
#             k += 1
#     return(k)

# matn = input("matnni kiriting: ")
# harf = input('Harfni kiriting: ')
# print(harftop(matn))






# def inlist(word):
#     word_list = []
#     word1 = ""

#     for i in word:
#         if i != " ":
#             word1 += i
#         else:
#             if word1:
#                 word_list.append(word1)
#                 word1 = ""


#     if word1:
#         word_list.append(word1)
#     return(word_list)


# print(inlist(input("enter text: ")))






# def summ(n):
#     newl = []
#     for i in l:
#         summa = 0
#         if i < 0:
#             i *= -1
#         while i > 0:
#             qoldiq = i % 10
#             summa += qoldiq
#             i = i // 10
#         newl.append(summa)
#     return newl

# l = [1, 34, -90, 45, 36, 120, 306]
# print(summ(l))






# def decToBIn(dec):
#     b = ""
#     while dec > 0:
#         b = str(dec % 2) + b
#         dec = dec // 2
#     return b


# a = int(input("Enter a num: "))
# print(decToBIn(a), "2sanoq")



# def info(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")


# info(age = 18, name = "Ali")