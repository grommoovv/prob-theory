import math

def get_user_choice():
	print(f"\nВыберите задачу из списка ниже:")
	print(f"1. Электрическая цепь из пяти элементов составлена по схеме, приведенной на рисунке. Найти вероятность разрыва цепи, предполагая, что отказы отдельных элементов независимы и равны qi=(1,2,3,4,5).")
	print(f"2. Один студент выучил m1 из n вопросов программы, а второй m2. Каждому из них задают по три вопроса. Найти вероятность того, что не менее, чем на два вопроса правильно ответят:")
	print(f"	a) оба студента;")
	print(f"	b) только первый студент;")
	print(f"	c) только один из них;")
	print(f"	d) хотя бы один из студентов.")
	print(f"3. Составить задачу.")
	print(f"0. Завершить программу.")
	return int(input("\nВведите номер задачи: "))

def main():

	while True:

		choice = get_user_choice()
		
		if choice == 1:

			# Схема из 2 Варианта
			print("Формула выражающая сложное событие A через Аi простые: A=(A1+A4)*A3*(A2+A5)")
			print("Формула дня нахождения вероятности, что цепь выйдет из строя P(A)=(P(A1)+P(A4)-P(A1*A4))*P(A3)*(P(A2)+P(A5)-P(A2*A5))")

			failure_probability_list = [0, 0, 0, 0, 0]
			work_probability_list = [0, 0, 0, 0, 0]

			for i in range(0, 5):
					while True:
						failure_probability_list[i] = float(input(f"Укажите вероятность отказа [0;1] элемента P(A{i+1}): "))

						if failure_probability_list[i] > 1 or failure_probability_list[i] < 0: print("\nУкажите допустимое значение вероятности отказа.")
						else: break

			for i in range(0, 5):
					work_probability_list[i] = 1-failure_probability_list[i]
					print(f"Вероятность работы элемента P(A{i+1}) = {work_probability_list[i]:.{5}f}")

			result = (failure_probability_list[0]+failure_probability_list[3]-(failure_probability_list[0] * failure_probability_list[3]))*failure_probability_list[2]*(failure_probability_list[1]+failure_probability_list[4]-(failure_probability_list[1]*failure_probability_list[4]))

			print(f"По формуле P(A)=({failure_probability_list[0]}+{failure_probability_list[3]}-({failure_probability_list[0]}*{failure_probability_list[3]})*{failure_probability_list[2]}*({failure_probability_list[1]}+{failure_probability_list[4]}-({failure_probability_list[1]}*{failure_probability_list[4]})={result}")

		elif choice == 2:
			print(f"\nВероятность того что первый студент ответит не менее чем на 2 вопроса - Р(А1)=(С(m1;2)*С(n-m1))/C(n;3)+C(m1;3)/C(n;3)")
			print(f"Вероятность того что второй студент ответит не менее чем на 2 вопроса - Р(А2)=(С(m2;2)*С(n-m2))/C(n;3)+C(m2;3)/C(n;3)")

			def one(m):
				return math.factorial(m) // (math.factorial(2) * math.factorial(m - 2))
					
			def two(n, m):
				return math.factorial(n-m) // (math.factorial(1) * math.factorial((n - m) - 1))
					
			def three(n):
				return math.factorial(n) // (math.factorial(3) * math.factorial(n - 3))
			
			def four(m):
				return math.factorial(m) // (math.factorial(3) * math.factorial(m - 3))
			
			n = int(input("\nВведите общее количество вопросов (n): "))

			while True:
				m1 = int(input("Введите количество вопросов, которое выучил первый студент (m1): "))
				m2 = int(input("Введите количество вопросов, которое выучил второй студент (m2): "))

				if m1 < 2 and m2 < 2: print(f"\nКоличество вопросов, которые выучили студенты, не должно быть меньше двух.\n")
				else: break
					
			p1 = (one(m1)*two(n,m1)/three(n))+(four(m1)/three(n))
			p2 = (one(m2)*two(n,m2)/three(n))+(four(m2)/three(n))

			print(f"\nВероятность того что первый студент ответит не менее чем на 2 вопроса - {p1}")
			print(f"Вероятность того что второй студент ответит не менее чем на 2 вопроса - {p2}")
			print(f"a) оба студента - P(A1) * P(A2) = {p1*p2};")
			print(f"b) только первый студент - P(A1) * (1-P(A2)) = {p1*(1-p2)};")
			print(f"c) только один из них - (P(A1) * (1-P(A2))) + ((1-P(A1))*P(A2) = {(p1*(1-p2))+((1-p1)*p2)};")
			print(f"d) хотя бы один из студентов - 1 - ((1-(P(A1))*(1-P(A2)) = {1-((1-p1) * (1-p2))}.")

		elif choice == 3:
			list_one = []
			list_two = []
			list_three = []

			is_events_count_correct = 0

			hypothesis_sum = 0

			formula = int(input(f"3.Выберите формулу: (0-Полная вероятность; 1-Байеса): "))

			while is_events_count_correct == 0:
				events_count = int(input(f"Введите количество событий [2;8]: "))
				if events_count < 2 or events_count > 8: print(f"Введите доступное количество событий")
				else: is_events_count_correct = 1

			for i in range(events_count):
				hypothesis = float(input(f"Введите вероятность гипотезы P(H{i+1}): "))
				list_one.append(hypothesis)
				hypothesis_sum += hypothesis
				if hypothesis_sum > 1:
					print(f"Сумма гипотез не должна привышать 1")
					list_one.pop(len(list_one))

			for i in range(events_count):
				conditional_probabilities = float(input(f"Введите условные вероятности P(A|H{i+1}): "))
				list_two.append(conditional_probabilities)

			if formula == 0:
				hypothesis_sum = 0

				print(f"Формула полной вероятности: P(A)=sigma(P(Hi)*P(A|Hi))")

				for i in range(len(list_one)): hypothesis_sum += list_one[i] * list_two[i]

				print(f"Вероятность {hypothesis_sum:.{5}f}")

			if formula == 1:
				hypothesis_sum = 0

				for i in range(len(list_one)): 
					hypothesis_sum += list_one[i] * list_two[i]

				for i in range(len(list_one)): 
					list_three.append(list_one[i] * list_two[i] / hypothesis_sum)

				print(f"Полная веротяность равна {hypothesis_sum:.{5}f}")

				for i in range(len(list_three)): 
					print(f"Вероятность Байеса {i + 1}-й гипотезы {list_three[i]:.{5}f})")

		elif choice == 0:
			print(f"\nПрограмма завершена.")
			break

		else:
			print(f"\nВы ввели неверный номер задачи. Попробуйте снова.\n")

main()