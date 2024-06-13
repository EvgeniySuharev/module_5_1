class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor_list = []
        if new_floor < 1 or new_floor > self.number_of_floors:
            return print('Такого этажа не существует')
        for i in range(1, new_floor + 1):
            floor_list.append(i)
        return print(*floor_list)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
