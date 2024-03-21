from matplotlib import pyplot as plt
from math import floor, log10
from PIL import Image
from tkinter import filedialog

def get_data():
	while True:
		fname = filedialog.askopenfilename(title="Выберите файл с данными")
		if fname:
			f = open(fname)
			data = [float(x) for x in f.read().split()]
			break
	return data

def get_user_choice():
    print("\nВыберите интересующие вас пункты: ")
    print("1. Задание количества интервалов, получение и вывод на экран интервального ряда частот и относительных частот, построение соответствующих гистограмм;")
    print("2. Построение группированного ряда распределения частот и относительных частот и построение соответствующих полигонов;")
    print("3. Нахождение и вывод на экран эмпирической функции распределения F*(х) для интервальных и группированных рядов, построение их графиков;")
    print("4. Вывод на экран формул для вычисления числовых характеристик выборки: ̄xᵦ, Dᵦ, σᵦ, Sᵦ, их вычисление и вывод на экран полученных результатов;")
    print("0. Завершить программу;")
    return int(input("Введите необходимый номер: "))

def print_interval_frequency_row(interval_count, min_value, max_value, step, ns):
    print("\nИнтервальный ряд частот:")
    print()
    print("┃xᵢ;xᵢ₊₁┃", end='')
    counter = min_value
    for i in range(interval_count - 1):
        print(f"{counter:>6.2f};{counter + step:<6.2f}", end='┃')
        counter += step
    print(f"{counter:>6.2f};{max_value:<6.2f}", end='┃')
    print("\n┃  nᵢ   ┃", end='')
    [print(f"{n:^13}", end='┃') for n in ns]
    print()

def print_interval_relative_frequency_row(interval_count, min_value, max_value, step, ws):
    # Относительные частоты
    print("\nИнтервальный ряд относительных частот:")
    print()
    print("┃xᵢ;xᵢ₊₁┃", end='')
    counter = min_value
    for i in range(interval_count - 1):
        print(f"{counter:>6.2f};{counter + step:<6.2f}", end='┃')
        counter += step
    print(f"{counter:>6.2f};{max_value:<6.2f}", end='┃')
    print("\n┃  wᵢ   ┃", end='')
    [print(f"    {w:.3f}    ", end='┃') for w in ws]
    print()

def histogram_interval_frequency_row(step, unique_data, max_values_list, ns):
    # Гистограммы
    # Частоты
    histns = [n / step for n in ns]
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(unique_data[0] - 1, min(0.0, unique_data[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=8)
    ax.text(0, 0, '0', color='black', fontsize=12, ha='right', va='bottom')
    # plt.style.use('ggplot')
    plt.xlim((unique_data[0] - 1, unique_data[-1] + 1))
    plt.ylim((0, max(histns) + max(histns) / 100))
    plt.grid()  # частоты
    plt.stairs(histns, max_values_list, fill=True, facecolor="yellow",edgecolor="black", linewidth=1.8, zorder=3)
    plt.vlines(max_values_list[1:-1], 0, histns[:-1], color="black", zorder=4)
    
    plt.title('Гистограмма интервального ряда частот')
    plt.xlabel('xᵢ')
    plt.ylabel('nᵢ')
    plt.xticks(max_values_list)
    plt.yticks(histns)

def histogram_interval_relative_frequency_row(step, unique_data, max_values_list, ws):
    # Относительные частоты
    histws = [w / step for w in ws]
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(unique_data[0] - 1, min(0.0, unique_data[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=8)
    ax.text(0, 0, '0', color='black', fontsize=12, ha='right', va='bottom')

    # plt.style.use('ggplot')
    plt.xlim((unique_data[0] - 1, unique_data[-1] + 1))
    plt.ylim((0, max(histws) + max(histws) / 100))
    plt.grid()  # частоты
    plt.stairs(histws, max_values_list, fill=True, facecolor="red",edgecolor="black", linewidth=1.8, zorder=3)
    plt.vlines(max_values_list[1:-1], 0, histws[:-1], color="black", zorder=4)

    plt.title('Гистограмма интервального ряда относительных частот')
    plt.xlabel('xᵢ')
    plt.ylabel('wᵢ')
    plt.xticks(max_values_list)
    plt.yticks(histws)
    plt.show()

def print_frequency_rows(xs, ns, ws):
    print("Группированный ряд частот:")
    print()
    print("┃xᵢ ┃", end='')
    [print(f"{x:^6.2f}", end='┃') for x in xs]
    print("\n┃nᵢ ┃", end='')
    [print(f"{n:^6}", end='┃') for n in ns]
    print()
    # Относительные частоты
    print("Группированный ряд относительных частот:")
    print()
    print("┃xᵢ ┃", end='')
    [print(f"{x:^6.2f}", end='┃') for x in xs]
    print("\n┃wᵢ ┃", end='')
    [print(f" {w:.3f}", end='┃') for w in ws]
    print()

def plot_statistical_frequency_row(unique_data, ns, xs):
    # Найти и вывести полигоны частот
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(unique_data[0] - 1, min(0.0, unique_data[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=8)
    plt.xlim((unique_data[0] - 1, unique_data[-1] + 1))
    plt.ylim((0, max(ns) + max(ns) / 100))
    plt.grid()  # частоты
    plt.plot(xs, ns, linewidth=3, color='orange')

    plt.title('Полигон статистического ряда частот')
    plt.xlabel('xᵢ')
    plt.ylabel('nᵢ')
    plt.xticks(xs)
    plt.yticks(ns)

def plot_statistical_relative_frequency_row(unique_data, ws, xs):
    # Относительных частот
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(unique_data[0] - 1, min(0.0, unique_data[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=8)
    plt.xlim((unique_data[0] - 1, unique_data[-1] + 1))
    plt.ylim((0, max(ws) + max(ws) / 100))
    plt.grid()
    plt.plot(xs, ws, linewidth=3, color='red')

    plt.title('Полигон статистического ряда относительных частот')
    plt.xlabel('xᵢ')
    plt.ylabel('wᵢ')
    plt.xticks(xs)
    plt.yticks(ws)
    plt.show()

def print_empirical_distribution_func_interval_row(fstar, max_values_list):
    # Интервальный
    print()
    print("F*(x) Интервального ряда:")
    print(f"         ╭─0    при x < {max_values_list[1]}")
    for i in range(2, len(fstar)):
        if i == len(fstar) // 2:
            print(f"F*(x)  = │ {fstar[i-1]:<4} при {max_values_list[i - 1]:>5.2f} ≤ x < {max_values_list[i]:<5.2f}")
        else:
            print(f"         │ {fstar[i-1]:<4} при {max_values_list[i - 1]:>5.2f} ≤ x < {max_values_list[i]:<5.2f}")
    print(f"         ╰─1    при x > {max_values_list[-1]}")

def plot_empirical_distribution_func_interval_row(fstar, max_values_list):
    # график
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(max_values_list[0] - 1, min(0.0, max_values_list[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=8)
    plt.xlim((max_values_list[1] - 1, max_values_list[-1] + 1))
    plt.ylim((0, 1))
    plt.grid()  # относительные частоты
    plt.hlines(fstar, max_values_list, max_values_list[1:] + [max(max_values_list) + 1], linewidth=3, clip_on=False, colors='black')

    plt.scatter(max_values_list[1:], fstar[1:], marker='<', s=100, edgecolors='black', facecolors='black')


    plt.title('Эмпирическая функция распределения интервального ряда')
    plt.xlabel('xᵢ')
    plt.ylabel('F*(xᵢ)')
    plt.xticks(max_values_list)
    plt.yticks([0] + fstar + [1])

def print_empirical_distribution_func_grouped_row(fstar, ws, xs):
    # Группированный
    print()
    print("F*(x) Групированного ряда:")
    print(f"         ╭─0    при x < {xs[0]}")
    for i in range(1, len(ws)):
        if i == len(ws) // 2:
            print(f"F*(x)  = │ {fstar[i]:<4} при {xs[i - 1]:>2} ≤ x < {xs[i]:<2}")
        else:
            print(f"         │ {fstar[i]:<4} при {xs[i - 1]:>2} ≤ x < {xs[i]:<2}")
    print(f"         ╰─1    при x > {xs[-1]}")

def plot_empirical_distribution_func_grouped_row(fstar, xs):
    # график
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(xs[0] - 1, min(0.0, xs[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, 1, "^k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    plt.xlim((xs[0] - 1, xs[-1] + 1))
    plt.ylim((0, 1))
    plt.grid()  # относительные частоты
    plt.hlines(fstar, [xs[0] - 1] + xs, xs + [xs[-1] + 1], linewidth=3, clip_on=False, colors='black')
    tmp = fstar.pop(0)
    plt.scatter(xs, fstar, marker='<', s=100, edgecolors='black', facecolors='black')
    fstar.insert(0, tmp)

    plt.title('Эмпирическая функция распределения группированного ряда')
    plt.xlabel('xᵢ')
    plt.ylabel('F*(xᵢ)')
    plt.xticks(xs)
    plt.yticks([0] + fstar + [1])
    plt.show()

def numerical_characteristics_sample(length, xs, ns):
    print("Числовые характеристики выборки:")
    xmean = sum([x * y for x, y in zip(xs, ns)]) / length
    dmean = sum([((xmean - x) ** 2) * y for x, y in zip(xs, ns)]) / length
    sigmamean = dmean ** 0.5
    s = ((length * dmean) / (length - 1)) ** 0.5
    print(f"- ̄xᵦ = {xmean}\n- Dᵦ = {dmean}\n- σᵦ = {sigmamean}\n- Sᵦ = {s}")

def show_formulas():
	img = Image.open("image.png")
	plt.figure()
	plt.axis("off")
	plt.imshow(img)
	plt.show()

def main():
        
	data = get_data()
        
	length = len(data)

	unique_data = sorted(list(set(data)))

	max_value = max(unique_data)
	min_value = min(unique_data)
        
	max_values_list = []
	max_values_list.append(min_value)

	counter = min_value

	interval_count = floor(1 + 3.322 * log10(len(data)))
	interval = []
       
	step = (max_value - min_value) / interval_count
	
	while True:

		choice = get_user_choice()                  
		
		if choice == 1:
			print("\n1.")
			interval_count = int(input("Введите количество интервалов: "))
				
			print("interval_count:", interval_count)
		
			for i in range(interval_count - 1):
					interval.append([x for x in data if counter <= x and x < counter + step])
					counter += step
					max_values_list.append(counter)
																				
			interval.append([x for x in data if counter <= x])
			max_values_list.append(max_value)
			ns = [len(interval) for interval in interval]
			
			ws = [n / length for n in ns]
		
			print_interval_frequency_row(interval_count, min_value, max_value, step, ns)
			print_interval_relative_frequency_row(interval_count, min_value, max_value, step, ws)
			histogram_interval_frequency_row(step, unique_data, max_values_list, ns)
			histogram_interval_relative_frequency_row(step, unique_data, max_values_list, ws)
                  
			xs = [round((max_values_list[i] + max_values_list[i + 1]) / 2, 2) for i in range(interval_count)]
											
		elif choice == 2:
			print_frequency_rows(xs, ns, ws)
			plot_statistical_frequency_row(unique_data, ns, xs)
			plot_statistical_relative_frequency_row(unique_data, ws, xs)

		elif choice == 3:
			fstar = [0]
			for i in range(1, len(ws)):
					fstar.append(round(ws[i - 1] + fstar[i - 1], 5))
			fstar.append(1)
                  
			print_empirical_distribution_func_interval_row(fstar, max_values_list)          
			plot_empirical_distribution_func_interval_row(fstar, max_values_list)
			print_empirical_distribution_func_grouped_row(fstar, ws, xs)          
			plot_empirical_distribution_func_grouped_row(fstar, xs)
																		
		elif choice == 4:
			numerical_characteristics_sample(length, xs, ns)
			show_formulas()
																			
		elif choice == 0:
			print("\nПрограмма завершена.")                  
			break
    
		else:
			print("\nНеверно выбрано действие. Попробуйте снова.")

main()

