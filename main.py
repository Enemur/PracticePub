from DataBase.db import DataBase

try:
    DataBase.callFunction('set_model', 'Artem', 'yellow')
    res = DataBase.callFunction('get_model', 1)
    print(res)
except Exception as error:
    print(str(error))