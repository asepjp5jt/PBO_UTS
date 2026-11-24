class Alfamart:
    pass
class Kasir:
    pass

Alfamart1 = Alfamart()
Alfamart2 = Alfamart()
print(type(Alfamart1))
print(type(Alfamart2))

kasir1 = Kasir()
kasir2 = Kasir()
print(type(kasir1))
print(type(kasir2))

alfamart1 = Alfamart()
alfamart1.id = 12345
alfamart1.nama = "alfamart cilegon"
print(alfamart1.id)
print(alfamart1.nama)

alfamart2 = Alfamart()
alfamart2.id = 67890
alfamart2.nama = "alfamart serang"
print(alfamart2.id)
print(alfamart2.nama)