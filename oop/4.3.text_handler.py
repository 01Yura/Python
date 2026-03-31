"""
Будем называть словом любую последовательность из одной или более букв. Текстом будем считать набор слов, разделенных пробельными символами.
Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса TextHandler должен иметь три метода:
add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
"""


class TextHandler:
    def __init__(self):
        self.li = []

    def add_words(self, text: str):
        self.li.extend(text.split())

    def get_shortest_words(self):
        if len(self.li) > 0:
            li = sorted(self.li, key=len)
            shortest_length = len(li[0])
            return [word for word in self.li if len(word) == shortest_length]
        else:
            return self.li

    def get_longest_words(self):
        if len(self.li) > 0:
            li = sorted(self.li, key=len, reverse=True)
            longest_length = len(li[0])
            return [word for word in self.li if len(word) == longest_length]
        else:
            return self.li

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())


class TextHandler2:
    def __init__(self):
        self.words = []
        self.shortest = 0
        self.longest = 0

    def add_words(self, words):
        words = words.split()
        self.words.extend(words)
        self.shortest = min(map(len, self.words))
        self.longest = max(map(len, self.words))

    def get_shortest_words(self):
        return [w for w in self.words if len(w) == self.shortest]

    def get_longest_words(self):
        return [w for w in self.words if len(w) == self.longest]