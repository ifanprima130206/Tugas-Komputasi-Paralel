from multiprocessing import Pool

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    with Pool(2) as pool:
        left_sorted, right_sorted = pool.map(sorted, [left, right])
    return merge(left_sorted, right_sorted)

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

if __name__ == "__main__":
    arr = input_numbers()
    print("Sebelum sort:", arr)
    sorted_arr = parallel_merge_sort(arr)
    print("Sesudah sort:", sorted_arr)
