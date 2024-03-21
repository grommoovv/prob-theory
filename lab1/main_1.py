import math

def arrangement_without_repetition(n, k):
    if n < k:
        return "Ошибка: Количество элементов должно быть не меньше размера выборки."

    return math.perm(n, k)

def arrangement_with_repetition(n, k): return n ** k

def permutation_without_repetition(n): return math.factorial(n)

def permutation_with_repetition(n, counts):
    print(counts)
    denominator = 1
    for count in counts:
        denominator *= math.factorial(count)
    return math.factorial(sum(counts)) // denominator

def combination_without_repetition(n, k):
    if n < k:
        return "Ошибка: Количество элементов должно быть не меньше размера выборки."

    return math.comb(n, k)

def combination_with_repetition(n, k): return math.comb(n + k - 1, k)

def main():
    print("Выберите формулу:")
    print("1. Размещение без повторений (A(n,k) = n! / (n - k)!)")
    print("2. Размещение с повторениями (n^k)")
    print("3. Перестановка без повторений (n!)")
    print("4. Перестановка с повторениями (n! / (n_1! * n_2! * ... * n_k!))")
    print("5. Сочетание без повторений (C(n,k) = n! / (k!(n - k)!))")
    print("6. Сочетание с повторениями (C(n+k-1,k) = (n+k-1)! / (k!(n-1)!))")

    choice = input("Введите номер формулы: ")

    if choice == '1':
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите размер выборки (k): "))

        result = arrangement_without_repetition(n, k)
        print(f"Число размещений без повторений: {result}")
    elif choice == '2':
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите размер выборки (k): "))

        result = arrangement_with_repetition(n, k)
        print(f"Число размещений с повторениями: {result}")
    elif choice == '3':
        n = int(input("Введите количество элементов (n): "))

        result = permutation_without_repetition(n)
        print(f"Число перестановок без повторений: {result}")
    elif choice == '4':
        n = int(input("Введите количество элементов (n): "))
        counts = list(map(int, input("Введите количество повторений для каждого элемента (через пробел): ").split()))

        result = permutation_with_repetition(n, counts)
        print(f"Число перестановок с повторениями: {result}")
    elif choice == '5':
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите размер выборки (k): "))

        result = combination_without_repetition(n, k)
        print(f"Число сочетаний без повторений: {result}")
    elif choice == '6':
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите размер выборки (k): "))

        result = combination_with_repetition(n, k)
        print(f"Число сочетаний с повторениями: {result}")
    else:
        print("Ошибка: Неверный выбор формулы.")
        
main()
