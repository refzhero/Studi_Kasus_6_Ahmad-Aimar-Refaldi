import json

with open("inventaris.json", "r", encoding="utf-8") as f:
    data = json.load(f)


def tambah_data(nama, stok, harga):
    data.append({
        "nama": nama,
        "stok": stok,
        "harga": harga
    })

    return "Data ditambah"


def simpan_file():
    with open("inventaris.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return "Data tersimpan ke inventaris.json"


while True:
    print("===== SISTEM MANAJEMEN INVENTARIS =====")
    print("1. Tampilkan data")
    print("2. Tambah data")
    print("3. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        print("===== DATA INVENTARIS =====")
        print(data)

    elif pilihan == "2":
        nama = input("Nama barang: ")
        stok = input("Stok barang: ")
        harga = input("Harga barang: ")

        print(tambah_data(nama, stok, harga))
        print(simpan_file())

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")