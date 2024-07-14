"""Количество выполненных ДЗ (запишите значение 12)
Количество затраченных часов (запишите значение 1.5)
Название курса (запишите значение 'Python')
Время на одно задание (вычислить используя 1 и 2 переменные)
Выведите на экран(в консоль), используя переменные, следующую строку:
Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа."""


number_of_completed_requests = 12
Number_of_hours_spent = 1.5
Course_name = 'Python'
Time_per_task = Number_of_hours_spent / number_of_completed_requests
print("Курс:", Course_name, 'всего задач:', number_of_completed_requests, "затрачено часов:", Number_of_hours_spent,
      "среднее время выполнения", Time_per_task, "часа.")