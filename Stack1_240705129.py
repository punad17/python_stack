import os
from queue import LifoQueue
from collections import deque

print()
maxSize  = int(input('Masukkan Jumlah data yang ingin ditambah:'))

DequeStack = deque()
LifoStack = LifoQueue(maxsize=maxSize)

cek = True
while cek:
    os.system('cis')
    print('Masukkan Pilihan anda-')
    print(' 1. Stack dengan Deque')
    print(' 2. Stack dengan Lifoqueue')
    print(' 0. Keluar')

    pil =int(input('Masukkan Pilihan anda'))

    if pil ==1:
        os.system('csl')
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

            if pilMenu ==1:
                if len(DequeStack) <= maxSize:
                    while i <= maxSize:
                        item = input (f'Masukkan data ke {i}:')
                        DequeStack.append(item)
                        i+=1
                else:
                    print('Data tidak bisa ditambah. Stack sudah penuh!!')

            elif pilMenu == 2:
                if len(DequeStack) !=0:
                    print(f'Elemen terakhir:{DequeStack.pop()} data telah dihapus')
            else:
                print('Stack kosong. Tidak ada elemen untuk dihapus!!')
