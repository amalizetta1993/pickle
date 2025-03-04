import pickle

music = {
    'Pink Floyd': 'The wall',
    'Nirvana': 'Nivermind',
    'AC/DC': 'Back in Black',
    'Coldplay': 'A head full of dreams'
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


def add_data(musica, gruppa, album):
    if gruppa in musica:
        print(f"Группа {gruppa} уже существует в базе данных")
        return False
    musica[gruppa] = album
    return True


def remove_data(musica, gruppa):
    if gruppa not in musica:
        print("Такой страны нет")
        return False
    musica.pop(gruppa)
    return True


def search_data(musica, gruppa):
    if gruppa in musica:
        return musica[gruppa]
    return print('Таких данных нет')


def edit_data(musica, gruppa, new_album):
    if gruppa not in musica:
        print(f"Страна {gruppa} не найдена в базе данных.")
        return False
    old_capital = musica[gruppa]
    musica[gruppa] = new_album
    print(f"Обновлено: {gruppa} - {old_capital} -> {new_album}")
    return True


my_pickler_5 = MyPickler(protocol=5)
my_pickler_5.pickle_file('music_albums', music)
mus = MyUnpickler.unpickle_file('music_albums')

add_data(mus, 'Селин Дион', 'Falling into You')
print(mus)
remove_data(mus, 'AC/DC')
print(mus)
print(search_data(mus, 'Nirvana'))
edit_data(mus, 'Nirvana', 'In Utero')
print(mus)
