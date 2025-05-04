from abc import ABC, abstractmethod

# Abstract class dasar untuk semua item perpustakaan
class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self._item_id = item_id
        self._title = title
        self._available = True

    @abstractmethod
    def display_info(self):
        pass

    @property
    def title(self):
        return self._title

    def get_id(self):
        return self._item_id

    def is_available(self):
        return self._available

    def borrow(self):
        if self._available:
            self._available = False
            return True
        return False

    def return_item(self):
        self._available = True

# Subclass Book
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.__author = author

    def display_info(self):
        status = "Available" if self._available else "Borrowed"
        print(f"[BOOK] ID: {self._item_id}, Title: {self._title}, Author: {self.__author}, Status: {status}")

# Subclass Magazine
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue):
        super().__init__(item_id, title)
        self.__issue = issue

    def display_info(self):
        status = "Available" if self._available else "Borrowed"
        print(f"[MAGAZINE] ID: {self._item_id}, Title: {self._title}, Issue: {self.__issue}, Status: {status}")

# Class Library untuk manajemen koleksi
class Library:
    def __init__(self):
        self._items = []

    def add_item(self, item: LibraryItem):
        self._items.append(item)

    def display_all_items(self):
        if not self._items:
            print("Tidak ada item di perpustakaan.")
        else:
            for item in self._items:
                item.display_info()

    def search_by_title(self, title):
        found = [item for item in self._items if item.title.lower() == title.lower()]
        if found:
            for item in found:
                item.display_info()
        else:
            print("Item tidak ditemukan berdasarkan judul.")

    def search_by_id(self, item_id):
        for item in self._items:
            if item.get_id() == item_id:
                item.display_info()
                return
        print("Item tidak ditemukan berdasarkan ID.")

# Fungsi menu CLI
def main():
    library = Library()

    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tambah Majalah")
        print("3. Tampilkan Semua Item")
        print("4. Cari Item berdasarkan Judul")
        print("5. Cari Item berdasarkan ID")
        print("6. Keluar")
        choice = input("Pilih menu (1-6): ")

        if choice == '1':
            item_id = input("Masukkan ID Buku: ")
            title = input("Masukkan Judul Buku: ")
            author = input("Masukkan Nama Pengarang: ")
            book = Book(item_id, title, author)
            library.add_item(book)
            print("Buku berhasil ditambahkan.")
        elif choice == '2':
            item_id = input("Masukkan ID Majalah: ")
            title = input("Masukkan Judul Majalah: ")
            issue = input("Masukkan Edisi Majalah: ")
            magazine = Magazine(item_id, title, issue)
            library.add_item(magazine)
            print("Majalah berhasil ditambahkan.")
        elif choice == '3':
            print("\n== Daftar Semua Item ==")
            library.display_all_items()
        elif choice == '4':
            title = input("Masukkan Judul yang dicari: ")
            library.search_by_title(title)
        elif choice == '5':
            item_id = input("Masukkan ID yang dicari: ")
            library.search_by_id(item_id)
        elif choice == '6':
            print("Terima kasih! Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
