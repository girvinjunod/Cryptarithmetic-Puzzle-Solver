#Girvin Junod 13519096 K02 Tucil Stima 2

#Program ini terdiri dari fungsi baca soal dari file, toposortnya, dan output
def namaaplikasi(): #Print nama aplikasi
    print("SUSUNAN RENCANA KULIAH DENGAN APLIKASI SIX*3:")

def bacafile(namafile): #membaca input dari file, output list representasi DAG sesuai format
    '''
    Format penulisan soal seperti
    A, B, C, D.
    E, F.
    G.
    H, I.
    '''
    #soal asumsi ada di folder yang sama dengan file python
    f = open(namafile) #baca soal
    read = f.read().split('\n') #dipisahkan dari newline
    listkuliah = [] #list representasi DAG. List berisi list lainnya.
    for i in range(len(read)):
        read[i] = read[i].replace('.','') #menghilangkan titik
        if read[i] != '': #jika bukan empty space
            templist = read[i].split(',') #dipisahkan berdasarkan koma
            for j in range (len(templist)): #Menghapus trailing dan leading white space
                templist[j] = templist[j].strip()
            kosong = False
            for k in range (len(templist)): #Pengecekkan jika ada yang list kosong
                if templist[k] == "":
                    kosong  = True
                    break
            if kosong == False:
                listkuliah.append(templist) #Dimasukkan ke DAG
    return listkuliah

def toposort(listdag): 
    #untuk toposort, input list representasi DAG sesuai format, output list berisi node yang sudah di topo sort
    #Node tingkat sama (sama-sama bisa diambil) dikelompokkan menjadi satu string dan dipisah dengan koma
    #Contoh output: ['A', 'B , C', 'D']
    hasil = []
    while len(listdag): #Selama DAG masih berisi
        now = [] #list sementara penyimpan node yang bisa diambil untuk semester ini
        keambil = False
        for j in listdag:
            if len(j) == 1: #Mengambil semua node yang syaratnya sudah terpenuhi
                keambil = True
                ambil = j[0] #Karena tinggal 1 ambil elemen pertama
                now.append(ambil) #Dimasukkan ke list sementara
        if keambil:
            k = 0
            while k < len(listdag):
                for l in now:
                    if l in listdag[k]: #Menghapus  node yang diambil dari syarat node lain
                        listdag[k].remove(l)
                if len(listdag[k]) == 0: #Menghapus node yang diambil dari list representasi DAG
                    listdag.remove(listdag[k])
                    k-=1
                k+=1
        #output
        str = ""
        for n in range (len(now)): 
            if n == len(now) - 1: #Formatting output
                str += now[n]
            else:
                str += now[n]
                str += ", "
        hasil.append(str)
    return hasil

def outputkuliah(hasil): #input list yang sudah tersort, output menuliskan hasil sesuai tujuan program yaitu untuk mengambil mata kuliah
    #Format output menuruti persoalan mata kuliah
    for i in range (len(hasil)):
        if i > 7: #Kalau lebih dari 8 semester dipotong
            break
        #Merubah angka ke angka romawi untuk output
        if i+1 == 1:
            roman = "I"
        elif i+1 == 2:
            roman = "II"
        elif i+1 == 3:
            roman = "III"
        elif i+1 == 4:
            roman = "IV"
        elif i+1 == 5:
            roman = "V"
        elif i+1 == 6:
            roman = "VI"
        elif i+1 == 7:
            roman = "VII"
        elif i+1 == 8:
            roman = "VIII"

        str = "Semester " + roman + ": "
        print(str + hasil[i], end= "")
        if i == len(hasil) - 1: #Kalau yang paling akhir kasih titik di akhirnya
            print(".")
        else:
            print()

#syarat, soal harus ada di folder yang sama dengan file python

#Main Program

#ganti nama soal di sini
namafile = "soal9.txt" 

namaaplikasi()
listkuliah = bacafile(namafile)
hasil = toposort(listkuliah)
outputkuliah(hasil)