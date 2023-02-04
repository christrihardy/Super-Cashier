# Super-Cashier


## Latar Belakang
Super Cashier adalah program kasir sederhana berbasis bahasa pemrograman Python. 
Program ini dapat menjalankan fungsi dasar mesin kasir sehingga pengguna dapat melakukan proses belanja secara self-service

## Tools
Languages: 
- Python

Libraries:
- Tabulate

## Objectives
Tujuan Pembelajaran:
- Membuat program kasir sederhana dengan prinsip OOP
- Menerapkan konsep error catching dengan 'try-except'
- Menerapkan metode modular code 
- Menerapkan penulisan code yang bersih(clean code) dengan acuan PEP8

Program Objectives:
Membuat program kasir sederhana yang mempunyai fungsi:
- Menambahkan barang ke keranjang belanja virtual
- Mengubah nama,jumlah, atau harga barang yang telah dibeli
- Menghapus satu atau semua barang di keranjang
- Menampilkan daftar barang yang ada di keranjang
- Menghitung harga total belanja akhir dan cek diskon berdasarkan total belanja 
- UI sederhana untuk menjalankan fungsi-fungsi diatas dengan user input

## Flowchart:
![FLOWCHART KASIR](https://user-images.githubusercontent.com/122888994/216419676-545da74c-c9f1-4ba1-aa25-ba4289d85c0e.png)

1. User membuat objek ID transaksi
2. User menambahkan item dengan memasukkan nama, jumlah dan harga item yg ingin dibeli
    - Input 'yes' jika masih ingin menambahkan item lagi
3. Jika user mau mengecek/melihat daftar belanjaan, user bisa melakukan check order
    -Menampilkan daftar belanjaan dalam bentuk tabel
    -Notifikasi bila ada input yang tidak benar
5. Jika ada kesalahan input, user dapat mengupdate nama/harga/jumlah item yang salah
6. Jika batal membeli item, user dapat menghapus item:
    - Hapus 1 item
    - Reset transaksi(hapus seluruh item)
 7. Jika sudah selesai berbelanja, user dapat melakukan checkout
    - Diskon jika total belanja memenuhi syarat

## Deskripsi Program
Files:
- Module 'cashier.py' berisi class Transaction yang memiliki berbagai method untuk fungsi kasir
- Module 'simple_UI.py' berisi daftar menu dan pembuatan objek ID transaksi
- File utama 'main.py' untuk menjalankan program Super Cashier

## Cara Penggunaan
1. Download/clone repository ini ke direktori lokal anda
2. Jalankan file **main.py**
3. Pilih fitur dari daftar menu untuk menjalankan fungsi kasir

## Program Functions
cashier.py 
1. **__init__()**

    Inisialisasi class Transaction(). 
    
    Memuat dict_belanja yang akan berfungsi sebagai 'keranjang belanja' dan counter untuk hitung total belanja
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L9-L18
    
2. **add_item()**

    Method untuk tambah item ke keranjang dict_belanja. 
    
    Menyimpan nama sebagai Key, dan harga/jumlah sebagai Values. Total per item (jumlah * harga) juga disimpan sebagai values
    
    Jika memasukkan lagi item yg sama, maka jumlah baru akan ditambahkan ke jumlah yang sudah ada di keranjang
    
    - Input: Nama Item, Jumlah, Harga
    
    - Output: Notifikasi penambahan item, input(yes/no) jika user ingin tambah item lagi 
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L20-L75
    
3. **check_list()**

    Cek apakah sebuah nama item ada di keranjang atau tidak, akan dipanggil di method lain. Akan raise Error Message jika nama item tidak ada di keranjang
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L77-L86
    
4. **update_item_name()**

    Method untuk mengubah nama item
    
    Memanggil check_list() untuk cek apakah input nama item yg ingin diubah ada di keranjang, input akan di loop sampai nama item benar
    
    Jika keranjang masih kosong: exit input dan kembali ke menu
    
    - Input: Nama Item yang ingin diubah, Nama Item Baru
    
    - Output: Notifikasi perubahan nama item
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L88-L121
    
    
5. **update_item_qty()**
    
    Method untuk mengubah jumlah item
    
    Memanggil check_list() untuk cek apakah input nama item yg ingin diubah jumlahnya ada di keranjang, input akan di loop sampai nama item benar.Jika keranjang masih kosong: exit input dan kembali ke menu
    
    - Input: Nama Item yang ingin diubah jumlahnya, Jumlah Item Baru
    
    - Output: Notifikasi perubahan jumlah item
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L123-L165
    
6. **update_item_price()**

     Method untuk mengubah harga item

     Memanggil check_list() untuk cek apakah input nama item yg ingin diubah jumlahnya ada di keranjang, input akan di loop sampai nama item benar. Jika keranjang          masih kosong: exit input dan kembali ke menu

     - Input: Nama Item yang ingin diubah harganya, Harga Item Baru

     - Output: Notifikasi perubahan harga item
     https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L167-L208
 
7. **delete_item()**

   Method untuk menghapus sebuah item dari keranjang
    - Input: Nama Item yang ingin dihapus
    - Output: Notifikasi penghapusan item
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L210-L230
    
8. **reset_transaction()**

    Method untuk menghapus semua item atau reset transaksi
    - Output: Notifikasi semua item berhasil dihapus
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L232-L237
    
9. **check_order()**

    Method untuk cek daftar belanjaan/item apa saja yang ada di keranjang.
    
    Isi keranjang ditampilkan dalam bentuk tabel dan akan di cek jika ada input yang salah(blank input, nilai 0 atau angka negatif)
    - Output:  - Tabel belanjaan
               - Notifikasi pemesanan sudah benar, keranjang masih 0 atau ada kesalahan input
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L239-L264
    
10. **total_price()**

    Method untuk menghitung total belanja customer
    
    Daftar belanja akan ditampilkan dalam bentuk tabel dan dihitung totalnya. Method ini juga akan cek jika customer berhak mendapatkan diskon berdasarkan total belanjanya. Jika mendapatkan diskon, akan ditampilkan jumlah diskon yang didapat
    - Output: 
        - ID transaksi
        - Tabel belanjaan
        - Diskon (jika ada)
        - Total yang harus dibayar
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/cashier.py#L266-L302

simple_UI.py

1. **Input ID Transaksi**
   
   User input untuk membuat ID transaksi. Hasil input akan menjadi instance object dari class Transaction() dan akan disimpan sebagai keys di dict_ID untuk dipanggil methodnya di fungsi menu(). Akan mengeluarkan output berupa: print dari ID transaksi yg telah diinput
   
   Contoh:
   - Input '12345' akan membuat instance yg sama seperti mengetik code berikut: 12345 = Transaction() 
    
   https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/simple_UI.py#L8-L24
   
2. **menu()**

    Fungsi untuk menampilkan daftar menu sederhana sehingga user bisa melakukan user input untuk menjalankan fungsi program. Input berupa angka 1 sampai 9 dan akan memanggil fungsi sesuai apa yang ditampilkan di daftar menu.
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/simple_UI.py#L71-L116

3. **Caller Functions**
    
    Kumpulan fungsi untuk memanggil method dari instance ID transaksi yg telah dibuat user. Fungsi ini akan dipanggil di fungsi menu() untuk menjalankan method dari instance class Transaction() berdasarkan user input
    https://github.com/christrihardy/Super-Cashier/blob/1ef30b40a454f4b4dcf624f10cc7c40c4d707c88/simple_UI.py#L26-L69
    

## Test Case & Hasil
1.  Customer menambahkan 2 item:
    - Ayam Goreng, Jumlah: 2 pcs, Harga: 20000
    - Pasta Gigi, Jumlah: 3 pcs, Harga: 15000
    
    ![test case 1](https://user-images.githubusercontent.com/122888994/216420674-4d42f9d7-0bce-403f-9cdd-6876004eb924.png)

    
    ![test 1_3](https://user-images.githubusercontent.com/122888994/215345540-93b45ee2-d279-43c5-8acc-86ceff434ba6.png)


2.  Customer ingin menghapus item 'Pasta Gigi'
  
    ![test 2](https://user-images.githubusercontent.com/122888994/215345712-83f1e6f5-3762-43ee-981d-f787a456b350.png)
    
    ![test 2_2](https://user-images.githubusercontent.com/122888994/215345719-6083ca56-8d87-4f19-9162-92585e063b09.png)

3.  Customer ingin menghapus semua belanjaan
 
    ![test 3](https://user-images.githubusercontent.com/122888994/215345400-571442c3-61ac-440d-bb17-5c0e323e50ba.png)
    
    ![image](https://user-images.githubusercontent.com/122888994/215345820-ba535a6f-fc89-4390-86e5-a642107f7dd0.png)

4.  Customer selesai belanja dan ingin melihat total yang harus dibayar

    ![test 4](https://user-images.githubusercontent.com/122888994/215345419-7b16db4c-aa54-497b-813a-4dc7045067e2.png)

### Conclusion
Program kasir sederhana berbasis Python ini dapat melakukan fungsi kasir sederhana. Dengan adanya UI daftar menu dengan user input, customer dapat menjalankan fungsi kasir dari program ini dengan mudah dibanding harus mengetik method satu-satu

Future Work:
1. Menambahkan GUI agar penggunaan program lebih mudah dan intuitif
2. Menambahkan fitur kasir yang lebih kompleks, seperti penghitungan pembayaran
3. Memperbaiki alur program, misalnya: exit ke menu kalau terlanjur masuk input setelah pilih fitur
4. Revisi lain dari saran/kritik user yang telah mencoba program ini


