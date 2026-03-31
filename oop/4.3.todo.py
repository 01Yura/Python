"""
Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Todo должен иметь один атрибут:
things — изначально пустой список дел, которые нужно выполнить

Класс Todo должен иметь четыре метода экземпляра:
add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде кортежа:
(<название дела>, <приоритет>)
get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n
get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет
"""


class Todo:
    def __init__(self):
        self.things = []

    def add(self, name, priority):
        self.things.append((name, priority))

    def get_by_priority(self, n):
        if len(self.things) > 0:
            return [name for name, priority in self.things if priority == n]
        return []

    def get_low_priority(self):
        if len(self.things) > 0:
            lowest_priority = min(map(lambda el: el[1], self.things))
            return [name for name, priority in self.things if priority == lowest_priority]
        return []

    def get_high_priority(self):
        if len(self.things) > 0:
            highest_priority = max(map(lambda el: el[1], self.things))
            return [name for name, priority in self.things if priority == highest_priority]
        return []


todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())
