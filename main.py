from Balance_analysis_models.task_one.Task_one_model import Task_one
from Balance_analysis_models.task_two.Task_two_model import Task_two
import time


b11 = int(input("Сільське  господарство | Сільське  господарство: "))
b12 = int(input("Сільське  господарство | Промисловість: "))
b13 = int(input("Сільське  господарство | Транспорт: "))
print("____________________________________________________")
time.sleep(1)
b21 = int(input("Промисловість | Сільське  господарство: "))
b22 = int(input("Промисловість | Промисловість: "))
b23 = int(input("Промисловість | Транспорт: "))
print("____________________________________________________")
time.sleep(1)
b31 = int(input("Транспорт | Сільське  господарство: "))
b32 = int(input("Транспорт | Промисловість: "))
b33 = int(input("Транспорт | Транспорт: "))
print("____________________________________________________")
time.sleep(1)
x11 = int(input("Загальний випуск  Сільське  господарство : "))
x21 = int(input("Загальний випуск  Промисловість : "))
x31 = int(input("Загальний випуск  Транспорт : "))
print("____________________________________________________")
time.sleep(1)
y11 = int(input("Кінцевий попит Сільське  господарство : "))
y21 = int(input("Кінцевий попит Промисловість : "))
y31 = int(input("Кінцевий попит Транспорт : "))
print("____________________________________________________")
time.sleep(1)
percent = int(input("Процент змін попиту : "))
print("____________________________________________________")
time.sleep(1)
v1 = float(input("Сільське  господарство : "))
v2 = float(input("Промисловість : "))
v3 = float(input("Транспорт : "))
print("____________________________________________________")
time.sleep(1)
enter_options = int(input("Введіть номер завдання : "))
print("____________________________________________________")
time.sleep(1)


class Main:
    def __init__(self, b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31, n, v1, v2, v3):
        self.v3 = v3
        self.v2 = v2
        self.v1 = v1
        self.n = n
        self.y31 = y31
        self.y21 = y21
        self.y11 = y11
        self.x31 = x31
        self.x21 = x21
        self.x11 = x11
        self.b33 = b33
        self.b32 = b32
        self.b31 = b31
        self.b23 = b23
        self.b22 = b22
        self.b21 = b21
        self.b13 = b13
        self.b12 = b12
        self.b11 = b11
        self.t_o = Task_one(b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31, n)
        self.t_t = Task_two(b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31, v1, v2, v3)

    def result_task_one(self):
        return f"Матриця А : {self.t_o.calculation_A_matrix()} \n" \
               f"_____________________________________________ \n" \
               f"Матриця D : {self.t_o.calculation_D_matrix()} \n" \
               f"_____________________________________________ \n" \
               f"Матриця X : {self.t_o.calculation_X_matrix()} \n" \
               f"_____________________________________________ \n" \
               f"Фінальний результат : {self.t_o.final_calculation()} \n" \
               f"_____________________________________________ \n"

    def result_task_two(self):
        return f"Матриця P : {self.t_t.calculation_P_matrix()} \n" \
               f"_____________________________________________ \n"


if __name__ == '__main__':
    main = Main(b11, b12, b13, b21, b22, b23, b31, b32, b33, x11, x21, x31, y11, y21, y31, percent, v1, v2, v3)
    if enter_options == 1:
        print(main.result_task_one())
    elif enter_options == 2:
        print(main.result_task_two())