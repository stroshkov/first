import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

#можете посмотреть содержимое файлв с квартирами через print, можете - на вкладке output.csv
#print (flats_list)


#TODO 1:
#Напишите цикл, который проходит по всем квартирам, и печатает только новостройки
#и их порядковые номера в файле. Подсказка:
for i, flat in enumerate(flats_list):
  if "новостройка" in flat:
    print('Квартира с таким порядковым номером {0} является новостройкой'.format(i))


#TODO 2:
#При помощи пересечения множеств попробуйте сравнить больше двух новостроек между собой одновременно
# например, пересечение 3 и 6 квартиры из файла с ЦИАНа делается так:
# flats_intersesction = set(flats_list[2]) & set(flats_list[5])
# Порядковые номера новостроек вы уже получили при выполнении предыдущего задания.
# Не забудьте вывести результат функцией print


flats_intersesction = set(flats_list[10]) & set(flats_list[30]) & set(flats_list[66])
print(flats_intersesction)


# TODO3:
#Вот так мы превратили наш массив квартир в словарь, где ключом является уникальный номер объявления,
#а значением - ссылка на страничку с объявлением.
# #Измените код так, чтобы стало наоборот.
test_dict = dict()
for i, flat in enumerate(flats_list):
  if i == 0:
    continue
  test_dict[flat[len(flat)-1]] = flat[0]
  # test_dict[flat[0]] = flat[len(flat)-1]
print (test_dict)
