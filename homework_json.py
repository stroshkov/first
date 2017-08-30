import json


def get_cookbook():
  with open('cookbook.json', encoding='utf8') as file:
      cook_book = json.load(file)
      return cook_book
 
 
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cookbook = get_cookbook()
    for dish in dishes:
        for ingridient in cookbook[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['Количество'] *= person_count
            if new_shop_list_item['Название_ингредиента'] not in shop_list:
                shop_list[new_shop_list_item['Название_ингредиента']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['Название_ингредиента']]['Количество'] += new_shop_list_item['Количество']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['Название_ингредиента'], shop_list_item['Количество'],
                                shop_list_item['Единица измерения']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').title().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
