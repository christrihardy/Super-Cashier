"""
Module yang berisi class & fungsi kasir untuk Super Cashier
Akan diimport ke module simple_UI.py
"""

from tabulate import tabulate


class Transaction:

    def __init__(self):
        """Inisialisasi dictionary keranjang belanja"""

        # Keranjang belanja untuk menampung item,jumlah, harga dan harga total
        self.dict_belanja = {}

        # Counter untuk menghitung total harga belanjaan
        self.total_belanja = 0

    def add_item(self):
        """
        Method untuk memasukkan barang yang ingin dibeli

        Input: 
        - Nama Item
        - Jumlah Item
        - Harga Item
        """
        print("---Tambah Item---")

        nama_item = input("Nama Item: ")

        # Jika input berupa blank input atau bukan angka, nilai input = 0
        try:
            jumlah_item = input("Jumlah Item: ")
            harga_item = input("Harga Item: ")

            jumlah_item = int(jumlah_item)
            harga_item = int(harga_item)

        except:
            jumlah_item = 0
            harga_item = 0

        # Jika nama item sama, tambah jumlah lama dengan jumlah baru
        if nama_item in self.dict_belanja.keys():
            print("Nama barang sama, jumlah akan ditambahkan")

            jumlah_baru = self.dict_belanja[nama_item][0] + jumlah_item
            harga_total = jumlah_baru * self.dict_belanja[nama_item][1]

            # Update jumlah baru & harga total baru di keranjang
            # Harga tidak di-update karena item yg sama
            self.dict_belanja[nama_item][0] = jumlah_baru
            self.dict_belanja[nama_item][2] = harga_total

        # Jika nama item unik/tidak ada di keranjang, tambah sebagai item baru
        else:
            harga_total = jumlah_item*harga_item
            self.dict_belanja[nama_item] = [
                jumlah_item, harga_item, harga_total]

        print(f"Anda menambahkan item '{nama_item}' sejumlah: {jumlah_item}")

        while True:
            another = input("Tambah item lain? (yes/no): ")
            if another.lower() == 'yes':
                self.add_item()
            elif another.lower() == 'no':
                break
            else:
                print("Mohon input 'yes' atau 'no'")
                continue

            return

        print(".............................................")

    def check_list(self, nama):
        """
        Method untuk mengecek apakah nama barang ada di keranjang belanja

        Akan dipanggil di method utama lainya untuk cek input
        """
        if nama in self.dict_belanja.keys():
            pass
        else:
            raise KeyError(
                "Item tidak ditemukan, mohon input nama item dengan benar")

    def update_item_name(self):
        """
        Method untuk update nama barang

        Input:
        - Nama item yg ingin diubah
        - Nama item baru

        """
        print("---Ubah Nama Item---")
        if len(self.dict_belanja) == 0:
            print("Keranjang masih kosong, kembali ke menu")
            return

        # User input akan di-loop sampai nama barang benar (ada di keranjang)
        while True:
            try:
                nama_item = input("Nama item yang ingin diubah: ")
                self.check_list(nama_item)
                break

            except Exception as e:
                print(e)

        update_nama = (input("Nama item baru: "))

        # Buat key baru untuk nama item baru dengan harga & jumlah yg sama
        # Lalu delete key nama item lama, karena key immutable
        self.dict_belanja[update_nama] = self.dict_belanja[nama_item]
        del self.dict_belanja[nama_item]

        print(
            f"Update nama berhasil, item '{nama_item}' diubah menjadi '{update_nama}'")
        print(".............................................")

    def update_item_qty(self):
        """"
        Method untuk update jumlah barang

        Input:
        - Nama item yg ingin diubah jumlahnya
        - Jumlah baru

        """
        print("---Ubah Jumlah Item---")
        if len(self.dict_belanja) == 0:
            print("Keranjang masih kosong, kembali ke menu")
            return

        # User input akan di-loop sampai nama barang benar
        while True:
            try:
                nama_item = input("Masukkan nama item: ")
                self.check_list(nama_item)
                break

            except Exception as e:
                print(e)

        # User input akan di-loop sampai input berupa angka
        while True:
            try:
                update_jumlah = int(input("Jumlah diubah menjadi: "))
                break

            except ValueError:
                print("Mohon masukkan angka")

        # update jumlah ke dict
        self.dict_belanja[nama_item][0] = update_jumlah

        # Update harga total per item karena jumlah item berubah
        harga_baru = update_jumlah * self.dict_belanja[nama_item][1]
        self.dict_belanja[nama_item][2] = harga_baru

        print(
            f"Update jumlah item '{nama_item}' berhasil, jumlah diubah menjadi: {update_jumlah}")
        print(".............................................")

    def update_item_price(self):
        """
        Method untuk update harga barang

        Input:
        - Nama item yang ingin diubah harganya
        - Harga baru
        """
        print("---Ubah Harga Item---")
        if len(self.dict_belanja) == 0:
            print("Keranjang masih kosong, kembali ke menu")
            return

        # User input akan di-loop sampai nama barang benar
        while True:
            try:
                nama_item = input("Masukkan nama item: ")
                self.check_list(nama_item)
                break

            except Exception as e:
                print(e)

        # User input akan di-loop sampai input berupa angka
        while True:
            try:
                update_harga = int(input("Harga diubah menjadi: "))
                break

            except ValueError:
                print("Mohon masukan angka")

        # update harga baru ke dict
        self.dict_belanja[nama_item][1] = update_harga

        # Update harga total per item karena harga item berubah
        harga_baru = update_harga * self.dict_belanja[nama_item][0]
        self.dict_belanja[nama_item][2] = harga_baru

        print(
            f"Update harga item '{nama_item}' berhasil, harga diubah menjadi {update_harga}")
        print(".............................................")

    def delete_item(self):
        """Method untuk menghapus suatu barang dari keranjang"""
        print("---Hapus Item---")
        if len(self.dict_belanja) == 0:
            print("Keranjang masih kosong, kembali ke menu")
            return

        # User input akan di-loop sampai nama barang benar
        while True:
            try:
                nama_item = input("Item yang ingin dihapus: ")
                self.check_list(nama_item)
                break

            except Exception as e:
                print(e)

        self.dict_belanja.pop(nama_item)

        print(f"Item '{nama_item}' berhasil dihapus")
        print(".............................................")

    def reset_transaction(self):
        """Method untuk menghapus/reset semua barang yang ada di keranjang"""

        self.dict_belanja.clear()
        print("Semua item di keranjang telah dihapus!")
        print(".............................................")

    def check_order(self):
        """
        Method untuk menampilkan barang yang ada di keranjang

        Output: 
        - Tabel dan 
        - Pesan 'pemesanan sudah benar atau salah'
        """

        # Menampilkan belanjaan dalam bentuk tabel
        print(tabulate([[k, ] + v for k, v in self.dict_belanja.items()],
              headers=["Nama", "Jumlah", "Harga", "Total"], tablefmt="github"))
        print(".............................................")

        # Cek jika ada harga/jumlah bernilai 0, negatif atau empty string
        if any(any(0 > minus for minus in val) or 0 in val for val in self.dict_belanja.values()):
            print("Ada kesalahan input harga atau jumlah, mohon cek order anda")
        elif "" in self.dict_belanja.keys():
            print("Ada kesalahan input nama barang, mohon cek order anda")
        # Cek jika keranjang belanja kosong
        elif len(self.dict_belanja) == 0:
            print("Tidak ada item di keranjang")
        else:
            print("Pemesanan sudah benar")

        print(".............................................")

    def total_price(self):
        """
        Method untuk menghitung total harga belanjaan & diskon yang didapat

        Output: 
        - Tabel belanjaan
        - Diskon (jika memenuhi syarat)
        - Jumlah yang harus dibayar
        """

        # Hitung total harga belanjaan
        for x in self.dict_belanja:
            self.total_belanja += self.dict_belanja[x][2]

        # Menampilkan belanjaan dalam bentuk tabel
        print(tabulate([[k, ] + v for k, v in self.dict_belanja.items()],
              headers=["Nama", "Jumlah", "Harga", "Total"], tablefmt="github"), "\n")

        print(f"Total belanja anda senilai: Rp. {self.total_belanja:,.0f}")

        # Menentukan diskon
        if self.total_belanja > 500_000:
            diskon = 0.1 * self.total_belanja
            self.total_belanja -= diskon
            print(f"Selamat! Anda mendapatkan diskon 10%")
        elif self.total_belanja > 300_000:
            diskon = 0.08 * self.total_belanja
            self.total_belanja -= diskon
            print(f"Selamat! Anda mendapatkan diskon 8%")
        elif self.total_belanja > 200_000:
            diskon = 0.05 * self.total_belanja
            self.total_belanja -= diskon
            print(f"Selamat! Anda mendapatkan diskon 5%")

        print(".............................................")
        print(f"Jumlah yang harus dibayar: Rp. {self.total_belanja:,.0f}")
        print(".............................................")
