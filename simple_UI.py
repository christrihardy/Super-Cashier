"""
Module berisi objek dari class Transaction dan fungsi daftar menu sederhana Super Cashier
Akan diimport ke file utama main.py
"""

import cashier

# User input untuk membuat
transaksi_1 = cashier.Transaction()

# Function untuk memanggil method dari objek


def add_item():
    transaksi_1.add_item()
    menu()


def update_name():
    transaksi_1.update_item_name()
    menu()


def update_qty():
    transaksi_1.update_item_qty()
    menu()


def update_price():
    transaksi_1.update_item_price()
    menu()


def delete_item():
    transaksi_1.delete_item()
    menu()


def reset_transaction():
    transaksi_1.reset_transaction()
    menu()


def check_order():
    transaksi_1.check_order()
    menu()


def total_price():
    transaksi_1.total_price()
    menu()

# UI sederhana


def menu():
    """
    Daftar fitur Super Cashier
    Input angka sesuai daftar yg ada untuk menjalankan fitur
    """
    print("""---Super Cashier---
    1. Add Item
    2. Update Item Name
    3. Update Item Quantity
    4. Update Item Price
    5. Delete Item
    6. Reset Transaction
    7. Check Order
    8. Total Price
    9. Exit
    """)

    # Input akan diulang sampai berupa angka
    while True:
        try:
            fitur = int(input("Pilih fitur: "))
            break
        except ValueError:
            print("Input harus angka, masukkan nomor fitur")

    # Memanggil fitur sesuai nomor
    if fitur == 1:
        add_item()
    elif fitur == 2:
        update_name()
    elif fitur == 3:
        update_qty()
    elif fitur == 4:
        update_price()
    elif fitur == 5:
        delete_item()
    elif fitur == 6:
        reset_transaction()
    elif fitur == 7:
        check_order()
    elif fitur == 8:
        total_price()
    elif fitur == 9:
        print("Terima kasih")
        exit()  # Exit program


# Jalankan menu() saat module ini diimport di main.py
menu()
