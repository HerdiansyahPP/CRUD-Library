ListBuku = [
    {
        'Judul Buku': 'Bumi Manusia',
        'Penulis': 'Pramoedya Toer', 
        'Tahun Terbit': 1980,
        'Stock': 5
    },
    {
        'Judul Buku': 'Rich Dad Poor Dad',
        'Penulis': 'Robert Kiyosaki',
        'Tahun Terbit': 2000, 
        'Stock': 5
    },
    {
        'Judul Buku': 'Laskar Pelangi',
        'Penulis': 'Andrea Hirata',
        'Tahun Terbit': 2005, 
        'Stock': 5
    },
    {
        'Judul Buku': 'Negeri 5 Menara',
        'Penulis': 'Ahmad Fuadi',
        'Tahun Terbit': 2009, 
        'Stock': 5
    },
    {
        'Judul Buku': 'Atomics Habits',
        'Penulis': 'James Clear',
        'Tahun Terbit': 2018,
        'Stock': 5
    }
]

# Fungsi Menampilkan Daftar Buku
def DaftarBuku():
    print('\nDaftar Buku\n')
    print('No\t| Judul Buku\t\t| Penulis \t\t| Tahun Terbit \t| Stock ')
    for index in range(len(ListBuku)):
        print(str(index+1) + '\t| ' + ListBuku[index]['Judul Buku'] + '   \t| ' + str(ListBuku[index]['Penulis']) + '    \t| ' + str(ListBuku [index]['Tahun Terbit']) + '    \t| ' + str(ListBuku [index]['Stock']))

# Fungsi Read
def Read():
    while (True):
        print('''
        Ini adalah Menu Read

        List SubMenu :
        1. Menampilkan seluruh daftar buku
        2. Menampilkan 1 buku
        3. Kembali ke Menu Utama
        ''')
        MenuRead= input('Masukkan angka menu read yang ingin dijalankan (1, 2, atau 3): ')
        if (MenuRead == '1'):
            if ListBuku == []:
                print('\nTidak ada data! Daftar buku KOSONG!') 
            else:
                DaftarBuku()
        elif (MenuRead == '2'):
            JudulRead = input('Masukkan Judul Buku yang ingin dicek : ').title() #.title() membuat huruf awal tiap kata jadi kapital. Handling Case Sensitive pada Judul atau nama Kolom
            ListBukuRead = []
            for i in range(len(ListBuku)):
                ListBukuRead.append(ListBuku[i]['Judul Buku'])
            if JudulRead not in ListBukuRead :
                print(f"Tidak ada data buku '{JudulRead}'!") 
            else:
                IndexRead = ListBukuRead.index(JudulRead)
                print('\nNo\t| Judul Buku\t\t| Penulis \t\t| Tahun Terbit \t| Stock ')
                print(str(IndexRead+1) + '\t| ' + ListBuku[IndexRead]['Judul Buku'] + '   \t| ' + str(ListBuku[IndexRead]['Penulis']) + '    \t| ' + str(ListBuku [IndexRead]['Tahun Terbit']) + '    \t| ' + str(ListBuku [IndexRead]['Stock']))
        elif (MenuRead == '3'):
            break
        else :
            print('Pilihan yang anda masukkan salah! Input angka sub menu Read harus 1, 2, atau 3!')

# Fungsi Create
def Create():
    while (True):
        print('''
        Ini adalah Menu Create

        List SubMenu :
        1. Menambah buku ke daftar buku
        2. Kembali ke Menu Utama
        ''')
        MenuCreate= input('Masukkan angka menu create yang ingin dijalankan (1 atau 2): ')
        if (MenuCreate == '1'):   
            JudulCreate = input('Masukkan Judul buku yang ingin diinput : ').title()
            ListBukuCreate = []
            for i in range(len(ListBuku)):
                ListBukuCreate.append(ListBuku[i]['Judul Buku'])
            if  JudulCreate not in ListBukuCreate:
                Penulis = input('Masukkan Nama Penulis Buku : ').title()
                while (True):
                    Tahun = input('Masukkan Tahun Terbit Buku : ')
                    if Tahun.isnumeric():
                        break
                    else: 
                        print('Input Tahun Terbit harus berupa angka!')
                while (True):
                    Stock = input('Masukkan Stock Buku : ')
                    if Stock.isnumeric():
                        break
                    else: 
                        print('Input Stock harus berupa angka!')
                
                ListBuku.append({
                    'Judul Buku': JudulCreate, 
                    'Penulis': Penulis,
                    'Tahun Terbit': Tahun,
                    'Stock': Stock})
                print('\nData buku tersimpan!')       
                DaftarBuku()
            else:
                print('\nBuku sudah ada!')
        elif (MenuCreate == '2'):
            break
        else:
            print('Pilihan yang anda masukkan salah! Input angka sub menu Create harus 1 atau 2!')

    
def Update():
    while (True):
        print('''
        Ini adalah Menu Update

        List SubMenu :
        1. Mengupdate daftar buku
        2. Kembali ke Menu Utama
        ''')
        MenuUpdate= input('Masukkan angka menu update yang ingin dijalankan (1 atau 2): ')
        if (MenuUpdate == '1'):
            DaftarBuku()
            JudulUpdate = input('Masukkan Judul buku yang ingin diupdate : ').title()
            ListBukuUpdate = []
            for i in range(len(ListBuku)):
                ListBukuUpdate.append(ListBuku[i]['Judul Buku'])
            if JudulUpdate not in ListBukuUpdate:
                print('\nData yang Anda cari tidak ada!\n')
            else:
                IndexUpdate = ListBukuUpdate.index(JudulUpdate)
                print('No\t| Judul Buku\t\t| Penulis \t\t| Tahun Terbit \t| Stock ')
                print(str(IndexUpdate+1) + '\t| ' + ListBuku[IndexUpdate]['Judul Buku'] + '   \t| ' + str(ListBuku[IndexUpdate]['Penulis']) + '    \t| ' + str(ListBuku [IndexUpdate]['Tahun Terbit']) + '    \t| ' + str(ListBuku [IndexUpdate]['Stock']))
                while (True):
                    LanjutUpdate = input('Melanjutkan ke update data (0=No, 1=Yes) : ')
                    if (LanjutUpdate == '0'):
                        break
                    elif (LanjutUpdate == '1'):
                        while (True):
                            PilihKolom = input('Masukkan kolom yang ingin diupdate : ').title()
                            if PilihKolom in ['Judul Buku','Penulis','Tahun Terbit','Stock']:
                                if PilihKolom in ['Tahun Terbit','Stock']:
                                    while (True):                                        
                                        Value = input('Masukkan value yang ingin diinput : ')
                                        if Value.isnumeric():
                                            break
                                        else: 
                                            print('Input harus berupa angka!')
                                else:
                                    Value = input('Masukkan value yang ingin diinput : ').title()
                                while (True):
                                    YakinUpdate = input('Yakin update data? (0=No, 1=Yes) : ')
                                    if (YakinUpdate == '0'):
                                        break
                                    elif (YakinUpdate == '1'):
                                        ListBuku[IndexUpdate][PilihKolom] = Value
                                        print('Data Terupdate !')
                                        DaftarBuku()
                                        break
                                    else :
                                        print('Pilihan yang anda masukkan salah! Input angka harus 0 atau 1!')
                                break
                            else:
                                print('Kolom yang diinput tidak ada di data!')
                        break
                    else:
                        print('Pilihan yang anda masukkan salah! Input angka harus 0 atau 1!')     
        elif (MenuUpdate == '2'):
            break
        else:
            print('Pilihan yang anda masukkan salah! Input angka sub menu Update harus 1 atau 2!')
        
def Delete():
    while (True):
        print('''
        Ini adalah Menu Delete

        List SubMenu :
        1. Menghapus 1 buku
        2. Kembali ke Menu Utama
        ''')
        MenuDelete= input('Masukkan angka menu update yang ingin dijalankan (1 atau 2): ')
        if (MenuDelete == '1'):
            DaftarBuku()
            JudulDelete = input('Masukkan Judul buku : ').title()
            ListBukuDelete = []
            for i in range(len(ListBuku)):
                ListBukuDelete.append(ListBuku[i]['Judul Buku'])
            if JudulDelete not in ListBukuDelete:
                print('\nData yang Anda cari tidak ada!')
            else:
                IndexDelete = ListBukuDelete.index(JudulDelete)
                del ListBuku[IndexDelete]
                print('\nData Deleted!')
                DaftarBuku()
        elif (MenuDelete == '2'):
            break
        else :
            print('Pilihan yang anda masukkan salah! Input angka sub menu Delete harus 1 atau 2!')
        
def MenuUtama():   
    while (True):
        print('''
Selamat Datang di Menu Utama Perpustakaan

List Menu :
1. Menampilkan Daftar Buku
2. Menambah Buku
3. Mengupdate Daftar Buku
4. Menghapus Buku
5. Exit Program
        ''')
        Menu= input('Masukkan angka menu yang ingin dijalankan (1-5): ')
        if (Menu == '1'):       
            Read()
        elif (Menu == '2'):
            Create()
        elif (Menu == '3'):
            Update()            
        elif (Menu == '4'):
            Delete()
        elif (Menu == '5'):
            print('\nTerima kasih telah menggunakan program Perpustakaan!')
            print('Developer: Herdiansyah P P (Purwadhika JCDSOL08)\n')
            break
        else:
            print('Pilihan yang anda masukkan salah! Input angka Menu harus 1 sampai 5!')

MenuUtama() 