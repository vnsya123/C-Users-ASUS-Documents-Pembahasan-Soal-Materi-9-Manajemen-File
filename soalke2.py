def jalankan_soal(nama_file):
    print(f"nama file1: {nama_file}\n")
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                if '||' not in baris:
                    continue  
                soal, jawaban = baris.strip().split('||')
                soal = soal.strip()
                jawaban_benar = jawaban.strip().lower()

                print(soal)
                user_jawab = input("Jawab: ").strip().lower()

                if user_jawab == jawaban_benar:
                    print("Jawaban benar!\n")
                else:
                    print("Jawaban salah!\n")
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")


jalankan_soal('soal.txt')
