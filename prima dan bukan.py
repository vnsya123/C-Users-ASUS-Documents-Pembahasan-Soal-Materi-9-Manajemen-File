def cek_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def proses_file(file):
    with open(file, 'r') as f:
        baris = f.readlines()
    
    print(f"Hasil dari {file}:")
    for i, isi in enumerate(baris):
        try:
            angka = int(isi.strip())
            if cek_prima(angka):
                print(f"Baris {i+1}: {angka} adalah bilangan **prima**")
            else:
                print(f"Baris {i+1}: {angka} **bukan** bilangan prima")
        except ValueError:
            print(f"Baris {i+1}: Bukan angka valid")
    print()


proses_file('file1.txt')
proses_file('file2.txt')
