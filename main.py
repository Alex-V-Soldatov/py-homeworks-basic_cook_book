import os

path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path) as f:
    book = {}
    for string in f:
        dish = string.strip()  
        ingredient_quantity = int(f.readline().strip())  
        dish_book = []  
        for i in range(ingredient_quantity):
            ingredient_name, quantity, measure = f.readline().strip().split('|')
            dish_book.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        book[dish] = dish_book  
        f.readline()  


def get_shop_list_by_dishes(dishes, persons_quantity):
    grocery_quantity = {}  
    for i in dishes:
        for ingredient in book[i]:  
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * persons_quantity,
                                      'measure': ingredient['measure']})])
            if grocery_quantity.get(ingredient['ingredient_name']) == 'None':
                res = (int(grocery_quantity[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_quantity[ingredient['ingredient_name']]['quantity'] = res
            else:
                grocery_quantity.update(ingredient_list)
    return grocery_quantity


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос', 'Омлет', 'Запеченный картофель'], 5))