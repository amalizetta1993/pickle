import pickle

geography = {
    'Россия': 'Москва',
    'Беларусь': 'Минск',
    'Таиланд': 'Бангкок',
    'Китай': 'Пекин',
    'Индонезия': 'Джакарта',
    'Турция': 'Стамбул',
    'Малайзия': 'Куала - Лумпур',
}


class MyPickler:
    def __init__(self, protocol=pickle.DEFAULT_PROTOCOL):

        if protocol < 0 or protocol > 5:
            self.protocol = pickle.DEFAULT_PROTOCOL
        elif protocol == 0:
            self.protocol = pickle.HIGHEST_PROTOCOL
        else:
            self.protocol = protocol

    def pickle_data(self, data):
        pickled_data = pickle.dumps(data, self.protocol)
        return pickled_data

    def pickle_file(self, filename, data: object):
        with open(filename, 'wb') as fp:
            pickle.dump(data, fp, self.protocol)
        return f'Произведен пиклинг в файле {filename}'


class MyUnpickler:

    @classmethod
    def unpickle_data(cls, pickled_data):
        unpickle_data = pickle.loads(pickled_data)
        return unpickle_data

    @classmethod
    def unpickle_file(cls, pickled_filename):
        try:
            with open(pickled_filename, 'rb') as fp:
                unpickle_data = pickle.load(fp)
        except FileExistsError:
            return 'Файл не найден'
        return unpickle_data


def add_data(geography, country, capital):
    if country in geography:
        print(f"Страна {country} уже существует в базе данных")
        return False
    geography[country] = capital
    return True


def remove_data(geography, country):
    if country not in geography:
        print("Такой страны нет")
        return False
    geography.pop(country)
    return True


def search_data(geography, country):
    if country in geography:
        return geography[country]
    return print('Таких данных нет')


def edit_data(geography, country, new_capital):
    if country not in geography:
        print(f"Страна {country} не найдена в базе данных.")
        return False
    old_capital = geography[country]
    geography[country] = new_capital
    print(f"Обновлено: {country} - {old_capital} -> {new_capital}")
    return True


my_pickler_5 = MyPickler(protocol=5)
my_pickler_5.pickle_file('countries', geography)
stran = MyUnpickler.unpickle_file('countries')

add_data(stran, 'Япония', 'Токио')
print(stran)
remove_data(stran, 'Япония')
print(stran)
print(search_data(stran, 'Китай'))
edit_data(stran, 'Китай', 'Шанхай')
print(stran)
