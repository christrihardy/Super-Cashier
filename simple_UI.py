"""
Module berisi objek dari class Transaction dan fungsi daftar menu sederhana Super Cashier
Akan diimport ke file utama main.py
"""

import cashier

# Buat objek ID transaksi berdasarkan user input
dict_ID = {}

while True:
    try:
        transaction_ID = input("Buat ID transaksi: ")
        if not transaction_ID:
            raise ValueError
        break

    except:
        print('Mohon input ID transaksi')  # Loop jika input berupa kosong

print("ID transaksi anda:", transaction_ID)

# Simpan objek dari user input di dictionary, key sebagai nama instance
dict_ID[transaction_ID] = cashier.Transaction()

# Function untuk memanggil method dari instance object
def add_item():
    dict_ID[transaction_ID].add_item()
    menu()


def update_name():
    dict_ID[transaction_ID].update_item_name()
    menu()


def update_qty():
    dict_ID[transaction_ID].update_item_qty()
    menu()


def update_price():
    dict_ID[transaction_ID].update_item_price()
    menu()


def delete_item():
    dict_ID[transaction_ID].delete_item()
    menu()


def reset_transaction():
    dict_ID[transaction_ID].reset_transaction()
    menu()


def check_order():
    dict_ID[transaction_ID].check_order()
    menu()


def total_price():
    print("Transaction ID:", transaction_ID)
    dict_ID[transaction_ID].total_price()
    menu()


def leave():
    print("Terima kasih atas kunjunganya")

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
        leave()
        return  # stop code