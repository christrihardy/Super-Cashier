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
- Menerapkan penulisan code yang bersih(clean code) dengan acuan PEP8

Program Objectives:
Membuat program kasir sederhana yang mempunyai fungsi:
- Menambahkan barang ke keranjang belanja virtual
- Mengubah nama,jumlah, atau harga barang yang telah dibeli
- Menghapus satu atau semua barang di keranjang
- Menampilkan daftar barang yang ada di keranjang
- Menghitung harga total belanja akhir dan cek diskon berdasarkan total belanja 
- UI sederhana untuk menjalankan fungsi-fungsi diatas dengan user input

Alur Program/Flowchart:
![FLOWCHART KASIR](https://user-images.githubusercontent.com/122888994/216411621-c7ac820b-4301-4571-a590-c14a71892c05.png)

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

Code Summary:
1. init()
2. add_item()
3. check_list()
4. update_item_name()
5. update_item_qty()
6. update_item_price()
7. delete_item()
8. reset_transaction()
9. check_order()
10. total_price()

## Cara Penggunaan
1. Download/clone repository ini ke direktori lokal anda
2. Jalankan file main.py
3. Pilih fitur dari daftar menu untuk menjalankan fungsi kasir

## Test Case & Hasil
1.  Customer menambahkan 2 item:
    - Ayam Goreng, Jumlah: 2 pcs, Harga: 20000
    - Pasta Gigi, Jumlah: 3 pcs, Harga: 15000
    
    ![test 1](https://user-images.githubusercontent.com/122888994/215345285-8edab589-e941-450f-a08e-96df3427eb72.png)
    
    ![test 1_2](https://user-images.githubusercontent.com/122888994/215345346-f5e61516-93cb-407b-9d88-90b5011908c0.png)
    
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

Future Work:
1. Menambahkan GUI agar penggunaan program lebih mudah dan intuitif
2. Menambahkan fitur kasir yang lebih kompleks, seperti penghitungan pembayaran


