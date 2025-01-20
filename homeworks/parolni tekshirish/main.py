def parolni_tekshirish(parol):

    uzunlik = False
    raqam = False
    katta_harf = False
    kichik_harf = False
    unikal_belgi = False

    if len(parol) >= 8:
        uzunlik = True

    for belgi in parol:
        if belgi.isdigit():
            raqam  = True
        if belgi.isupper():
            katta_harf = True
        if belgi.islower():
            kichik_harf = True
        if ord(belgi) >= 32 and ord(belgi) <= 47 or ord(belgi) >= 58 and ord(belgi) <= 64 or ord(belgi) >= 91 and ord(belgi) <= 96:
            unikal_belgi = True 


    if uzunlik == False:
        return "Parol kamida 8 ta belgidan iborat bo'lishi kerak."
    if raqam == False:
        return "Parolda kamida 1 ta raqam bo'lishi kerak."
    if katta_harf == False:
        return "Parolda kamida 1 ta katta harf bo'lishi kerak."
    if kichik_harf == False:
        return "Parolda kamida 1 ta kichik harf bo'lishi kerak."
    if unikal_belgi == False:
        return "Parolda kamida 1 ta unikal belgi bo'lishi kerak."

    return "Parol qabul qilindi!"


parol = input("Parolni kiriting: ")
natija = parolni_tekshirish(parol)
print(natija)