class BankAccount:
    def __init__(self, no, saldo=0):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")
        self.no = no
        self.saldo = saldo

    def tampil(self):
        print(f"No Rekening : {self.no}")
        print(f"Saldo       : Rp. {self.saldo:,}".replace(",", "."))

try:
    udin = BankAccount("1234567890", 1000)
    print("udin berhasil dibuat")
    udin.tampil()
except ValueError as e:
    print("Error pada udin:", e)

print("-" * 30)

try:
    josjis = BankAccount("1357924680", -1000)
    print("josjis berhasil dibuat")
    josjis.tampil()
except ValueError as e:
    print("Error pada josjis:", e)