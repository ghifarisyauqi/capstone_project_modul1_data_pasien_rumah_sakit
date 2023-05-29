

# Data pasien rumah sakit dalam bentuk list
kodePasien =  ['P0001', 'P0002', 'P0003', 'P0004', 'P0005']
jenisKelamin =  ['Laki-laki', 'Perempuan', 'Perempuan', 'Laki-laki', 'Perempuan']
usia = [23, 31, 33, 29, 18]
penyakit = ['Demam', 'Flu', 'Maag', 'Demam', 'Diare']
biayaPengobatan = [75000, 50000, 65000, 75000, 100000]
obat = ['Paracetamol', 'Decolgen', 'Lansoprazol',' Paracetamol', 'Diapet']


      
              
    
def tampilan_menu():    # Fungsi yang berisi menu utama dari program
    print('''
SELAMAT DATANG DI PUSAT INFORMASI RUMAH SAKIT
__________________________________________________
Menu 1 : Menampilkan data pasien rumah sakit
Menu 2 : Menambahkan data pasien rumah sakit
Menu 3 : Mengubah data pasien rumah sakit
Menu 4 : Menghapus data pasien rumah sakit
Menu 5 : Keluar dari program
__________________________________________________
''')
    print()




def menu1():            # Fungsi yang berisi program menu 1
    while True:
        tampilan_menu1()
        pilihan1 = input('Pilih menu yang ingin diakses : ')
        if pilihan1 == '1':
            data_pasien()
        elif pilihan1 == '2':
            showDataByCode()
        elif pilihan1 == '3':
            rekomendasi_obat()
        elif pilihan1 == '4':
            break
        else :
            print()
            print('- Menu tidak tersedia -')
            print('- Masukkan angka yang sesuai -')
            print()

def tampilan_menu1():   # Fungsi untuk menampilkan menu 1
    print()
    print('''
Menu 1 (Masukkan angka sesuai pilihan Anda)
___________________________________________
1. Tampilkan semua data pasien rumah sakit
2. Tampilkan data sesuai kode pasien
3. Tampilkan rekomendasi obat untuk pasien
4. kembali ke menu utama
___________________________________________
        ''')
    print()

def data_pasien():      # Fungsi untuk menampilkan data pasien
    kodePasien.sort()   # Method agar data dalam list selalu ditampilkan berurutan 
    print(f'''
DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________''')
    for i in range(len(kodePasien)):
          print(f'{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}')
    
    print('''
__________________________________________________________________________________
    ''')
    
def showDataByCode():   # Fungsi untuk menampilkan data pasien berdasarkan kode pasien
    while True:
        menampilkan_data = input('Masukkan kode pasien yang ingin ditampilkan: ').capitalize()
        for i, j in enumerate(kodePasien):
            if menampilkan_data == kodePasien[i] :
                print(f'''
DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu1()       
                break
        else:
            print()
            print('- Kode pasien tidak ditemukan -')
            print()
            break

def rekomendasi_obat(): # Fungsi untuk menampilkan rekomendasi obat setiap penyakit
    nama_penyakit = input('Masukkan nama penyakit pasien: ').capitalize()    
    if nama_penyakit == penyakit[0]:
        print()
        print(f'- Rekomendasi obat untuk {nama_penyakit} adalah {obat[0]} -  ')
        print()
        menu1()
    elif nama_penyakit == 'Flu':
        print()
        print(f'- Rekomendasi obat untuk {nama_penyakit} adalah {obat[1]} -  ')    
        print()
        menu1()
    elif nama_penyakit == 'Maag':
        print()
        print(f'- Rekomendasi obat untuk {nama_penyakit} adalah {obat[2]} -  ')       
        print()
        menu1()
    elif nama_penyakit == 'Diare':
        print()
        print(f'- Rekomendasi obat untuk {nama_penyakit} adalah {obat[4]} -  ')
        print()
        menu1()
    else:
        print()
        print('- Nama penyakit tidak ditemukan -')
        print()
        rekomendasi_obat()




def menu2():            # Fungsi yang berisi program menu 2
    while True:
        tampilan_menu2()
        pilihan2 = input('pilihan menu yang ingin diakses : ')
        if pilihan2 == '1':
            tambah_data()
        elif pilihan2 == '2':
            break
        else :
            print()
            print('- Menu tidak tersedia -')
            print('- Masukkan angka yang sesuai -')
            print()

def tampilan_menu2():   # Fungsi untuk menampilkan menu 2
    print()
    print('''
Menu 2 (Masukkan angka sesuai pilihan Anda)
___________________________________________
1. Tambahkan data pasien baru
2. Kembali ke menu utama
___________________________________________
        ''')
    print()

def tambah_data():      # Fungsi untuk menambahkan data pasien baru
    while True:
        kodePasienBaru = str(input('Masukkan kode pasien: ')).capitalize()
        if kodePasienBaru in kodePasien:
            print()
            print('- Kode pasien sudah ada -')
            print()
        elif kodePasienBaru.isdigit() == True:
            print()
            print('- Kode pasien harus berupa alphanumerik')
            print()
        elif kodePasienBaru.isalpha() == True:
            print()
            print('- Kode pasien harus berupa alphanumerik')
            print()
        else:
            jenisKelaminBaru = input('Masukkan jenis kelamin: ').capitalize()
            usiaBaru = int(input('Masukkan usia pasien: '))
            penyakitBaru = input('Masukkan penyakit pasien: ').capitalize()
            biayaPengobatanBaru = int(input('Masukkan biaya pengobatan pasien: '))
            print(f'''
DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasienBaru:<15} {jenisKelaminBaru:<20} {usiaBaru:<10} {penyakitBaru:<15} {biayaPengobatanBaru:<10}
__________________________________________________________________________________
    ''')
            simpan_perubahan = input('apakah Anda ingin menyimpan data yang di input? (Ya/Tidak): ').capitalize()
            if simpan_perubahan == 'Ya':
                kodePasien.append(kodePasienBaru)
                jenisKelamin.append(jenisKelaminBaru)
                usia.append(usiaBaru)
                penyakit.append(penyakitBaru)
                biayaPengobatan.append(biayaPengobatanBaru)
                print()
                print('- Data berhasil disimpan -')
                menu2()
            elif simpan_perubahan == 'Tidak':
                print()
                print('- Data tidak disimpan -')
                menu2()
                break




def menu3():            # Fungsi yang berisi program menu 3
    while True:
        tampilan_menu3()
        pilihan3 = input('pilihan menu yang ingin diakses : ')
        if pilihan3 == '1':
            ubah_data()
        elif pilihan3 == '2':
            break
        else:
            print('- Menu tidak tersedia -')
            print('- Masukkan angka yang sesuai -')

def tampilan_menu3():   # Fungsi untuk menampilkan menu 3
    print()
    print('''
Menu 3 (Masukkan angka sesuai pilihan Anda)
___________________________________________
1. Ubah data pasien
2. Kembali ke menu utama
___________________________________________
        ''')
    print()

def ubah_data():        # Fungsi untuk mengubah data per kolom
    while True:
        data_pasien()
        mengubah_data = input('Masukkan kode pasien yang ingin diubah: ').capitalize()
        for i, j in enumerate(kodePasien):
            if mengubah_data == kodePasien[i] :
                print(f'''
DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')      
                break
        else:
            print()
            print('- Kode pasien tidak ditemukan -')
            print()
            break   

        kolom_diubah = input('Masukkan nama kolom yang datanya ingin diubah: ').upper()
        if kolom_diubah == 'KODE PASIEN':
            print()
            print('- Kode pasien tidak dapat di ubah, silakan ubah data di kolom lain -')
            print()

        elif kolom_diubah == 'JENIS KELAMIN':
            ubahJenisKelamin = input('Masukkan jenis kelamin baru: ').capitalize()
            yakin = input('Apakah Anda yakin akan mengubah data ini? (Ya/Tidak): ').capitalize()
            if yakin == 'Ya':
                jenisKelamin[i] = ubahJenisKelamin
                print()
                print('- Data berhasil diubah! -')
                print()
                print(f'''DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu3()
            elif yakin == 'Tidak':
                print()
                print('- data tidak jadi diubah -')
                print()
                print(f'''DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu3()
                break

        elif kolom_diubah == 'USIA':
            ubahUsia = int(input('Masukkan usia baru: '))
            yakin = input('Apakah Anda yakin akan mengubah data ini? (Ya/Tidak): ').capitalize()
            if yakin == 'Ya':
                usia[i] = ubahUsia
                print()
                print('- Data berhasil diubah! -')
                print()
                print(f'''DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu3()
            elif yakin == 'Tidak':
                print()
                print('- data tidak jadi diubah -')
                print()
                print(f'''DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu3()
                break

        elif kolom_diubah == 'PENYAKIT':
            ubahPenyakit = input('Masukkan penyakit baru: ').capitalize()
            yakin = input('Apakah Anda yakin akan mengubah data ini? (Ya/Tidak): ').capitalize()
            if yakin == 'Ya':
                penyakit[i] = ubahPenyakit
                print()
                print('- Data berhasil diubah! -')
                print()
                print(f'''
DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu3()
            elif yakin == 'Tidak':
                print()
                print('- data tidak jadi diubah -')
                print()
                print(f'''DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu3()
                break

        elif kolom_diubah == 'BIAYA PENGOBATAN':
            ubahBiayaPengobatan = int(input('Masukkan biaya pengobatan baru: '))
            yakin = input('Apakah Anda yakin akan mengubah data ini? (Ya/Tidak): ').capitalize()
            if yakin == 'Ya':
                biayaPengobatan[i] = ubahBiayaPengobatan
                print()
                print('- Data berhasil diubah! -')
                print()
                print(f'''DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu3()
            elif yakin == 'Tidak':
                print()
                print('- data tidak jadi diubah -')
                print()
                print(f'''DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                menu3()
        else:
            print()
            print('- Nama kolom tidak tersedia -')
        break





def menu4():            # Fungsi yang berisi program menu 4
    while True:
        tampilan_menu4()
        pilihan4 = input('pilihan menu yang ingin diakses : ')
        if pilihan4 == '1':
            hapus_data()
        elif pilihan4 == '2':
            reset()
        elif pilihan4 == '3':
            break
        else:
            print('- Menu tidak tersedia -')
            print('- Masukkan angka yang sesuai -')

def tampilan_menu4():   # Fungsi untuk menampilkan menu 4
    print()
    print('''
Menu 4 (Masukkan angka sesuai pilihan Anda)
___________________________________________
1. Hapus data pasien
2. Reset data
3. Kembali ke menu utama
___________________________________________
        ''')
    print()

def hapus_data():       # Fungsi untuk menghapus data per baris
    while True:
        data_pasien()
        menghapus_data = input('Masukkan kode pasien yang ingin dihapus: ').capitalize()
        for i, j in enumerate(kodePasien):
            if menghapus_data == kodePasien[i] :
                print(f'''
DATA PASIEN RUMAH SAKIT
__________________________________________________________________________________
Kode Pasien     Jenis Kelamin        Usia       Penyakit        Biaya Pengobatan
__________________________________________________________________________________
{kodePasien[i]:<15} {jenisKelamin[i]:<20} {usia[i]:<10} {penyakit[i]:<15} {biayaPengobatan[i]:<10}
__________________________________________________________________________________
''')
                break
        else :
            print('- Kode pasien tidak ditemukan -')
            break
        
        konfirmasi_hapus_data = input('Apakah Anda yakin untuk menghapus data? (Ya/Tidak): ').capitalize()
        if konfirmasi_hapus_data == 'Ya':
            del kodePasien[i]
            data_pasien()
            print()
            print('- Data berhasil dihapus -')
            print()
            menu4()
            break
        elif konfirmasi_hapus_data == 'Tidak':
            print()
            print ('- Data tidak dihapus -')
            print ()
            menu4()
            break

def reset():            # Fungsi untuk mereset semua data yang ada
    data_pasien()
    hapus_semua = input('Apakah Anda ingin mengapus semua data/reset? (Ya/Tidak) ').capitalize()
    if hapus_semua == 'Tidak':
        print()
        print ('- Data tidak dihapus -')
        print ()
        menu4()
    yakin = input('Melakukan reset akan menghilangkan semua data, tetap lanjutkan? (Ya/Tidak) ').capitalize()
    if yakin == 'Ya':
        kodePasien.clear()
        data_pasien()
        print()
        print('- Data berhasil dihapus -')
        print()
        menu4()
        
    elif yakin == 'Tidak':
        print()
        print ('- Data tidak dihapus -')
        print ()
        menu4()
        
                                        
           

def exit():             # Fungsi untuk keluar dari program
    print()
    print('- Terimakasih semoga informasi bisa digunakan dengan baik -')
    print()



def main_app():         # Fungsi yang berisi menu utama dari program
    while True:
        tampilan_menu()
        pilihan = input('Pilihan Menu Yang Diinginkan : ')

        if pilihan == '1' :
            menu1()
            
        elif pilihan == '2':
            menu2()
            
        elif pilihan == '3':
            menu3()
            
        elif pilihan == '4':
            menu4()
            
        elif pilihan == '5':
            exit()
            break
        else :
            print()
            print('- Masukkan angka yang benar!- ')
            print()
            main_app()
        
       

main_app()              # Memanggil fungsi main_app agar program berjalan