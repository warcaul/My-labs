from enum import IntEnum
import math
import openpyxl
class start_end:
    """
    Класс ввода и вывода данных
    """
    def __init__(self):
        """
        Метод инициации. Пустая так как не требуется вводить атрибуты.
        """
        pass
    def hand (self):
        """
        Метод ручного ввода данных. Сначала запрашивает количество данных, а потом сами данные.
        """
        a = float(input("Кількість значень"))
        x=0
        while x < a:
            b = float(input("Значення Х"))
            S.append(b)
            x += 1
        return(S)
    def ef (self):
        """
        Метод ввода данных из файла формата .xlsx. Использует библиотеку openpyxl. Читает данные с первого столбца
        """
        wb = openpyxl.load_workbook("test.xlsx" , read_only=True)
        sheet = wb.active
        for row in sheet.rows:
            a = float(row[0].value)
            S.append(a)
    def file_out (self):
        """
        Вывод данных в файл. Выводить в три строки:
        1 - список данных
        2 - среднее арифметическое
        3 - средняя квадратическая погрешность
        """
        output = open('answer.txt', 'w')
        output.write(str(answer_list) + '\n')
        output.write(str(answer_mv) + '\n')
        output.write(str(answer_rms) + '\n')
        output.close
        output.close
    def console (self):
        """
        Вывод данных в консоль. Выводит в три строчки:
        1 - список данных
        2 - среднее арифметическое
        3 - средняя квадратическая погрешность
        """
        print("список експериментальних даних" , answer_list)
        print("середнє значення величини" , answer_mv)
        print("середня квадратична похибка середнього" , answer_rms)

class calculate:
    """
    Класс обчисления данных
    """
    def __init__(self,S=[]):
        self.S=S
    """
    Инициализация класса. Ввод списка как атрибута.
    """
    def mv (self):
        """
        Метод расчета среднего арифметического. Считает длину списка и суму всех его елементов, затем делит их между собой.
        """
        a = math.fsum(self.S)
        b =  len(self.S)
        answer_mv = a/b
        return(answer_mv)
    
    def rms (self):
        """
        Метод расчета средней квадратической погрешности. Считает длину списка и суму всех его елементов. 
        Затем считает среднее арифметическое. Создает список квадратов отклонения от среднего для каждого значения списка данных
        Считает сумму нового списка. Высичляет  среднюю квадратическую погрешность среднего
        """
        a = math.fsum(self.S)
        b = len(self.S)
        m = a/b
        L1 = []
        for i in self.S:
            c = (i-m)**2
            L1.append(c)
        c = math.fsum(L1)
        d = b * (b-1)
        answer_rms = math.sqrt (c/d)
        return(answer_rms)


S=[]
"""
Создает пустой список данных
"""
p = input("Файл Excel або вручну")
"""
Выбор способа ввода данных
"""
if p == "Файл Excel":
    p = start_end()
    p.ef()
    pass
elif p == "вручну":
    p = start_end()
    p.hand()
    pass
else: print("Невідомий формат")

answer_list = S
S = calculate(S)
answer_rms = S.rms()
answer_mv = S.mv()
"""
Вычисление среднего значения и средней квадратической погрешности среднего
"""

q = input("Файл  або консоль")
"""
Выбор способа вывода данных
"""
if q == "Файл":
    q = start_end ()
    q.file_out()
    pass
elif q == "консоль":
    q = start_end ()
    q.console()
    pass
else: print("Невідомий формат")
