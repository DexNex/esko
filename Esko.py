#Esko adalah sebuah progam sederhana yang membantu manusia.
#di buat 17 agustus 2022.
#di buat oleh DexNex(Ali imam mustaqiim)

print ("乇丂匚ㄖ v1.0")
print ("by DexNex(Ali imam mustaqiim)")
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
elif luas == 2:
  print("\n 1.Kakulator biasa \n 2.Kakulator Ajaib")
elif luas == 3: 
  print("Tunggu Fitur Selajutnya ~_+ ")
else:
  print("Input yang anda masukan salah ")    