        import numpy as np


        def get_matrix_input():
        while True:
                try:
                n = int(input("Masukkan jumlah persamaan: "))
                m = int(input("Masukkan jumlah variabel: "))

                if n <= 0 or m <= 0:
                        print("Jumlah harus lebih dari 0.")
                        continue

                matrix = np.zeros((n, m + 1))
                print(f"Masukkan matriks ukuran {n} x {m + 1}:")

                for i in range(n):
                        while True:
                        try:
                                row = list(map(float, input(f"Baris {i + 1}: ").split()))
                                if len(row) != m + 1:
                                print(f"Harus {m + 1} angka.")
                                continue
                                matrix[i] = row
                                break
                        except ValueError:
                                print("Input harus angka.")

                return matrix

                except ValueError:
                print("Input tidak valid.")


        def gaussian_elimination(matrix):
        matrix = matrix.astype(float)
        rows, cols = matrix.shape

        print("\nOriginal Matrix:")
        print(np.round(matrix, 2))
        print("-" * 30)

        for i in range(rows):
                pivot_row = max(range(i, rows), key=lambda r: abs(matrix[r, i]))

                if matrix[pivot_row, i] == 0:
                continue

                if pivot_row != i:
                matrix[[i, pivot_row]] = matrix[[pivot_row, i]]
                print(f"\nR{i + 1} <-> R{pivot_row + 1}")
                print(np.round(matrix, 2))
                print("-" * 30)

                matrix[i] /= matrix[i, i]
                print(f"\nNormalisasi R{i + 1}")
                print(np.round(matrix, 2))
                print("-" * 30)

                for k in range(i + 1, rows):
                factor = matrix[k, i]
                matrix[k] -= factor * matrix[i]
                print(f"\nR{k + 1} = R{k + 1} - {factor:.2f} * R{i + 1}")
                print(np.round(matrix, 2))
                print("-" * 30)

        return matrix


        def solve_system(matrix):
        rows, cols = matrix.shape
        reduced = gaussian_elimination(matrix)

        rank_coeff = np.linalg.matrix_rank(reduced[:, :-1])
        rank_aug = np.linalg.matrix_rank(reduced)
        variables = cols - 1

        if rank_coeff != rank_aug:
                print("\nSistem tidak memiliki solusi.")
                return

        if rank_coeff < variables:
                print("\nSistem memiliki solusi tak hingga.")
                return

        solution = np.zeros(variables)
        for i in range(variables - 1, -1, -1):
                solution[i] = reduced[i, -1] - np.dot(reduced[i, i + 1:variables], solution[i + 1:variables])

        print("\nSistem memiliki solusi unik:")
        print("Solution:", np.round(solution, 4))


        if __name__ == "__main__":
        matrix = get_matrix_input()
        solve_system(matrix)
