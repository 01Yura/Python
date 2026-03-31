"""
Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Postman должен иметь один атрибут:
delivery_data — изначально пустой список адресов, по которым следует доставить письма

Экземпляр класса Postman должен иметь три метода экземпляра:
add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов эти данные в виде кортежа:
(<улица>, <дом>, <квартира>)
get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице, в которые требуется доставить письма
get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в этом доме, в которые требуется доставить письма
"""


class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apt):
        self.delivery_data.append((street, house, apt))

    def get_houses_for_street(self, num_street):
        if self.delivery_data:
            li = [house for street, house, apt in self.delivery_data if street == num_street]
            result = []
            for house in li:
                if house not in result:
                    result.append(house)
            return result
        else:
            return []

    def get_flats_for_house(self, num_street, num_house):
        if self.delivery_data:
            li = [apt for street, house, apt in self.delivery_data if street == num_street and house == num_house]
            result = []
            for apt in li:
                if apt not in result:
                    result.append(apt)
            return result
        else:
            return []


class Postman2:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street):
        return list({h: None for s, h, _ in self.delivery_data if s == street})

    def get_flats_for_house(self, street, house):
        return list({a: None for s, h, a in self.delivery_data if s == street and h == house})


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))