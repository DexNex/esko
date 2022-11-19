#Esko adalah sebuah progam sederhana yang membantu manusia.
#di buat 17 agustus 2022.

print ("乇丂匚ㄖ v1.0")
print ("\n Alat Untuk Memecahkan Masalah Matematika")
print("\n")
print("17 Agustus 2022")
nama_yu = input("Siapa Nama Anda: ")
print ("Selamat datang :",nama_yu)
print ("Menu :")
print ("\n 1.Penghitung Luas \n 2.Kakulator \n 3.Lainya \n")

luas = int(input("Masukan Pilihan :"))
if luas == 1:
  print("\n 1.Luas persegi panjang \n 2.Luas persegi \n 3.Segitiga \n 4.Lingkaran")
  #menu
  ls = int(input("\n Masukan pilihan :"))
  if ls == 1:
     p = int(input("Panjang :"))
     l = int(input ("Lebar : "))
     j = p*l
     print("haslinya :",j)
  if ls == 2:
     pp = int(input("Panjang"))
     jp = pp*pp
     print ("hasilnya :",jp)
  if ls == 3:
     la = int(input("Alas"))
     lt = int(input("tinggi"))
     js = 0.5*la*lt
     print ("hasilnya :",js)
  if ls == 4:
     ll = int(input("Jaring Jaring"))
     hl = 3.14*ll*ll
     print ("hasilnya :",hl)
  else:
      print("Input salah")
      
elif luas == 2:
  print("\n 1.Kakulator biasa \n 2.Kakulator Ajaib\n")
  kak = int(input("Masukan Input :"))
  if kak == 1:
      print ("\n 1.Penambahan \n 2.Pengurangan \n 3.Perkalian \n 4.Pembagian\n")
      kak = int(input("Masukan Input :"))
  if kak == 1:
      tamb = int(input("Masukan Nilai A : "))
      tamb2 = int(input("Masukan Nilai B : "))
      juml = tamb+tamb2
      print ("Hasil : ",juml)
  elif kak == 2:
      peng= int(input("Masukan Nilai A : "))
      peng2= int(("Masukan Nilai B : "))
      juml2= peng-peng2
      print ("Hasil : ", juml2)
  elif kak == 3:
      perk= int(input("Masukan Nilai A : "))
      perk2 = int(input("Masukan Nilai B : "))
      juml3 = perk*perk2
      print ("Hasil : ",juml3)
  elif kak == 4:
      pemb=int(input("Masukan Nilai A : "))
      pemb2 = int(input("Masukan Nilai B : "))
      juml4 = pemb//pemb2
      print ("Hasil : ", juml4)
  else:
      print("Input Salah")
      
elif luas == 3: 
  print ("\n 1. Spam Text" "\n 2.Lainya")
  menu_3 = int(input("\nMasukan Input : "))
  if menu_3 == 1:
      kata = input("Masukan Kata : ")
      nilai_a = int(input("Masukan Nilai Awal : "))
      nilai_ak = int(input("Masuka Nilai Akhir : "))
      while nilai_a <= nilai_ak:
          print (kata,nilai_a)
          nilai_a += 1
          
else:
  print("Input yang anda masukan salah ")    
  