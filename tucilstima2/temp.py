#Girvin Junod 13519096 K02 Tucil Stima 2
'''
Format penulisan soal seperti
A, B, C, D.
E, F.
G.
H, I.
'''
#syarat, soal harus ada di folder yang sama dengan file python
namafile = "soal.txt" #ganti nama soal di sini
f = open(namafile) #baca soal
read = f.read().split('\n') #dipisahkan dari newline
listkuliah = [] #list representasi DAG. List berisi list lainnya.
for i in range(len(read)):
    read[i] = read[i].replace('.','') #menghilangkan titik
    if read[i] != '': #jika bukan empty space
        templist = read[i].split(',') #dipisahkan berdasarkan koma
        for j in range (len(templist)): #Menghapus trailing dan leading white space
            templist[j] = templist[j].strip()
        listkuliah.append(templist) #Dimasukkan ke DAG

nsemester = 0 #Menghitung semester, asumsi maksimal 8 semester

while len(listkuliah): #Selama DAG masih berisi
    nsemester += 1
    if nsemester > 8: #Kalau lebih dari 8 semester dipotong
        break
    semesternow = [] #array sementara penyimpan mata kuliah yang bisa diambil untuk semester ini
    keambil = False
    for j in listkuliah:
        if len(j) == 1: #Mengambil semua matakuliah yang syaratnya sudah terpenuhi
            keambil = True
            ambil = j[0] #Karena tinggal 1 ambil elemen pertama
            semesternow.append(ambil) #Dimasukkan ke array sementara
    if keambil:
        k = 0
        while k < len(listkuliah):
            for l in semesternow:
                if l in listkuliah[k]: #Menghapus mata kuliah yang diambil dari syarat mata kuliah lain
                    listkuliah[k].remove(l)
            if len(listkuliah[k]) == 0: #Menghapus mata kuliah yang diambil dari list kuliah
                listkuliah.remove(listkuliah[k])
                k-=1
            k+=1
    #Merubah angka ke angka romawi untuk output
    if nsemester == 1:
        roman = "I"
    elif nsemester == 2:
        roman = "II"
    elif nsemester == 3:
        roman = "III"
    elif nsemester == 4:
        roman = "IV"
    elif nsemester == 5:
        roman = "V"
    elif nsemester == 6:
        roman = "VI"
    elif nsemester == 7:
        roman = "VII"
    elif nsemester == 8:
        roman = "VIII" 
    #output
    print("Semester " + roman + ": ", end= "")
    for n in range (len(semesternow)): 
        if n == len(semesternow) - 1: #Formatting output
            print(semesternow[n], end="")
            if len(listkuliah) == 0:
                print(".", end= "")
        else:
            print(semesternow[n], end=", ")
    print("")