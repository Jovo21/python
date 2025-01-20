# def nomer(n):
#     company = {
#         '90': "Beeline",
#         '91': 'Beeline',
#         '94': 'Ucell',
#         '93': 'Ucell',
#         '95': 'Uzmobile',
#         '99': 'Uzmobile',
#         '97': 'Mobiuz'
#     }
#     company_code = n[4:7]
#     if n[0:4]== '+998' and len(n)==13:
#         return company[company_code]
#     else:
#         return 'Bu kompaniya mavjud emas'


# phone_number = input('Phone number: ')
# print(nomer(phone_number))









# def viloyat_aniqlash(raqam):
#     viloyatlar = {
#     "01": "Toshkent shahar",
#     "10": "Toshkent viloyati",
#     "60": "Andijon",
#     "80": "Buxoro",
#     "25": "Jizzax",
#     "70": "Qashqadaryo",
#     "85": "Navoi",
#     "50": "Namangan",
#     "30": "Samarqand",
#     "75": "Surxondaryo",
#     "40": "Fargona",
#     "90": "Xorazm",
#     "20": "Sirdaryo",
#     "95": "Qoraqalpogiston"
# }
#     viloyat_kod = raqam[:2]

#     return viloyatlar.get(viloyat_kod, 'Xech qanday viloyatga tegishli emas')
    

# raqam = input("Mashina raqamini kiriting: ")


# viloyat = viloyat_aniqlash(raqam)
# print(f" {viloyat}.")







# import time

# def loading():
#     while True:
#         for i in range(3):
#             print("loading" + "." * (i + 1), end="\r")
#             time.sleep(0.5)
#         print("loading...", end="\r")


# loading()









def vaqt():
    k = 86400
    for i in range(k, 0, -1):
        soat = 86400 // 3600
        minut = 86400 % 3600 // 60
        sec = 86400 % 60
        print(f"{soat:02}:{minut:02}:{sec:02}")
        time.sleep(0.5)
        k -= 1

vaqt()
