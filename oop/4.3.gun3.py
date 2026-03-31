"""
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь три метода экземпляра:
shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее
shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля
"""


class Gun:
    def __init__(self, try_num=0):
        self.try_num = try_num

    def shoot(self):
        self.try_num += 1
        if self.try_num % 2 != 0:
            print("pif")
        else:
            print("paf")

    def shots_count(self):
        return self.try_num

    def shots_reset(self):
        self.try_num = 0
