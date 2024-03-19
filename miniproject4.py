class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class PeralatanRumahSakit:
    def __init__(self, id, nama, kategori, kualitas, kondisi, lokasi):
        self.id = id
        self.nama = nama
        self.kategori = kategori
        self.kualitas = kualitas
        self.kondisi = kondisi
        self.lokasi = lokasi

    def __str__(self):
        return f"ID: {self.id}, Nama: {self.nama}, Kategori: {self.kategori}, Kualitas: {self.kualitas}, Kondisi: {self.kondisi}, Lokasi: {self.lokasi}"


class IndexedPeralatanRumahSakit:
    def __init__(self, data, index):
        self.data = data
        self.index = index


class IndexedInventoryPeralatanRumahSakit:
    def __init__(self):
        self.head = None

    def tambah_peralatan_di_awal(self, peralatan, id_peralatan):
        new_node = Node(IndexedPeralatanRumahSakit(peralatan, id_peralatan))
        new_node.next = self.head
        self.head = new_node

    def tambah_peralatan_di_akhir(self, peralatan):
        new_node = Node(IndexedPeralatanRumahSakit(peralatan, None))
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def tambah_peralatan_di_tengah(self, peralatan, posisi):
        if posisi < 0:
            print("Posisi harus non-negatif.")
            return
        if posisi == 0:
            self.tambah_peralatan_di_awal(peralatan)
            return
        new_node = Node(IndexedPeralatanRumahSakit(peralatan, None))
        current = self.head
        prev = None
        count = 0
        while current and count < posisi:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Posisi terlalu tinggi.")
            return
        prev.next = new_node
        new_node.next = current

    def hapus_peralatan(self, posisi):
        if posisi < 0:
            print("Posisi harus non-negatif.")
            return
        if not self.head:
            print("Inventaris kosong.")
            return
        if posisi == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 0
        while current and count < posisi:
            prev = current
            current = current.next
            count += 1
        if not current:
            print("Posisi terlalu tinggi.")
            return
        prev.next = current.next

    def update_peralatan(self, nama_peralatan, kualitas, kondisi):
        current = self.head
        while current:
            if current.data.data.nama == nama_peralatan:
                current.data.data.kualitas = kualitas
                current.data.data.kondisi = kondisi
                return
            current = current.next
        print("Peralatan tidak ditemukan.")

    def tampilkan_peralatan(self):
        if not self.head:
            print("Inventaris kosong.")
            return
        print("Seluruh Peralatan Rumah Sakit:")
        current = self.head
        while current:
            peralatan = current.data.data  # Akses atribut dari objek PeralatanRumahSakit yang dibungkus
            print(f"ID: {peralatan.id}, Nama: {peralatan.nama}, Kategori: {peralatan.kategori}, Kualitas: {peralatan.kualitas}, Kondisi: {peralatan.kondisi}, Lokasi: {peralatan.lokasi}")
            current = current.next

    def sort_by_attribute(self, key, descending=False):
        # Split attributes string into a list
        attributes_list = key.split()

        # Ensure that all attributes are valid
        valid_attributes = ['nama', 'kategori', 'kualitas', 'kondisi', 'lokasi']
        for attr in attributes_list:
            if attr not in valid_attributes:
                print(f"Atribut '{attr}' tidak valid.")
                return

        # Sort the inventory based on the specified attributes
        temp = []
        current = self.head
        while current:
            temp.append(current.data)
            current = current.next

        # Sort the inventory using Merge Sort
        temp = self.merge_sort(temp, key, descending)

        # Update the linked list with the sorted items
        self.head = None
        for item in temp:
            self.tambah_peralatan_di_akhir(item.data)

    def merge_sort(self, items, key, descending=False):
        if len(items) <= 1:
            return items
        midpoint = len(items) // 2
        left_half = items[:midpoint]
        right_half = items[midpoint:]
        left_half = self.merge_sort(left_half, key, descending)
        right_half = self.merge_sort(right_half, key, descending)
        return self.merge(left_half, right_half, key, descending)

    def merge(self, left, right, key, descending):
        result = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if (not descending and getattr(left[left_index].data, key) <= getattr(right[right_index].data, key)) or \
                    (descending and getattr(left[left_index].data, key) >= getattr(right[right_index].data, key)):
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    def search_by_attribute(self, key, attribute):
        current = self.head
        index = 0
        while current:
            if getattr(current.data.data, attribute) == key:
                return index
            current = current.next
            index += 1
        return -1
    
    def search_by_id(self, id_peralatan):
        current = self.head
        index = 0
        while current:
            if current.data.data.id == id_peralatan:
                return index
            current = current.next
            index += 1
        return -1

    def search_by_name(self, nama_peralatan):
        current = self.head
        index = 0
        while current:
            if current.data.data.nama == nama_peralatan:
                return index
            current = current.next
            index += 1
        return -1

    def search_peralatan(self, key):
        index_by_id = self.search_by_id(key)
        if index_by_id != -1:
            return index_by_id
        else:
            index_by_name = self.search_by_name(key)
            return index_by_name


def input_peralatan():
    id_peralatan = input("Masukkan ID peralatan: ")
    nama = input("Masukkan nama peralatan: ")
    kategori = input("Masukkan kategori peralatan: ")
    kualitas = input("Masukkan kualitas peralatan: ")
    kondisi = input("Masukkan kondisi peralatan: ")
    lokasi = input("Masukkan lokasi peralatan: ")
    return PeralatanRumahSakit(id_peralatan, nama, kategori, kualitas, kondisi, lokasi)


inventory = IndexedInventoryPeralatanRumahSakit()

# Menambahkan beberapa peralatan
peralatan1 = PeralatanRumahSakit("01", "Stetoskop", "Alat Kesehatan", "Baik", "Baru", "Depan Ruangan")
peralatan2 = PeralatanRumahSakit("02", "Gunting Medis", "Alat Bedah", "Baik", "Baru", "Ruang Operasi")
peralatan3 = PeralatanRumahSakit("03", "Infus", "Alat Kesehatan", "Baik", "Baru", "Kamar Pasien")
inventory.tambah_peralatan_di_awal(peralatan1, peralatan1.id)
inventory.tambah_peralatan_di_awal(peralatan2, peralatan2.id)
inventory.tambah_peralatan_di_awal(peralatan3, peralatan3.id)

while True:
    print("\nPilihan Menu:")
    print("1. Tambah Peralatan di Awal")
    print("2. Tambah Peralatan di Akhir")
    print("3. Tambah Peralatan di Tengah")
    print("4. Hapus Peralatan")
    print("5. Update Peralatan")
    print("6. Tampilkan Peralatan")
    print("7. Sort Peralatan")
    print("8. Search Peralatan by Name or ID")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan menu: ")

    if pilihan == "1":
        peralatan = input_peralatan()
        inventory.tambah_peralatan_di_awal(peralatan)
    elif pilihan == "2":
        peralatan = input_peralatan()
        inventory.tambah_peralatan_di_akhir(peralatan)
    elif pilihan == "3":
        peralatan = input_peralatan()
        posisi = int(input("Masukkan posisi peralatan yang ingin ditambahkan: "))
        inventory.tambah_peralatan_di_tengah(peralatan, posisi)
    elif pilihan == "4":
        posisi = int(input("Masukkan posisi peralatan yang ingin dihapus: "))
        inventory.hapus_peralatan(posisi)
    elif pilihan == "5":
        nama_peralatan = input("Masukkan nama peralatan yang ingin diupdate: ")
        kualitas_baru = input("Masukkan kualitas baru peralatan: ")
        kondisi_baru = input("Masukkan kondisi baru peralatan: ")
        inventory.update_peralatan(nama_peralatan, kualitas_baru, kondisi_baru)
    elif pilihan == "6":
        inventory.tampilkan_peralatan()
    elif pilihan == "7":
        key = input("Masukkan atribut untuk sorting (nama, kategori, kualitas, kondisi, lokasi): ").lower()
        descending = input("Apakah Anda ingin mengurutkan secara descending? (y/n): ").lower() == "y"
        inventory.sort_by_attribute(key, descending)
        print("Peralatan telah diurutkan.")
    elif pilihan == "8":
        key = input("Masukkan nama atau ID peralatan yang ingin dicari: ")
        index = inventory.search_peralatan(key)
        if index != -1:
            print("Peralatan ditemukan:")
            current = inventory.head
            for _ in range(index):
                current = current.next
            print(current.data.data)
        else:
            print("Peralatan tidak ditemukan.")
    elif pilihan == "0":
        print("Terima kasih!")
        break
    else:
        print("Pilihan menu tidak valid. Silakan pilih lagi.")

