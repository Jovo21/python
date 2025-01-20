a = input('Keyni kiriting: ')


person = {
    'name': 'Ali',
    'age': 21,
    'city': 'Tashkent',
    'address': 'Sergeli',
    'isStudent': True,
}


k = person.get(a,f"not key: {a}")

print(k)