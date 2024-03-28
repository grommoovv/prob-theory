from matplotlib import pyplot as plt
from PIL import Image
from matplotlib import pyplot as plt

def get_data():
	interval_count = int(input("Введите количество интервалов: "))
	data = set()
	freq = []
	for i in range(interval_count):
			[data.add(float(x)) for x in input(f"Введите {i + 1}-ый интервал в формате xᵢ;xᵢ₊₁: ").split(';')]
			freq.append(int(input(f"Введите {i + 1}-ую частоту: ")))

	data = sorted(list(data))
	return data, freq, interval_count

def get_user_choice():
    print()
    print("\nВыберите интересующие вас пункты:\n\
          1. Получение и вывод на экран интервального ряда частот и относительных частот, построение соответствующих гистограмм;\n\
          2. Построение группированного ряда распределения частот и относительных частот и построение соответствующих полигонов;\n\
          3. Нахождение и вывод на экран эмпирической функции распределения F*(х) для интервальных и группированных рядов, построение их графиков;\n\
          4. Вывод на экран формул для вычисления числовых характеристик выборки: ̄xᵦ, Dᵦ, σᵦ, Sᵦ, их вычисление и вывод на экран полученных результатов;\n\
          5. Завершить программу;\n")
    return int(input("Введите необходимый номер: "))

def print_interval_frequency_row(intervalAmount, xnmax, ns):
    # Частоты
    print("\nИнтервальный ряд частот:")
    print()
    print("┃xᵢ;xᵢ₊₁┃", end='')
    for i in range(intervalAmount - 1):
        print(f"{xnmax[i]:>6.2f};{xnmax[i + 1]:<6.2f}", end='┃')
    print(f"{xnmax[-2]:>6.2f};{xnmax[-1]:<6.2f}", end='┃')
    print("\n┃  nᵢ   ┃", end='')
    [print(f"{n:^13}", end='┃') for n in ns]
    print()

def print_interval_relative_frequency_row(intervalAmount, xnmax, ws):
    # Относительные частоты
    print("Интервальный ряд относительных частот:")
    print()
    print("┃xᵢ;xᵢ₊₁┃", end='')
    for i in range(intervalAmount - 1):
        print(f"{xnmax[i]:>6.2f};{xnmax[i + 1]:<6.2f}", end='┃')
    print(f"{xnmax[-2]:>6.2f};{xnmax[-1]:<6.2f}", end='┃')
    print("\n┃  wᵢ   ┃", end='')
    [print(f"{w:^13}", end='┃') for w in ws]
    print()

def histogram_interval_frequency_row(xnmax, ns):
    # Гистограммы
    # Частоты
    rangens = [n / (xnmax[1] - xnmax[0]) for n in ns]
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(xnmax[0] - 1, min(0.0, xnmax[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, max(rangens), "^k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.text(0, 0, '0', color='black', fontsize=12, ha='right', va='bottom')
    plt.xlim((xnmax[0] - 1, xnmax[-1] + 1))
    plt.ylim((0, max(rangens) + max(rangens) / 100))
    plt.grid()  # частоты
    plt.stairs(rangens, xnmax, fill=True, facecolor="yellow", edgecolor="black", linewidth=1.8, zorder=3)
    plt.vlines(xnmax[1:-1], 0, rangens[:-1], color="black", zorder=4)
    title_font = {'family': 'monospace', 'style': 'italic', 'weight': 'bold', 'size': 18, 'stretch': 'normal',
                  'color': 'black'}
    plt.title('Гистограмма интервального ряда частот', fontdict=title_font)
    plt.xlabel('xᵢ', fontsize=18)
    plt.ylabel('nᵢ', fontsize=18)
    plt.xticks(xnmax)
    plt.yticks(rangens)

def histogram_interval_relative_frequency_row(xnmax, ws):
    # Относительные частоты
    rangews = [w / (xnmax[1] - xnmax[0]) for w in ws]
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(xnmax[0] - 1, min(0.0, xnmax[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, max(rangews), "^k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.text(0, 0, '0', color='black', fontsize=12, ha='right', va='bottom')

    # plt.style.use('ggplot')
    plt.xlim((xnmax[0] - 1, xnmax[-1] + 1))
    plt.ylim((0, max(rangews) + max(rangews) / 100))
    plt.grid()  # частоты
    plt.stairs(rangews, xnmax, fill=True, facecolor="red", edgecolor="black", linewidth=1.8, zorder=3)
    plt.vlines(xnmax[1:-1], 0, rangews[:-1], color="black", zorder=4)
    title_font = {'family': 'monospace', 'style': 'italic', 'weight': 'bold', 'size': 18, 'stretch': 'normal',
                  'color': 'black'}
    plt.title('Гистограмма интервального ряда относительных частот', fontdict=title_font)
    plt.xlabel('xᵢ', fontsize=18)
    plt.ylabel('wᵢ', fontsize=18)
    plt.xticks(xnmax)
    plt.yticks(rangews)
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

def plot_statistical_frequency_row(xnmax, ns, xs):
    # Найти и вывести полигоны частот
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(xnmax[0] - 1, min(0.0, xnmax[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, max(ns), "^k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    plt.xlim((xnmax[0] - 1, xnmax[-1] + 1))
    plt.ylim((0, max(ns) + max(ns) / 100))
    plt.grid()  # частоты
    plt.plot(xs, ns, linewidth=3, color='orange')
    title_font = {'family': 'monospace', 'style': 'italic', 'weight': 'bold', 'size': 18, 'stretch': 'normal',
                  'color': 'black'}
    plt.title('Полигон статистического ряда частот', fontdict=title_font)
    plt.xlabel('xᵢ', fontsize=18)
    plt.ylabel('nᵢ', fontsize=18)
    plt.xticks(xs)
    plt.yticks(ns)

def plot_statistical_relative_frequency_row(xnmax, ws, xs):
    # Относительных частот
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(xnmax[0] - 1, min(0.0, xnmax[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, max(ws), "^k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    plt.xlim((xnmax[0] - 1, xnmax[-1] + 1))
    plt.ylim((0, max(ws) + max(ws) / 100))
    plt.grid()
    plt.plot(xs, ws, linewidth=3, color='red')
    title_font = {'family': 'monospace', 'style': 'italic', 'weight': 'bold', 'size': 18, 'stretch': 'normal',
                  'color': 'black'}
    plt.title('Полигон статистического ряда относительных частот', fontdict=title_font)
    plt.xlabel('xᵢ', fontsize=18)
    plt.ylabel('wᵢ', fontsize=18)
    plt.xticks(xs)
    plt.yticks(ws)
    plt.show()

def print_empirical_distribution_func_interval_row(fstar, xnmax):
    # Интервальный
    print()
    print("F*(x) Интервального ряда:")
    print(f"         ╭─0    при x < {xnmax[1]}")
    for i in range(2, len(fstar)):
        if i == len(fstar) // 2:
            print(f"F*(x)  = │ {fstar[i-1]:<4} при {xnmax[i - 1]:>5.2f} ≤ x < {xnmax[i]:<5.2f}")
        else:
            print(f"         │ {fstar[i-1]:<4} при {xnmax[i - 1]:>5.2f} ≤ x < {xnmax[i]:<5.2f}")
    print(f"         ╰─1    при x > {xnmax[-1]}")

def plot_empirical_distribution_func_interval_row(fstar, xnmax):
    # график
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', max(xnmax[0] - 1, min(0.0, xnmax[-1] + 1))))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(0, 1, "^k", transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    plt.xlim((xnmax[0] - 1, xnmax[-1] + 1))
    plt.ylim((0, 1))
    plt.grid()  # относительные частоты
    plt.hlines(fstar, xnmax, xnmax[1:] + [max(xnmax) + 1], linewidth=3, clip_on=False, colors='black')

    plt.scatter(xnmax[1:], fstar[1:], marker='<', s=100, edgecolors='black', facecolors='black')


    title_font = {'family': 'monospace', 'style': 'italic', 'weight': 'bold', 'size': 18, 'stretch': 'normal',
                  'color': 'black'}
    plt.title('Эмпирическая функция распределения', fontdict=title_font)
    plt.xlabel('xᵢ', fontsize=18)
    plt.ylabel('F*(xᵢ)', fontsize=18)
    plt.xticks(xnmax)
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
    title_font = {'family': 'monospace', 'style': 'italic', 'weight': 'bold', 'size': 18, 'stretch': 'normal',
                  'color': 'black'}
    plt.title('Эмпирическая функция распределения', fontdict=title_font)
    plt.xlabel('xᵢ', fontsize=18)
    plt.ylabel('F*(xᵢ)', fontsize=18)
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
       
	data, freq, intervalAmount = get_data()

	main = sum(freq)
	ws = [n / main for n in freq]

	while True:
		choice = get_user_choice()

		if choice == 1:
			print_interval_frequency_row(intervalAmount, data, freq)
			print_interval_relative_frequency_row(intervalAmount, data, ws)
			histogram_interval_frequency_row(data, freq)
			histogram_interval_relative_frequency_row(data, ws)
				
		xs = [round((data[i] + data[i + 1]) / 2, 2) for i in range(intervalAmount)]
								
		if choice == 2:
			print_frequency_rows(xs, freq, ws)
			plot_statistical_frequency_row(data, freq, xs)
			plot_statistical_relative_frequency_row(data, ws, xs)
				
		if choice == 3:
			fstar = [0]
			for i in range(1, len(ws)): fstar.append(round(ws[i - 1] + fstar[i - 1], 5))
			fstar.append(1)
			print_empirical_distribution_func_interval_row(fstar, data)
			plot_empirical_distribution_func_interval_row(fstar, data)
			print_empirical_distribution_func_grouped_row(fstar, ws, xs)
			plot_empirical_distribution_func_grouped_row(fstar, xs)
				
		if choice == 4:
			numerical_characteristics_sample(main, xs, freq)
			show_formulas()
                  
		if choice == 0:
			print("Программа завершена.")
			break

main()
