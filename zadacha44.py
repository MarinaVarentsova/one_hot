# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
# print(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)
print('перевод в one hot вид')
print(pd.get_dummies(data['whoAmI'], dtype=int))
