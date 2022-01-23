#variabel untuk jawaban benar dan salah
betul = 'Selamat kamu benar!'
salah = 'Maaf jawaban kamu masih salah. Coba lagi yah!'

#variabel score untuk menghitung jawaban yang benar, jika benar + 1
score = 0

#menampilan tulisan
print('Selamat datang di QuizApp V2')
print('====================')
print('1. Buah - Buahan')
print('2. Kendaraan')
print('3. Teknologi')
print('====================')
print('Silahkan dipilih kuis yang kamu inginkan!')

#variabel untuk menentukan kuis
selects = int(input('Tuliskan Jawabanmu: '))

# proses if else jika sudh ditentukan kuisnya
if selects == 1:
    print('\n====BUAH-BUAHAN====')
    question1 = input('Buah apa yang berwarna kuning? ')
    if question1.lower() == 'pisang':
        print(betul)
        score += 1
    else:
        print(salah)
    
    question2 = input('Buah apa yang berwarna ungu? ')
    if question2.lower() == 'anggur':
        print(betul)
        score += 1
    else:
        print(salah)
            
elif selects == 2:
    print('\n====Mekanik====')
    question1 = input('Apa kepanjangan dari SIM? ')
    if question1.lower() == 'surat izin mengemudi':
        print(betul)
        score += 1
    else:
        print(salah)
    question2 = input('Mobil memiliki berapa roda? ')
    if question2 == '4':
        print(betul)
        score += 1
    elif question2.lower() == 'empat':
        print(betul)
        score += 1
    else:
        print(salah)
        
elif selects == 3:
    print('\n====Teknologi====')
    question1 = input('Apa kepanjangan dari PC? ')
    if question1.lower() == 'personal computer':
        print(betul)
        score += 1
    else:
        print(salah)
    question2 = input('Apa kepanjangan dari RAM? ')
    if question2.lower == 'random access memory':
        print(betul)
        score += 1
    else:
        print(salah)
else: 
    print('Not Found, Try Again')
    quit()

#proses menghitung hasil / score
hasil = score * 100 /2

#menampilkan nilai
print('Nilaimu adalah: ',hasil,'%.')