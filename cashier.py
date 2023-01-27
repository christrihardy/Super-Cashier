
from tabulate import tabulate


class Transaction:
    """Class untuk membuat objek transaksi"""

    def __init__(self):

        # Keranjang belanja untuk menampung item,j umlah, harga dan harga total
        self.list_belanja = {}

        # Counter untuk menghitung total harga belanjaan
        self.total_belanja = 0
     
    def add_item(self, nama_item, jumlah_item, harga_item):
        """Method untuk memasukkan barang yang ingin dibeli"""

        # Hitung harga total per item
        harga_total = jumlah_item*harga_item
        self.list_belanja[nama_item]= [jumlah_item, harga_item, harga_total]

        print(f"Anda menambahkan item {nama_item} sejumlah: {jumlah_item}")
        print(".............................................")

    def check_list(self, nama):
        """
        Method untuk mengecek apakah nama barang ada di keranjang belanja
        Akan dipanggil di method utama lainya
        """
        if nama in self.list_belanja.keys():
            pass
        else:
            raise KeyError("Item tidak ditemukan, mohon input nama item dengan benar")
   
    def update_item_name(self):
        """
        Method untuk update nama barang
        """
        print("---Ubah Nama Item---")

        # User input akan di-loop sampai nama barang benar (ada di keranjang)
        while True:
            try:
                nama_item = input("Nama item yang ingin diubah: ") 
                self.check_list(nama_item) 
                break
   
            except Exception as e:
                print(e)
  
        update_nama = (input("Nama item baru: ")) 
      
        # Buat key baru untuk nama item baru dengan harga dan jumlah yg sama
        # Lalu delete key nama item lama, karena key immutable 
        self.list_belanja[update_nama]= self.list_belanja[nama_item]
        del self.list_belanja[nama_item]
        
        print(f"Update nama berhasil, item '{nama_item}' diubah menjadi '{update_nama}'")
        print(".............................................")

    
    def update_item_qty(self):
        """"Method untuk update jumlah barang"""
        print("---Ubah Jumlah Item---")

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

        self.list_belanja[nama_item][0]= update_jumlah #update jumlah baru ke 

        # Update harga total per item karena jumlah item berubah
        harga_baru = update_jumlah * self.list_belanja[nama_item][1]
        self.list_belanja[nama_item][2] = harga_baru
        
        print(f"Update jumlah item '{nama_item}' berhasil, jumlah diubah menjadi: {update_jumlah}")
        print(".............................................")
    
    def update_item_price(self):
        """Method untuk update harga barang"""
        print("---Ubah Harga Item---")

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

        self.list_belanja[nama_item][1]= update_harga # update harga baru ke dict

        # Update harga total per item karena harga item berubah
        harga_baru = update_harga * self.list_belanja[nama_item][0]
        self.list_belanja[nama_item][2] = harga_baru
        
        print(f"Update harga item '{nama_item}' berhasil, harga diubah menjadi {update_harga}")
        print(".............................................")
    
    def delete_item(self):
        """Method untuk menghapus suatu barang dari keranjang"""
        print("---Hapus Item---")

        # User input akan di-loop sampai nama barang benar
        while True:
            try:
                nama_item = input("Item yang ingin dihapus: ")
                self.check_list(nama_item)
                break
   
            except Exception as e:
                print(e)

        self.list_belanja.pop(nama_item)

        print(f"Item '{nama_item}' berhasil dihapus")
        print(".............................................")
        
    def reset_transaction(self):
        """Method untuk menghapus/reset semua barang yang ada di keranjang"""

        self.list_belanja.clear()
        print("Semua item di keranjang telah dihapus!")
        
    def check_order(self):
        """
        Method untuk menampilkan barang yang ada di keranjang

        Output: tabel dan pesan 'pemesanan sudah benar/salah'
        """

        # Menampilkan belanjaan dalam bentuk tabel
        print(tabulate([[k,] + v for k,v in self.list_belanja.items()], headers = ["Nama", "Jumlah", "Harga", "Total"], tablefmt ="github"))
        print(".............................................")

        # Branching untuk mengecek kesalahan input
        # Cek apakah ada harga/jumlah bernilai 0 atau nama berupa empty string
        if any(0 in val for val in self.list_belanja.values()): 
            print("Terjadi kesalahan input harga atau jumlah")
            
        elif "" in self.list_belanja.keys(): 
            print("Terjadi kesalahan input nama barang")
    
        else:
            print("Pemesanan sudah benar")

        print(".............................................")
        
    def total_price(self):
        """
        Method untuk menghitung total harga belanjaan & diskon yang didapat

        Output: tabel belanjaan, diskon(jika ada), dan jumlah yang harus dibayar
        """
        
        # Hitung total harga belanjaan
        for x in self.list_belanja:
            self.total_belanja += self.list_belanja[x][2]
        
        # Menampilkan belanjaan dalam bentuk tabel
        print(tabulate([[k,] + v for k,v in self.list_belanja.items()], headers = ["Nama", "Jumlah", "Harga", "Total"], tablefmt ="github"))
        
        print(f"Total belanja anda senilai: Rp. {self.total_belanja:,.0f}")
        
        # Branching untuk menentukan diskon yang didapat
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

