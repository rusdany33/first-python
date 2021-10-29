# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 04:27:15 2021

@author: rusda
"""
def halo_dunia():
    print('halo semua! halo rekan!')

# fungsi dan parameter
def selamat_datang(nama):
    print(f'halo {nama} selamat datang!')

#fungsi init
class Kucing():
    def __init__(self):
        print("Anggora bulu putih, mata biru laut")
tampilkan = Kucing()

# menghitung total nilai
def fungsi_total_nilai(var_harian, var_uts, var_uas) :
    var_harian = int(var_harian) * 0.3
    var_uts = int(var_uts) * 0.3
    var_uas = int(var_uas) * 0.4

    var_total = var_harian + var_uts + var_uas
    return var_total

#Deklarasi Fungsi Perulangan
def fungsi_perulangan():
    var_hasil_perulangan = 0
    for i in range(1,3):
        print("--------Nilai Ke ",i,"--------")
        var_harian = input("Nilai Harian : ")
        var_uts = input("Nilai UTS : ")
        var_uas = input("Nilai UAS : ")

        #Pemanggilan fungsi Penjumlahan
        var_hasil_perulangan +=(int(fungsi_total_nilai(var_harian, var_uts, var_uas)))

    return var_hasil_perulangan /i

kota = 'Lamongan'

def halo() :
  print(kota)

print('[print secara langsung]', kota)
print('[panggil fungsi halo]', end=' ')

halo()
