#Esko adalah sebuah progam sederhana yang membantu manusia.
#di buat 17 agustus 2022.

print ("乇丂匚ㄖ")
print ("\n A Tools Help For You")
print("\n")
print("di buat 17 Agustus 2022")
nama_yu = input("Siapa Nama Anda: ")
print ("Selamat datang :",nama_yu)
print ("Menu :")
print ("\n 1.Penghitung Luas \n 2.Kakulator \n 3.Spam Text \n 4.Konvrensi Suhu")

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
      kata = input("Masukan Kata : ")
      
          
      nilai_a =int(input("Masukan Nilai Awal,Tanpa Dengan Koma : "))
      nilai_ak = int(input("Masukan Nilai Akhir,Tanpa Dengan koma : "))
      while nilai_a <= nilai_ak:
          print (kata,nilai_a)
          nilai_a += 1
elif luas == 4:
      
      print ("\nKONVRENSI TEMPERATUR\n")
      print ("1.Celcius \n2.Reamur \n3.Fahrenheit \n4.Kelvin\n")
      pilih_suhu = int(input("Masukan Pilihan :"))
      if pilih_suhu == 1:
          suhu = float(input("Masukan Suhu Dalam Celcius : "))
          reamur = (4/5) * suhu
          fahrenheit = ((9/5) * suhu ) + 32
          kelvin = suhu + 273
          print ("\nSuhu Dalam Celcius :",suhu)
          print("\nSuhu Dalam Reamur :",reamur)
          print("Suhu Dalam Fahrenheit :",fahrenheit)
          print("Suhu Dalam Kelvin :",kelvin)
          
      elif pilih_suhu == 2:
          suhu_r = float(input("Masukan Suhu Dalam Reamur : "))
          Celcius = 5/4 * suhu_r
          fahrenheit = ((9/4) * suhu_r) + 32
          kelvin = ((5/4 ) * suhu_r)+ 273
          print ("\nSuhu Dalam Reamur :",suhu_r)
          print("\nSuhu Dalam Celcius :",Celcius)
          print("Suhu Dalam Fahrenheit :",fahrenheit)
          print("Suhu Dalam Kelvin :",kelvin)
          
      elif pilih_suhu == 3:
           
          suhu_f = float(input("Masukan Suhu Dalam Fahrenheit : "))
          Celcius = 5/9 * (suhu_f-32)
          reamur = 4/5 * ( suhu_f -32)
          kelvin = (((suhu_f-32) * 5/9) + 273.15)
          print ("\nSuhu Dalam Fahrenheit :",suhu_f)
          print("\nSuhu Dalam Celcius :",Celcius)
          print("Suhu Dalam Reamur :",reamur)
          print("Suhu Dalam Kelvin :",kelvin)
          
      elif pilih_suhu == 4:
          suhu_K = float(input("Masukan Suhu Dalam Kelvin : "))
          Celcius = (suhu_K-273)
          reamur = 4/5 * ( suhu_K -275)
          fahrenheit = (((suhu_K-32) * 5/9 )+ 273.15)
          print ("\nSuhu Dalam Kelvin :",suhu_K)
          print("\nSuhu Dalam Celcius :",Celcius)
          print("Suhu Dalam Reamur :",reamur)
          print("Suhu Dalam Fahrenheit :",fahrenheit)
      
      else:
          print("Input Salah")
                     
     
else:
  print("Input yang anda masukan salah ")    
  