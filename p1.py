class mahasiswa:
    nim: 0
    nama: ""

    def perkenalan(self):
        print(f"hello nama saya {self.nama}")

    def hello(self, nama):
        print(f"hello {self.nama}, nama saya {nama}")
mahasiswa = mahasiswa()
mahasiswa.nama = "udin"
mahasiswa.perkenalan()
mahasiswa.hello("josjis")