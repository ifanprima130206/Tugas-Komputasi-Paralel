from multiprocessing import Pool

def find_index(args):
    arr, target, offset = args
    return [i + offset for i, x in enumerate(arr) if x == target]

def input_numbers():
    while True:
        user_input = input("Masukkan angka dipisahkan koma contoh: 5,3,7,8,2 : ")
        try:
            numbers = [int(x.strip()) for x in user_input.split(",")]
            if not numbers:
                print("Daftar kosong, coba lagi.")
                continue
            return numbers
        except ValueError:
            print("Input harus berupa angka, coba lagi.")

def input_target():
    while True:
        try:
            target = int(input("Masukkan angka yang ingin dicari: "))
            return target
        except ValueError:
            print("Input harus berupa angka, coba lagi.")

if __name__ == "__main__":
    arr = input_numbers()
    target = input_target()

    n_process = 4
    chunk_size = len(arr) // n_process
    chunks = []
    for i in range(n_process):
        start = i * chunk_size
        end = None if i == n_process - 1 else (i + 1) * chunk_size
        chunks.append((arr[start:end], target, start))

    with Pool(n_process) as pool:
        results = pool.map(find_index, chunks)

    indices = [idx for sublist in results for idx in sublist]

    print(f"List awal: {arr}")
    print(f"Target yang dicari: {target}")
    print(f"Target ditemukan di index: {indices}")
