class Tomat:

    states = {0: 'Не зрелый', 1: 'Цветение', 2: 'Зеленый томат', 3: 'Красный томат'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomat {self._index} is {Tomat.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomat(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Сбор урожая...')
        self._plant.grow_all()
        print('Сбор урожая завершен')

    def harvest(self):
        print('Сбор урожая...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая завершен')
        else:
            print('Не созрело ещё.')

    @staticmethod
    def knowledge_base():
        print('''Время сбора урожая томатов в идеале должно наступать
, когда плоды становятся зрелыми зелеными, а
затем им дают созреть на лозе.''')

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Jenifer', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()