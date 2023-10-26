class AverageValue:
    """Класс для получения среднего значения из двух списков и их сравнения"""

    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def average_val(self):
        """Функция возвращает среднее значение из 2-х списков"""
        average_list_a = 0
        average_list_b = 0

        if self.list_a:
            average_list_a = sum(self.list_a) / len(self.list_a)
        if self.list_b:
            average_list_b = sum(self.list_b) / len(self.list_b)

        return average_list_a, average_list_b

    def comparison_average_val(self):
        """Функция возвращает результат сравнения 2-х средних значений"""

        average_list_a, average_list_b = self.average_val()

        if average_list_a > average_list_b:
            print('Первый список имеет большее среднее значение')
        elif average_list_b > average_list_a:
            print('Второй список имеет большее среднее значение')
        else:
            print('Средние значения равны')