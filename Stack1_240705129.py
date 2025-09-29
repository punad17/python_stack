import os
from queue import LifoQueue
from collections import deque

# Fungsi clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print()
maxSize  = int(input('Masukkan Jumlah data yang ingin ditambah: '))

DequeStack = deque()
LifoStack = LifoQueue(maxsize=maxSize)

cek = True
while cek:
    clear()
    print('Masukkan Pilihan anda-')
    print(' 1. Stack dengan Deque')
    print(' 2. Stack dengan Lifoqueue')
    print(' 0. Keluar')

    pilMenu = int(input('Masukkan Pilihan anda: '))

    if pilMenu == 1:
        clear()
        i = 1
        temp = True
        while temp:
            print()
            print('-Masukkan Pilihan anda-')
            print('1. Tambah Data dengan Deque')
            print('2. Hapus Data Deque')
            print('3. Tampil Data Deque')
            print('4. Jumlah Data Deque')
            print('0. Keluar')

            pilihan = int(input('Masukkan pilihan anda: '))

            if pilihan == 1:
                if len(DequeStack) < maxSize:
                    while i <= maxSize:
                        item = input(f'Masukkan data ke-{i}: ')
                        DequeStack.append(item)
                        i += 1
                else:
                    print('Data tidak bisa ditambah. Stack sudah penuh!!')

            elif pilihan == 2:
                if len(DequeStack) != 0:
                    print(f'Elemen terakhir: {DequeStack.pop()} telah dihapus')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')

            elif pilihan == 3:
                print('Data dalam stack adalah:')
                print(DequeStack)

            elif pilihan == 4:
                print(f'Jumlah Data dalam Stack = {len(DequeStack)}')

            else:
                temp = False
                break 

    elif pilMenu == 2:
        clear()
        temp = True
        while temp:
            print()
            print('Masukkan Pilihan Anda')
            print(' 1. Tambah Data dengan LifoQueue')
            print(' 2. Hapus Data LifoQueue')
            print(' 3. Tampil Data LifoQueue')
            print(' 4. Jumlah Data LifoQueue')
            print(' 0. Keluar')

            pilihan = int(input('Masukkan pilihan anda: '))

            if pilihan == 1:
                if LifoStack.full() == False:
                    i = LifoStack.qsize() + 1
                    while i <= maxSize:
                        item = input(f'Masukkan data ke-{i}: ')
                        LifoStack.put(item)
                        i += 1
                else:
                    print('Data tidak bisa ditambah. Stack sudah penuh!.')
            elif pilihan == 2:
                if not LifoStack.empty():
                    print(f'Elemen terakhir: {LifoStack.get()} telah dihapus')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')
            elif pilihan == 3:
                isi = list(LifoStack.queue)
                print('Data dalam Stack adalah:')
                print(isi)
            elif pilihan == 4:
                print(f'Jumlah Data dalam Stack = {LifoStack.qsize()}')
            else:
                temp = False
                break
    elif pilMenu == 0:
        cek = False
        break
    else:
        print('Pilihan tidak ada')
