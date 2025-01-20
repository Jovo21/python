A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))

toq = 0
juft = 0

for i in range(A,B+1,1):
    if i % 2 == 0:
        juft += 1
    else:
        toq += 1
print(f"Toq sonlar {toq} ta")
print(f"Juft sonlar {juft} ta")