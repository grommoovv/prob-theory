import math
import matplotlib.pyplot as plt
import pandas as pd
import os
from collections import Counter
from PIL import Image

def get_data():
	while True:
		file_name = input("Введите имя файла: ")
		if os.path.isfile(file_name):
			data = pd.read_csv(file_name, header=None)
			print("Входнные данные:\n", ' '.join(map(str, data[0].tolist())))
			return data
		else:
				print("Файл не найден. Введите имя файла еще раз.")

def get_user_choice():
	print("\nВыберите действие:")
	print("1. Составление вариационного ряда и вывод его на экран;")
	print("2. Составление и вывод на экран статистического ряда частот и относительных частот, построение полигона для каждого из них;")
	print("3. Нахождение эмпирической функции распределения F*(x) с выводом на экран определения эмпирической функции распределения и ее конкретного вида для заданного статистического распределения, построение графика F*(х);")
	print("4. Вывод на экран формул для вычисления числовых характеристик выборки: ̄xᵦ, Dᵦ, σᵦ, Sᵦ, их вычисление и вывод на экран полученных результатов;")    
	return int(input("Введите номер: "))

def print_statistical_frequency_row(unique_date, element_count):
	print(f'\nСтатистический ряд частот:')

	print("xᵢ| ", end='')
	for i in unique_date:  
		if i % 10 == i: print(f"   {i}   | ", end="")
		else: print(f"  {i}   | ", end="")

	print("\nnᵢ| ", end='')
	for _, count in element_count.items():
		print(f"   {count}   | ", end="")

def print_statistical_relative_frequency_row(unique_date, element_count, length):
	print(f'\nСтатистический ряд относительных частот:')
	
	print("xᵢ| ", end='')
	for i in unique_date:  
			if i % 10 == i: print(f"  {i}    | ", end="")
			else: print(f"  {i}   | ", end="")

	print("\nnᵢ| ", end='')
	for _, count in element_count.items():
			print(f" {count}/{length}  | ", end="")

def allocation_func(freq, date):
    leng = len(freq)
    Fix = 0
    print(f"         ╭─ F(X) = {Fix} , при x < {date[0]}")
    for k in range(0, leng - 1):
        Fix += freq[k]
        if k == (len(freq)-1)//2:
            print(f"F*(x) = ━┥  F(X) = {Fix} при {date[k]} ≤ X < {date[k + 1]}")
        else:
            print(f"         │  F(X) = {Fix}, при {date[k]} ≤ X < {date[k + 1]}")
    print(f"         ╰─ F(X) = {1} , при X >= {date[leng - 1]}")

def empirical_func(data, freq):
    data = [0] + data
    data.append(data[len(data) - 1] + 10)
    leng = len(freq)
    fix = 0
    Mass_Emperical = []
    Mass_Emperical.append(0)
    for k in range(0, leng - 1):
        fix += freq[k]
        Mass_Emperical.append(fix)
    Mass_Emperical.append(1)
    Mass_Emperical.append(1)
    plt.title('График эмпирической функции')
    plt.xlabel('xᵢ')
    plt.ylabel('F*(xᵢ)')
    plt.axis((0, max(data) + 1, 0, max(freq) + 1))
    plt.grid(True)
    plt.plot(max(data) + 1, 0, ">k", clip_on=False, ms=8)
    plt.plot(0, max(freq) + 1, "^k", clip_on=False, ms=8)
    plt.hlines(y=Mass_Emperical[0], xmin=data[0], xmax=data[1], color='black', linestyle='-', linewidth=2)
    for i in range(1, len(data) - 1):
        plt.hlines(y=Mass_Emperical[i], xmin=data[i], xmax=data[i + 1], color='black', linestyle='-', linewidth=2)
        plt.scatter(data[i], Mass_Emperical[i], marker='<', s=35, color='black')

    plt.show()

def calc_x(ms, ns):
    leng = len(ms)

    result = 0
    for j in range(leng):
        res = ms[j] * ns[j]
        result += res
    result = result / sum(ns)
    return result

def calc_d(ms, ns, xv):
    leng = len(ms)
    result = 0
    for j in range(leng):
        res = ((ms[j] - xv) ** 2) * ns[j]
        result += res
    result = result / sum(ns)
    return result

def calc_s(ms, xv):
    leng = len(ms)
    result = 0
    for j in range(leng - 1):
        res = ((ms[j] - xv) ** 2)
        result += res
    result = result / (leng - 1)
    result = math.sqrt(result)

    return result

def calc_b(S):
    result = math.sqrt(S)
    return result

def poligon(data, freq, title):
    plt.title(title)
    plt.xlabel('xᵢ')
    plt.ylabel('nᵢ')
    plt.plot(data, freq)
    plt.plot(data, freq, 'bo')
    plt.axis((0, max(data) + 1, 0, max(freq) + 1))
    plt.grid(True)
    plt.plot(max(data)+1, 0, ">k",  clip_on=False, ms=8)
    plt.plot(0, max(freq)+1, "^k",  clip_on=False, ms=8)
    plt.show()

def show_formulas():
	img = Image.open("image.png")
	plt.figure()
	plt.axis("off")
	plt.imshow(img)
	plt.show()

def main():
	raw_data = get_data()
	sorted_data = [int(el) for el in raw_data.iloc[0, 0].split()]
	sorted_data.sort()
	unique_date = sorted(set(sorted_data))

	length = len(sorted_data)

	element_count = Counter(sorted_data)

	freq = []
	relative_freq = []

	for _, count in element_count.items(): 
		freq.append(count)
		relative_freq.append(count / length)
    
	while True:
			
			choice = get_user_choice()

			if choice == 1:
					print(f"\nВариационный ряд: ")
					for i in sorted_data: 
						print(f"{i} | ", end="")
					print()
					
			elif choice == 2:
					print_statistical_frequency_row(unique_date, element_count)
					print()
					print_statistical_relative_frequency_row(unique_date, element_count, length)

					poligon(unique_date, freq, "Полигон cтатистического ряда частот")
					poligon(unique_date, relative_freq, "Полигон cтатистического ряда относительных частот")
					
			elif choice == 3:
					print("\nЭмпирической функцией распределения называется функция вида F*(x) действительного аргумента x,")
					print("значения которой в каждой точке равно накопленной относительной часоте событий, при (X < x).")
					print("\n                  nₓ\nФормула: F*(x) = ———\n                  n")
					
					allocation_func(relative_freq, unique_date)
					empirical_func(unique_date, relative_freq)
					
			elif choice == 4:
					print(f" ̄xᵦ = {calc_x(unique_date, freq)}")
					print(f"Dᵦ = {calc_d(unique_date, freq, calc_x(unique_date, freq))}")
					print(f"σ = {calc_b(calc_d(unique_date, freq, calc_x(unique_date, freq)))}")
					print(f"Sᵦ = {calc_s(unique_date, calc_x(unique_date, freq))}")
					show_formulas()
					
			elif choice == 0:
					print("\nПрограмма завершена.")
					break
			
			else:
				print("\nНеверно выбрано действие. Попробуйте снова.")

main()

