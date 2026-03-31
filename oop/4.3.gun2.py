"""
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь один метод экземпляра:
shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее
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
