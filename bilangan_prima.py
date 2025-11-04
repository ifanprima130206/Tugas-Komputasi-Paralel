from multiprocessing import Pool

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime(n):
    return n if is_prime(n) else None

def input_range():
    while True:
        try:
            start = int(input("Masukkan nilai awal: "))
            end = int(input("Masukkan nilai akhir: "))
            if start < 0 or end < 0:
                print("Nilai harus >= 0, coba lagi.")
                continue
            if start > end:
                print("Nilai awal harus <= nilai akhir, coba lagi.")
                continue
            return start, end
        except ValueError:
            print("Input harus berupa angka, coba lagi.")

if __name__ == "__main__":
    start, end = input_range()
    numbers = range(start, end + 1)
    
    print(f"Mengecek bilangan prima dari {start} hingga {end}...")

    with Pool() as pool:
        primes = list(filter(None, pool.map(check_prime, numbers)))
    
    print(f"Ditemukan {len(primes)} bilangan prima:")
    print(primes)
