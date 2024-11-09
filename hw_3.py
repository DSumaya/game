class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        result_division = self.cpu // self.memory
        result_multiplication  = self.cpu * self.memory
        return result_division, result_multiplication

    def __str__(self):
        return f"Computer(cpu={self.cpu}, memory={self.memory})"

    # Магические методы для сравнения
    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 0 < sim_card_number <= len(self.sim_cards_list):
            sim_card = self.sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")

    def __str__(self):
        return f"Phone(sim_cards_list={self.sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до локации: {location}")

    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})"


# Создание объектов
computer = Computer(20,5)
phone = Phone(["Beeline", "O!",])
smartphone1 = SmartPhone(8, 32,["Beeline"])
smartphone2 = SmartPhone(6, 64, ["O!"])

# Распечатка информации об объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print("Вычисления для компьютера:", computer.make_computations())

phone.call(1, "+996 777 99 88 11")

smartphone1.use_gps("Bishkek Park")
smartphone2.use_gps("Ala-Too")

print(computer == smartphone1)  # False
print(computer < smartphone2)   # True
