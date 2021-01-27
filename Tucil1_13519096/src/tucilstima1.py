import time

f = open("soal11.txt") #baca input
read = f.read().split('\n') #diread dan pembersihan input agar bisa diolah
awalwaktu = time.perf_counter() #waktu mulai eksekusi program
wordcount = len(read) - 2 #jumlah operand
wordarray = ['*' for i in range(wordcount)] #array operand
for i in range(len(read)):
    read[i] = read[i].replace(' ','').replace('+','') #membersihkan text input dari spasi dan +
for i in range(wordcount):
    wordarray[i] = read[i] #memasukkan operand ke array operand
result = read[len(read) - 1] #memasukkan kata hasil
letterarray = [] #array huruf unik awalnya kosong
for i in read:
    for j in i:
        if j != '-':
            if len(letterarray) == 0:
                letterarray.append(j) #jika array masih kosong langsung append
            else:
                unik = True
                for i in range(len(letterarray)):
                    if letterarray[i] == j: #pengecekkan huruf yang sama
                        unik = False
                        break
                if unik:
                    letterarray.append(j) #memasukkan huruf unik ke array
lettercount = len(letterarray)

jumlahtotaltes = 0
found = False
count = 0 #buat break loop
lettervaluearray = [1 for i in range(lettercount)]
hasilarray = [0 for j in range(wordcount)]
maxlength= len(result) #karena panjang kata result pasti lebih besar dari yang lain, hanya untuk kebutuhan mempercantik output aja si ini
if len(letterarray) > 10: #batas huruf di operand 10
    found = True
    print('Jumlah huruf unik melebihi 10')
if wordcount <2:
    found = True
    print('Jumlah operand kurang dari 2')
while found != True:
    n = lettercount-1 #digit terakhir array value huruf
    for i in range(lettercount): #bermula misal ada 3 digit 1 -> 111, akan ditambah 1 terus sampai habis semua kemungkinan value huruf
        lettervaluearray[n] = (lettervaluearray[n] + 1) % 10
        if lettervaluearray[n] == 1:
            n = n-1 #agar bisa manipulasi digit sebelum yang terakhir
        else:
            break #loopnya agar bisa manipulasi semua bagian array, kalau tidak perlu maka dibreak saja
    jumlahtotaltes+=1 #dianggap jumlah total tes mencangkupi tes yang tidak memenuhi syarat huruf unik atau huruf pertama 0
    if lettervaluearray[0] != 1:
        count = 1
    if count == 1 and lettervaluearray[0] == 1: #sudah menghabisi semua kemungkinan
        print("Tidak ada hasil")
        break
    hasil = 0
    valid = True #agar tidak perlu banyak perhitungan yang tidak perlu, dibuat pengecekkan validitas
    for i in range(lettercount):
        for j in range(lettercount):
            if lettervaluearray[i] == lettervaluearray[j] and i!=j: #pengecekkan keunikan value huruf
                valid = False
                break
    if valid: #jika semua nilai huruf unik
        for k in range(wordcount): #dibuat per operand
            stringnilai = ''
            for i in wordarray[k]:
                for j in range(lettercount):
                    if i == letterarray[j]:
                        stringnilai += str(lettervaluearray[j])
            stringnilai = int(stringnilai)
            stringnilai = str(stringnilai) #buat eliminasi yg awalnya 0
            if len(stringnilai) == len(wordarray[k]):
                hasil += int(stringnilai) #penambahan tiap operand
                hasilarray[k] = int(stringnilai) #nilai tiap operand disimpan
            else:
                valid = False
        if valid: #Jika tidak valid tidak dilihat lagi
            stringresult = ''
            for i in result:
                for j in range(lettercount):
                    if i == letterarray[j]:
                        stringresult += str(lettervaluearray[j])
            stringresult = int(stringresult)
            stringresult = str(stringresult)
            if (len(stringresult) == len(result)): #eliminasi yang awalnya 0
                if stringresult == str(hasil): #nilai cocok, ketemu
                    for l in range(wordcount): #formatting output
                        spasi = '  '
                        if l == wordcount-1:
                            spasi = '+ '
                        if len(wordarray[l]) < maxlength:
                            spasi += ' '*(maxlength-len(wordarray[l]))
                        print(spasi + wordarray[l], end='        ') #output soal
                        print(spasi+ str(hasilarray[l])) #output angka
                    print(' ' + (maxlength+2)*'-' + '        ' + (maxlength+2)*'-')
                    print('  ' + result, end='        ')
                    print('  ' + stringresult)
                    found = True
                    break

akhirwaktu = time.perf_counter() #program selesai, waktu akhir program
print('') #tambah newline biar cantik :v
print("Waktu eksekusi program = " + str(akhirwaktu - awalwaktu) + ' detik') #hitung lama eksekusi program
print('Jumlah total tes = ' + str(jumlahtotaltes)) #hitung total tes angka

