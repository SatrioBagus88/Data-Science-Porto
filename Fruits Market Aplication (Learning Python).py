from tabulate import tabulate



SelamatDatang= ('Selamat Datang Di Pasar Buah')
TampilkanMenu = ('List menu \n 1. Menampilkan Data Buah \n 2. Menambahkan Buah \n 3. Menghapus Buah \n 4. Membeli Buah \n 5. Exit Program')


data = [['Index', 'Nama', 'Stock', 'Harga'], ['Apel', 20, 10000], ['Jeruk', 15, 15000], ['Anggur', 25, 20000]]
    
dataset_buah = {"Apel", "Jeruk", "Anggur"}
datasetan = set()
HargaSemua = 0
keranjang_belanja = [['Index', 'Nama', 'Stock', 'Harga']]
strukbelanja = [["Nomor", "Nama Buah", "Total Pembelian", "Total Harga"]]

print()
print(SelamatDatang)
print(TampilkanMenu)
print()
PilihMenu = int(input('masukkan angka menu yang ingin dijalankan: '))
while True:
    if PilihMenu == 1:
        print()
        print ("Daftar Buah")
        print(tabulate(data, headers =  "firstrow", showindex = "always"))
        print()
        print(TampilkanMenu)
        PilihMenu = int(input(f'masukkan angka menu yang ingin dijalankan: '))
    if PilihMenu == 2:
        print()
        Tambahanbuah = input("masukan nama buah yang ingin ditambahkan: ").title()
        if Tambahanbuah in dataset_buah:
            TambahanStock = int(input("masukan jumlah stok yang ingin ditambahkan (dalam angka): "))
            for x,y in enumerate (data):
                if x > 0:
                    if y[0] == Tambahanbuah:
                        y[1] = y[1] + TambahanStock
                        print ("Stock Berhasil Ditambahkan")
            print()
            print(TampilkanMenu)
            PilihMenu = int(input('masukkan angka menu yang ingin dijalankan: '))
        elif Tambahanbuah not in dataset_buah:
            dataset_buah.add(Tambahanbuah)
            TambahanStock = int(input("masukan jumlah stok yang ingin ditambahkan (dalam angka): "))
            # if type(TambahanStock) != int:
            #     print("format penambahan salah, silahkan ulangi")
            #     TambahanStock = int(input("masukan jumlah stok yang ingin ditambahkan (dalam angka): "))
            input_harga_buah = int(input('masukkan harga buah yang ingin ditambahkan: '))
            tambah_buah = [Tambahanbuah, TambahanStock, input_harga_buah]
            data.append(tambah_buah)
            print()
            print ("Buah berhasil ditambahkan")
            print(TampilkanMenu)
            PilihMenu = int(input('masukkan angka menu yang ingin dijalankan: '))
    if PilihMenu == 3:
        print()
        print ("Daftar Buah")
        print(tabulate(data, headers =  "firstrow", showindex = "always"))
        index = int(input("Masukkan index buah yang ingin dihapus(dalam angka): "))
        i= index + 1
        while not (0<i and (i<(len(data)))):
            print("angka tidak sesuai")
            break
        if 0<i and (i<(len(data))):
            data.pop(i)
            print ("Buah berhasil dihapus")
            for sat, rio in enumerate (data):
                if sat > 0:
                    datasetan.update({rio[0]})
                    dataset_buah = datasetan
                    
            print()
            print(TampilkanMenu)
            PilihMenu = int(input('masukkan angka menu yang ingin dijalankan: '))
    if PilihMenu == 4:
        while True:
            print()
            print ("Daftar Buah")
            print(tabulate(data, headers =  "firstrow", showindex = "always"))
            print()
            beli_buah = int(input("masukan index buah yang ingin dibeli (dalam angka): "))
            duar = beli_buah + 1
            while not (0<duar and (duar<(len(data)))):
                print("angka tidak sesuai")
                break
            while 0<duar and (duar<(len(data))):
                Beli_berapa=int(input("masukan jumlah yang ingin dibeli (dalam angka): "))
                if not (Beli_berapa <= data[duar][1]):
                    print ("Stok tidak tersedia")
                while Beli_berapa <= data[duar][1]:
                    KEREN= Beli_berapa*data[duar][2]
                    print (f"Total Harga: {KEREN}")
                    for x,y in enumerate (data):
                        if x > 0:
                            if y[0] in (data[duar][0]):
                                y[1] = y[1] - Beli_berapa
                                break
                    struksementara = [data[duar][0], Beli_berapa, KEREN]
                    strukbelanja.append(struksementara)
                    print()
                    print("daftar belanja sementara: ")
                    print (tabulate(strukbelanja, headers =  "firstrow", showindex = "always"))
                    break
                print ("Menu keranjang:\n 1. Tambah barang belanja\n 2. Bayar belanja ")
                menukasir = int(input("masukan pilihan menu keranjang (dalam angka): "))
                if menukasir == 1:
                    print()
                    print ("Daftar Buah")
                    print(tabulate(data, headers =  "firstrow", showindex = "always"))
                    beli_buah = int(input("masukan index buah yang ingin dibeli (dalam angka): "))
                    duar = beli_buah + 1
                if menukasir == 2:
                    print (tabulate(strukbelanja, headers =  "firstrow", showindex = "always"))
                    # print (strukbelanja)
                    for A,B in enumerate (strukbelanja):
                        if A>0:
                            HargaSemua += B[2]
                    print (f"Harga total adalah {HargaSemua}")
                    uang= int(input("Masukan jumlah uang: "))
                    while uang < HargaSemua:
                        print (f"transaksi dibatalkan,uang kurang {HargaSemua-uang}")
                        uang= int(input("Masukan jumlah uang: "))
                    if uang == HargaSemua:
                        print ("Transaksi Berhasil")
                        break
                    if uang > HargaSemua:
                        print(f'uang kembalian anda {uang-HargaSemua}')
                        break
            strukbelanja.clear()
            strukbelanja = [["Nomor", "Nama Buah", "Total Pembelian", "Total Harga"]]
            print("Terima kasih sudah berbelanja")
            print()
            print(TampilkanMenu)
            PilihMenu = int(input('masukkan angka menu yang ingin dijalankan: '))
    if PilihMenu == 5:
        print ("Program Tertutup")
        break
