import os

# Задание 1
with open('test.txt', encoding='utf-8') as file:
    cook_book = {}
    for word in file:
        recepie_name = word.strip() 
        ingredients_count = file.readline() 
        ingredients = []
        for i in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')   
            ingredient_name, quantity, measure = recepie
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})                    
            # ingredients.append({'ingredient_name': recepie[0], 'quantity': recepie[1], 'measure': recepie[2]})
        file.readline()
        cook_book[recepie_name] = ingredients
print(cook_book) 

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):  
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for i in cook_book[dish]:   
                # print(i)            
                if i['ingredient_name'] in result:
                    result[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count
                else:
                    result[i['ingredient_name']] = {'quantity': int(i['quantity']) * person_count, 'measure': i['measure']}
    print(result)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)    
    


# Задание 3
dic_file = {}
directory = r'C:\Users\Пользователь\Desktop\телепузик\Нетология\Открытие файлов\files'
for filename in os.listdir(directory):
    # print(filename)
    f = os.path.join(directory, filename)
    # print(f)
    with open(f, 'r', encoding='utf-8') as file:
        count = len(file.readlines())
        # print(count)
    with open(f, 'r', encoding='utf-8') as file:
        list = file.read()
        # print(list)
        dic_file[filename] = count, list
# print(dic_file)
dic_file_sort = sorted(dic_file.items(), key=lambda x: x[1])
# print(dic_file_sort)
for file_list in dic_file_sort:
    with open('newfile.txt', 'a', encoding='utf-8') as file:
        file.write(str(file_list[0]))
        file.write('\n')
        for i in file_list[1]:
            # print(i)
            file.write(str(i))
            file.write('\n')
