from random import randint
import matplotlib.pyplot as plt

class WiFy:
    """Контроллер Wi-Fy
    """

    _instance = None
    

    @classmethod
    def __traffic_shaping(cls):
        """Формирование трафика
        """
        total_consumption = cls.consumption * randint(1,64)
        with open("traffic.txt",mode="a") as wf:
            wf.write(str(total_consumption))
            wf.write("\n")

    def __new__(cls, name: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.name = name # Имя сети
            cls.consumption = 1 # Рассход трафика на пользователя
            cls.__traffic_shaping()
        return cls._instance
    
    def viewing(self):
        """Просмотр трафика
        """

        plt.title(f"Трафик {self.name}")
        plt.ylabel("Мб")
        num = []
        with open("traffic.txt",mode="r") as rf:
            for i in rf.readlines():
                lst = i.split("\n")
                num.append(int(lst[0]))
        plt.plot(num)
        plt.show()




a = WiFy("Tenda")
#a.viewing()

b = WiFy("Kievstar")
#b.viewing()

bc = WiFy("Kievstarsss")
#bc.viewing()

bd = WiFy("Kievstarqwqwq")
bd.viewing()