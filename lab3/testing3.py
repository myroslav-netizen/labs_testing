class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Богдан", "Анонім", "Мирослав"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Мирослав")
        if not hobby:
            raise ValueError("Хобі не може бути порожнім!")
        self.name = name
        self.hobby = hobby


a = Name("Андрій", "музика")
b = Name("Мирослав", "")
c = Name("Мирослав", "читання")
print(c.name, c.hobby)