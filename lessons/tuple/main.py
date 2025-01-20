son = int(input("uch xonali son kiriting: "))

yuzlik = son // 100
onlik = (son // 10) % 10
birlik = son % 10

summa = yuzlik + onlik + birlik

check = summa == onlik or summa == birlik or summa == yuzlik

print(check)