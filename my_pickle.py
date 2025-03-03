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
        
        if protocol < 0 or protocol >5:
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
    
    
my_pickler_5 = MyPickler(protocol=5)


geography1 = my_pickler_5.pickle_data(geography)

geography1 = MyUnpickler.unpickle_data(geography1)
