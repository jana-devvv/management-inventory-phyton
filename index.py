# Struktur data untuk menyimpan data item

# Kelas Item ini akan menyimpan data dasar setiap item seperti ID, nama, jumlah dan harga

class Item :
    def __init__(self, id_item, name, quantity, price):
        # Menyimpan ID item
        self.id = id_item
        # Menyimpan nama item
        self.name = name
        # Menyimpan jumlah item
        self.quantity = quantity
        # Menyimpan harga item
        self.price = price

# Daftar (list) untuk menyimpan semua item yang ada dalam inventaris
inventory = []

# Fungsi untuk menambah item baru ke dalam inventaris
def add_item(id, name, quantity, price):
    # Membuat objek item baru dari kelas item
    item = Item(id, name, quantity, price)
    # Menambahkam objek item ke dalam daftar inventaris
    inventory.append(item)
    # Memberikan pesan bahwa item berhasil ditambahkan
    print(f"Item '{name}' berhasil ditambahkan.")

# Fungsi untuk menampilkan semua item dalam inventaris
def show_inventory():
    # Memberi tahu pengguna bahwa ini adalah daftar inventaris
    print("Daftar Inventaris: ")
    # Perulangan untuk menampilkan setiap item dalam inventaris
    for item in inventory:
        # Menampilkan ID, Nama, Jumlah dan Harga dari masing-masing item
        print(f"ID: {item.id}, Nama {item.name}, Jumlah: {item.quantity}, Harga: {item.price}")

# Fungsi untuk mengedit data item dalam inventaris berdasarkan ID
def edit_item(id, new_quantity=None, new_price=None):
    # Perulangan untuk mencari item berdasarkan ID
    for item in inventory:
        # Jika ID item ditemukan
        if item.id == id:
            # Jika ada jumlah baru yang diinput, perbarui jumlah item
            if new_quantity is not None:
                item.quantity = new_quantity
            # Jika ada harga baru yang diinput, perbarui harga item
            if new_price is not None:
                item.price = new_price
            # Memberikan pesan bahwa item berhasil diperbarui
            print(f"Item '{item.name}' berhasil diperbarui.")
            return # Keluar dari fungsi setelah item diperbarui
    # Jika Id item tidak ditemukan, berikan pesan
    print("Item tidak ditemukan.")

# Fungsi untuk menghapus item dari inventaris berdasarkan ID
def delete_item(id):
    global inventory # menggunakan variabel inventaris dari luar fungsi
    # Menghapus item dari daftar inventaris dengan filter ID yang berbeda
    inventory = [item for item in inventory if item.id != id]
    # Memberikan pesan bahwa item berhasil dihapus
    print(f"Item dengan ID {id} berhasil dihapus.")

# Fungsi untuk memeriksa item yang stoknya rendah (di bawah ambang batas)
def check_low_stock(threshold=5):
    # Memberi tahu pengguna bahwa ini adalah daftar item dengan stok rendah
    print("Item dengan stok rendah: ")
    # Perulangan untuk memeriksa jumlah stok setiap item
    for item in inventory:
        # Jika jumlah stok item kurang dari ambang batas
        if item.quantity < threshold:
            # Tampilkan nama dan jumlah item yang stoknya rendah
            print(f"{item.name} (Stok: {item.quantity})")

def menu():
    # Perulangan terus-menerus agar menu selalu tampil sampai pengguna keluar
    while True:
        # Menampilkan opsi menu untuk pengguna dalam bentuk tabel
        print("\n+------------------------------------------+")
        print("|        SISTEM MANAGEMENT INVENTORY       |")
        print("+----+-------------------------------------+")
        print("| NO |               Opsi Menu             |")
        print("+----+-------------------------------------+")
        print("| 1  | Add Item                            |")
        print("| 2  | Show Inventory                      |")
        print("| 3  | Edit Item                           |")
        print("| 4  | Delete Item                         |")
        print("| 5  | Check Low Stock                     |")
        print("| 6  | Exit                                |")
        print("+----+-------------------------------------+")

        # Meminta input dari pengguna untuk memilih menu
        opsi = input("Pilih menu: ")

        # Proses untuk masing-masing pilihan menu bisa ditambahkan di sini

        # Jika pilihan adalah 1, tambah item baru
        if opsi == "1":
            # Meminta input dari pengguna untuk data item baru
            id = input("ID Item: ")
            name = input("Nama Item: ")
            quantity = int(input("Jumlah: "))
            price = float(input("Harga: "))
            # Memanggil fungsi add_item untuk menambah item ke inventory
            add_item(id, name, quantity, price)
        # Jika pilihan adalah 2, tampilkan semua item ke inventory
        elif opsi == "2":
            # Meminta fungsi show_inventory untuk melihat daftar item
            show_inventory()
        # Jika pilihan adalah 3, edit item yang sudah ada
        elif opsi == "3":
            # Meminta input dari pengguna untuk ID item yang ingin diedit
            id = input("ID Item yang ingin diedit: ")
            # Meminta input jumlah baru atau biarkan kosong jika tidak ada perubahan
            new_quantity = int(input("Jumlah baru (kosongkan jika tidak diubah): ") or -1)
            # Meminta input harga baru atau biarkan kosong jika tidak ada perubahan
            new_price = float(input("Harga baru (kosongkan jika tidak diubah): ") or -1)
            # Memanggil fungsi edit_item untuk memperbarui data item
            edit_item(id, None if new_quantity == -1 else new_quantity, None if new_price == -1 else new_price)
        # Jika pilihan adalah 4, hapus item dari inventory
        elif opsi == "4":
            # Meminta input dari pengguna untuk ID item yang ingin dihapus
            id = input("ID item yang ingin dihapus: ")
            # Memanggil fungsi delete_item untuk menghapus item dari inventory
            delete_item(id)
        # Jika pilihan adalah 5, periksa stok rendah
        elif opsi == "5":
            # Meminta input dari pengguna untuk ID item yang ingin dihapus
            threshold = int(input("Masukkan ambang batas stok rendah: "))
            # Memanggil fungsi delete_item untuk menghapus item dari inventory
            check_low_stock(threshold)
        # Jika pilihan adalah 6, keluar dari program
        elif opsi == "6":
            # Memberi pesan keluar dan mengakhiri perulangan
            print("Keluar dari sistem.")
            break
        # Jika pilihan tidak valid, berikan pesan kesalahan
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

# Memanggil fungsi menu untuk menjalankan program
menu()