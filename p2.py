class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim


mhs = Mahasiswa("udin josjis", "14015161718")
print(mhs.nama)
print(mhs.nim)